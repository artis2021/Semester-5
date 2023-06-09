#include "types.h"
#include "x86.h"
#include "defs.h"
#include "date.h"
#include "param.h"
#include "memlayout.h"
#include "mmu.h"
#include "proc.h"
#include "processInfo.h"

int
sys_fork(void)
{
  return fork();
}

int
sys_exit(void)
{
  exit();
  return 0;  // not reached
}

int
sys_wait(void)
{
  return wait();
}

int
sys_kill(void)
{
  int pid;

  if(argint(0, &pid) < 0)
    return -1;
  return kill(pid);
}

int
sys_getpid(void)
{
  return myproc()->pid;
}

int
sys_sbrk(void)
{
  int addr;
  int n;

  if(argint(0, &n) < 0)
    return -1;
  addr = myproc()->sz;
  if(growproc(n) < 0)
    return -1;
  return addr;
}

int
sys_sleep(void)
{
  int n;
  uint ticks0;

  if(argint(0, &n) < 0)
    return -1;
  acquire(&tickslock);
  ticks0 = ticks;
  while(ticks - ticks0 < n){
    if(myproc()->killed){
      release(&tickslock);
      return -1;
    }
    sleep(&ticks, &tickslock);
  }
  release(&tickslock);
  return 0;
}

// return how many clock tick interrupts have occurred
// since start.
int
sys_uptime(void)
{
  uint xticks;

  acquire(&tickslock);
  xticks = ticks;
  release(&tickslock);
  return xticks;
}

int
sys_getNumProc(void)
{
	return getNumProcAssist();
}

int 
sys_getMaxPID(void)
{
	return getMaxPIDAssist();
}

int
sys_getProcInfo(void){
	int pid; //process id

	struct processInfo *info;
	// argptr to pass a pointer-to-struct to my system call
	argptr(0,(void *)&pid, sizeof(pid));
	argptr(1,(void *)&info, sizeof(info));

	struct processInfo temporaryInfo = getProcInfoAssist(pid);
	
	if(temporaryInfo.ppid == -1)
		return -1;

	info->ppid = temporaryInfo.ppid;
	info->psize = temporaryInfo.psize;
        info->numberContextSwitches = temporaryInfo.numberContextSwitches;
	return 0;
}

int
sys_set_burst_time(void)
{
  int burst_time;	//additional attribute burst_time
  argptr(0,(void *)&burst_time, sizeof(burst_time)); 

  return set_burst_timeAssist(burst_time);
}

int
sys_get_burst_time(void)
{
  return get_burst_timeAssist();
}

int
sys_getCurrentInfo(void)
{
  struct processInfo *info;
  argptr(0,(void *)&info, sizeof(info));

  struct processInfo temporaryInfo = getCurrentInfoAssist();

  if(temporaryInfo.ppid == -1)return -1;

  info->ppid = temporaryInfo.ppid;
  info->psize = temporaryInfo.psize;
  info->numberContextSwitches = temporaryInfo.numberContextSwitches;
  return 0;
}

int sys_getCurrentPID(void){
  return getCurrentPIDAssist();
}
