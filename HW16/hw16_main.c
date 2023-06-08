#include "nu32dip.h"
#include "uart2.h"
#include "motor.h"

int main(void) {
    NU32DIP_Startup();
    init_motor();
    UART2_Startup();
    
    float e_intg = 0;
    float dt = 0.1;
    
    while (1) {
        int com = 30;
        
        if(get_uart2_flag()){
            set_uart2_flag(0); // set the flag to 0 to be ready for the next message
            com = get_uart2_value();
            char line_center[100];
            sprintf(line_center,"%d\n\n\n\r",com);
            NU32DIP_WriteUART1(line_center);
        }
        
        float e = com - SETPOINT;
        e_intg = e_intg + dt * e;
        
		if (com > 25 && com < 35) {
            e = 0; // go straight (ignoring I part of controller)
        }

        set_pwm_dir(e, e_intg);  
        
        // _CP0_SET_COUNT(0);
        // while(_CP0_GET_COUNT()< 2 * 24000000){}
    } 
}
        