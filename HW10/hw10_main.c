#include "nu32dip.h"
#include "ws2812b.h"

int main(void) {
    NU32DIP_Startup();
    ws2812b_setup();
    
    
    int numLEDs = 8;
    int i = 0;
    while(1){
        int hue = 360/numLEDs * i;
        wsColor c = HSBtoRGB(hue, 1, 1); // full color wheel, full brightness
        ws2812b_setColor(&c, numLEDs);
        i++;
    }
    
    

}

