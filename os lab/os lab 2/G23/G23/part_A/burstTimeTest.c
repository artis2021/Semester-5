#include "types.h"
#include "stat.h"
#include "user.h"

int
main(void){
	//int a=3;
	printf(1,"Setting burst time value = 3 \n");

	set_burst_time(3);
	printf(1, "The burst time is: %d \n", get_burst_time());
	exit();
}
