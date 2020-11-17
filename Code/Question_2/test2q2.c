#include <stdio.h>
#include <time.h>
#include <stdlib.h>

#define size 10

/* FUNCTION DECLARATIONS */
void heap(void);
void stack(void);
void static_s(void);
/* FUNCTIONS */
void heap(void){ int*z = (int*) malloc(100000*sizeof(int)); free(ptr);}
void stack(void){ int y[size]; }
void static_s(void) { static int x[size]; }
free(ptr);
/* DRIVER METHOD */
int main() {
    struct timespec t_1, t_2;
    int i;

    /* HEAP */
    clock_gettime(CLOCK_REALTIME, &t_1);
    for( i=0; i<100000; i++){
        heap();
    }
    clock_gettime(CLOCK_REALTIME, &t_2);
    printf("Heap: %ld \n", (t_2.tv_nsec - t_1.tv_nsec));

    /* STACK */
    clock_gettime(CLOCK_REALTIME, &t_1);
    for( i=0; i<100000; i++ ){
        stack();
    }
    clock_gettime(CLOCK_REALTIME, &t_2);
    printf("Stack: %ld \n", (t_2.tv_nsec - t_1.tv_nsec));
    
    /* STATIC */
    clock_gettime(CLOCK_REALTIME, &t_1);
    for ( i=0; i< 100000; i++ ) {
        static_s();
    }
    clock_gettime(CLOCK_REALTIME, &t_2);
    printf("Static: %ld \n", (t_2.tv_nsec - t_1.tv_nsec));
    return 0;
}
