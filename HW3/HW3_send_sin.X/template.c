#include "nu32dip.h" // constants, functions for startup and UART
#include <math.h>

int main(void) {
  char message[100];
  
  NU32DIP_Startup(); // cache on, interrupts on, LED/button init, UART init
  while (1) {
    if (!NU32DIP_USER){
        for(int i=0; i<=100; i++){
            sprintf(message, "%f\r\n", sin(i*2*M_PI/100));
            NU32DIP_WriteUART1(message);
            
            _CP0_SET_COUNT(0);
            while(_CP0_GET_COUNT() <24000){} // 0.01s delay
        }
        
        while(!NU32DIP_USER){} //wait until button is released
	}
  }
}
	
