#include "nu32dip.h"
#include "uart2.h"
#include "motor.h"

int main(void) {
    NU32DIP_Startup();
    //init_motor();
    UART2_Startup();
    
    while (1) {
        int com = 0;
        /*
        if(get_uart2_flag()){
            set_uart2_flag(0); // set the flag to 0 to be ready for the next message
            com = get_uart2_value();
            char line_center[100];
            sprintf(line_center,"%d\n\n\n\r",com);
            NU32DIP_WriteUART1(line_center);
        */
        
        int e = com - SETPOINT;
        //set_pwm_dir(e);  
        
        // _CP0_SET_COUNT(0);
        // while(_CP0_GET_COUNT()< 2 * 24000000){}
        
    } 
}
        