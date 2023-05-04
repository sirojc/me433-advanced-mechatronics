#include "nu32dip.h"
#include "ws2812b.h"

#define LEDY NU32DIP_YELLOW

int main(void) {
    NU32DIP_Startup();
    ws2812b_setup();
    
    int numLEDs = 8;
    
    int hue = 0;
    int step = 10;
    
    wsColor c[numLEDs];
    
    while(1){
        LEDY = !LEDY;
        
        /*for(int i = 0; i < numLEDs; i++){
            int hue = (hue0 + step*i)%360;
            wsColor s = HSBtoRGB(hue, 1, 1);
            c[i] = s;
        }*/
        for(int i = 0; i< numLEDs; i++){
            c[i] = HSBtoRGB(hue + 20*i, 1, 1);
        }
        ws2812b_setColor(&c, numLEDs);

        if(hue >= 360){
            hue = 0;
        }
        else{
            hue += step;
        }
        
        _CP0_SET_COUNT(0);
        while(_CP0_GET_COUNT() < 24000 * 50){};
    }
}




        /*for(int n = 0; n < amt; n++){
            for(int i = 0; i < numLEDs; i++){
                int inc = (i+n) % (numLEDs-1);
                int hue = angle * inc;
                wsColor s = HSBtoRGB(hue, 1, 0.4); // full color wheel, full brightness
                c[i] = s;
            } 
            ws2812b_setColor(&c, numLEDs);
            _CP0_SET_COUNT(0);
            while(_CP0_GET_COUNT() < 24000 * 100){};
        }*/
