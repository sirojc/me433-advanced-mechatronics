#include "nu32dip.h"
#include "ws2812b.h"

#define LEDY NU32DIP_YELLOW

int main(void) {
    NU32DIP_Startup();
    ws2812b_setup();
    
    int numLEDs = 8;
    int cycles = 0;
    
    while(1){
        LEDY = !LEDY;
        int hue = 360/numLEDs * cycles; // change to make each LED a different color
        // wsColor c = HSBtoRGB(hue, 0, 1); // full color wheel, full brightness
        wsColor c = {255, 255, 255};
        ws2812b_setColor(&c, numLEDs);
        if(cycles < 7){
            cycles++;
        }
        else{
            cycles = 0;
        }
        _CP0_SET_COUNT(0);
        while(_CP0_GET_COUNT() < 24000 * 500){};
    }
    
    

}

