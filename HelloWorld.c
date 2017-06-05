#include<stdio.h>

int main() {
	
	int result = fib(10) /* Call the Fibonacci Function with argument 10 */
	/* printf("%d \n",result);	 Print the Result of the previous Fibonacci Function Call */
	printf("Hello World\n"); /* Simply print Hello World */
	return 0;
}



int fib(int n){
  if( n == 0){ 
    return 0;
  }
  if( n == 1){ 
    return 1;
  }
  if( n > 1){ 
    return fib(n-1)+fib(n-2);
  }
  return 0;
}
