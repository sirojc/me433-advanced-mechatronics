#include "nu32dip.h"
#include "mpu6050.h"
#include <stdio.h>
#include "font.h"
#include "ssd1306.h"

void blink(int, int); // blink the LEDs function

int main(void) {
    NU32DIP_Startup();
    init_mpu6050();
    ssd1306_setup();
	
    char m_in[100];
	// char array for the raw data
    unsigned char readings[14];
	// floats to store the data
    float az;
    
	// read whoami())
	unsigned char address = whoami();
    // print whoami())
    sprintf(m_in, "0x%X", address);
    NU32DIP_WriteUART1(m_in);
    // if whoami is not 0x68, stuck in loop with LEDs on
    if(address != 0x68){
        while(1){
            blink(4, 200);
        }
    }

    while (1) {
        _CP0_SET_COUNT(0);
        blink(1, 5);
        
        /*
        // read IMU
        burst_read_mpu6050(readings);
        // convert data
        az = conv_zXL(readings);
        */
        
        // 1. blink only one pixel (check it works, delete afterwards)
        
        // 2. function for one letter (in font.h)
        // 3. function for one word (in font.h)
        
        // print z acceleration az
        
        
        int fps = 24000000/_CP0_GET_COUNT();
    }
}

// blink the LEDs
void blink(int iterations, int time_ms) {
    int i;
    unsigned int t;
    for (i = 0; i < iterations; i++) {
        NU32DIP_GREEN = 0; // on
        NU32DIP_YELLOW = 1; // off
        t = _CP0_GET_COUNT();
        while (_CP0_GET_COUNT() < t + 12000 * time_ms) {}

        NU32DIP_GREEN = 1; // off
        NU32DIP_YELLOW = 0; // on
        t = _CP0_GET_COUNT(); // should really check for overflow here
        while (_CP0_GET_COUNT() < t + 12000 * time_ms) {
        }
    }
}

