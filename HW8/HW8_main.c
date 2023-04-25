#include "nu32dip.h"
#include "mpu6050.h"
#include <stdio.h>
#include "font.h"
#include "ssd1306.h"

#define LEDY NU32DIP_YELLOW

void drawChar(unsigned char sign, unsigned char x, unsigned char y);
void drawString(unsigned char* string, unsigned char x, unsigned char y);

int main(void) {
    NU32DIP_Startup();
    init_mpu6050();
    ssd1306_setup();
	
    char m_in[100];
	// char array for the raw data
    unsigned char r[14];
	// floats to store the data
    float az;

    while (1) {
        LEDY = !LEDY;

        _CP0_SET_COUNT(0);
        // read IMU
        burst_read_mpu6050(r);
        // convert data
        az = conv_zXL(r);
        // 1. blink only one pixel (check it works, delete afterwards)
        /*
        ssd1306_drawPixel(0, 0, 1);
        ssd1306_update();
        while(_CP0_GET_COUNT() < 24000 * 500){}
        ssd1306_drawPixel(0, 0, 0);
        ssd1306_update();
        _CP0_SET_COUNT(0);
         */
        // 2. function for one letter (in font.h)
        // 3. function for one word (in font.h)
        sprintf(m_in, "az = %f", az);
        ssd1306_clear();
        drawString(m_in, 0, 10);
        
        
        int fps = 24000000/_CP0_GET_COUNT();
        sprintf(m_in, "fps=%i", fps);
        drawString(m_in, 0, 25);
        ssd1306_update();
        //while(_CP0_GET_COUNT() < 24000 * 100){}
    }
}

void drawChar(unsigned char sign, unsigned char x, unsigned char y){
    for(int i = 0; i<5; i++){
        unsigned char col = ASCII[sign - 0x20][i];
        for(int j = 0; j<8; j++){
            ssd1306_drawPixel(x+i, y+j, (col>>j)&0b1);
        }
    }
}
void drawString(unsigned char* string, unsigned char x, unsigned char y){
    
    int i = 0;
    while(string[i] != 0){
        drawChar(string[i], x + 5*i, y); //x = column, y = row
        i++;
    }
    
    
}
