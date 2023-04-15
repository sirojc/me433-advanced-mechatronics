#include "spi.h"
#include <math.h>

void send_msg(int V, char Ch);

int main(void) {
  initSPI();
  
  int sine[400];
  int triangle[400];
  
  int time_ms = 24;
  
  for(int t = 0; t < 400; t++){
      sine[t] = 1023/2*(sin(2*M_PI*t/200)+1);
      if(t<200){
          triangle[t] = 1023*t/200;
      }
      else{
          triangle[t] = 1023/200 * (400-t);
      }   
  }
  
  while (1) {
      for(int t = 0; t<400; t++){
          _CP0_SET_COUNT(0);
          send_msg(sine[t], 0); // 0 = Channel A
          send_msg(triangle[t], 1); // 1 = Channel B
          
          // Delay to produce 2Hz sine wave and 1 Hz triangle wave
          while(_CP0_GET_COUNT() < 60000){}
      }

  }
}

void send_msg(int V, char Ch){
      unsigned char msg = 0b0;
      // [a_or_b 1 1 1 --10bits-- 0 0]
      unsigned short t = (Ch << 15) | (0b111 <<12) | (V <<2);
      
      unsigned char first8 = (t >> 8) & 0xFF;
      unsigned char last8 = t & 0xFF;
      
      LATBbits.LATB7 = 0;
      spi_io(first8);
      spi_io(last8);
      LATBbits.LATB7 = 1;
}