#include "types.h"
#include "stat.h"
#include "user.h"
#include "x86.h"

struct balance {
    char name[32];
    int amount;
};

struct thread_spinlock {
	uint locked;       // Is the lock held?

	// For debugging:
	char *name;        // Name of lock.
};

struct thread_mutex {
	uint locked;       // Is the lock held?

	// For debugging:
	char *name;        // Name of lock.
};

void
thread_spin_init(struct thread_spinlock *lk, char *name)
{
	lk->name = name;
	lk->locked = 0;
}

// Acquire the lock.
// Loops (spins) until the lock is acquired.
// Holding a lock for a long time may cause
// other CPUs to waste time spinning to acquire it.
void
thread_spin_lock(struct thread_spinlock *lk)
{
	// The xchg is atomic.
	while (xchg(&lk->locked, 1) != 0)
		;

	// Tell the C compiler and the processor to not move loads or stores
	// past this point, to ensure that the critical section's memory
	// references happen after the lock is acquired.
	__sync_synchronize();

}

// Release the lock.
void
thread_spin_unlock(struct thread_spinlock *lk)
{

	// Tell the C compiler and the processor to not move loads or stores
	// past this point, to ensure that all the stores in the critical
	// section are visible to other cores before the lock is released.
	// Both the C compiler and the hardware may re-order loads and
	// stores; __sync_synchronize() tells them both not to.
	__sync_synchronize();

	// Release the lock, equivalent to lk->locked = 0.
	// This code can't use a C assignment, since it might
	// not be atomic. A real OS would use C atomics here.
	asm volatile("movl $0, %0" : "+m" (lk->locked) : );
}

void
thread_mutex_init(struct thread_mutex *m, char *name)
{
	m->name = name;
	m->locked = 0;
}

// Acquire the lock.
// Loops (spins) until the lock is acquired.
// Holding a lock for a long time may cause
// other CPUs to waste time spinning to acquire it.
void
thread_mutex_lock(struct thread_mutex *m)
{
	// The xchg is atomic.
	while (xchg(&m->locked, 1) != 0)
		sleep(1);

	// Tell the C compiler and the processor to not move loads or stores
	// past this point, to ensure that the critical section's memory
	// references happen after the lock is acquired.
	__sync_synchronize();

}

// Release the lock.
void
thread_mutex_unlock(struct thread_mutex *m)
{

	// Tell the C compiler and the processor to not move loads or stores
	// past this point, to ensure that all the stores in the critical
	// section are visible to other cores before the lock is released.
	// Both the C compiler and the hardware may re-order loads and
	// stores; __sync_synchronize() tells them both not to.
	__sync_synchronize();

	// Release the lock, equivalent to lk->locked = 0.
	// This code can't use a C assignment, since it might
	// not be atomic. A real OS would use C atomics here.
	asm volatile("movl $0, %0" : "+m" (m->locked) : );
}

struct thread_spinlock lock;
struct thread_mutex mlock;

volatile int total_balance = 0;

volatile unsigned int delay (unsigned int d) {
    unsigned int i;
    for (i = 0; i < d; i++) {
        __asm volatile( "nop" ::: );
    }

    return i;
}

void do_work(void *arg){
    int i;
    int old;

    struct balance *b = (struct balance*) arg;
    printf(1, "Starting do_work: s:%s\n", b->name);

    for (i = 0; i < b->amount; i++) {
      //  thread_mutex_lock(&mlock);
        old = total_balance;
        delay(10000);
        total_balance = old + 1;
        //thread_mutex_unlock(&mlock);
    }

    printf(1, "Done s:%x\n", b->name);

    thread_exit();
    return;
}

int main(int argc, char *argv[]) {

    struct balance b1 = {"b1", 3200};
    struct balance b2 = {"b2", 2800};

    void *s1, *s2;
    int t1, t2, r1, r2;

    s1 = malloc(4096);
    s2 = malloc(4096);

    t1 = thread_creation(do_work, (void*)&b1, s1);
    t2 = thread_creation(do_work, (void*)&b2, s2);

    r1 = thread_join();
    r2 = thread_join();

    printf(1, "Threads finished: (%d):%d, (%d):%d, shared balance:%d\n",
           t1, r1, t2, r2, total_balance);

    exit();
}