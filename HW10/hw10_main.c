#include "nu32dip.h"
#include "ws2812b.h"

#define LEDY NU32DIP_YELLOW

int main(void) {
    NU32DIP_Startup();
    ws2812b_setup();
    
    int numLEDs = 8;
    int cycles = 0;
    int amt = 6;
    int angle = 360/amt;
    
    while(1){
        LEDY = !LEDY;
        int hue = angle * cycles;
        wsColor c = HSBtoRGB(hue, 1, 1); // full color wheel, full brightness
        //wsColor c = {255, 0, 0};
        ws2812b_setColor(&c, numLEDs);
        if(cycles < amt){
            cycles++;
        }
        else{
            cycles = 0;
        }
        _CP0_SET_COUNT(0);
        while(_CP0_GET_COUNT() < 24000 * 500){};
    }
    
    

}

