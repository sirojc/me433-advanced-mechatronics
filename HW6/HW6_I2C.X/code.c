#include "i2c_master_noint.h"
#include "nu32dip.h"

void write_GP7(unsigned char state);
int read_GP0();

int main(void) {
    NU32DIP_Startup();
   
    // init chip, GP0 input, GP7 output
    i2c_master_setup();
    ANSELB = 0;
    unsigned char IODIR = 0b01111111;
    i2c_master_start();
    i2c_master_send(0b01000000);
    i2c_master_send(0x00);
    i2c_master_send(IODIR);
    i2c_master_stop();
     
    while(1){
        //blink yellow LED
        NU32DIP_YELLOW = 1;
        _CP0_SET_COUNT(0);
        while(_CP0_GET_COUNT() < 12000*500){}
        NU32DIP_YELLOW = 0;
        _CP0_SET_COUNT(0);
        while(_CP0_GET_COUNT() < 12000*500){}
        
        int r = read_GP0();
        if(r==0){
            write_GP7(1);
        }
        else{
            write_GP7(0);
        }
        
        
        /*
        write_GP7(1);
        _CP0_SET_COUNT(0);
        while(_CP0_GET_COUNT() < 12000*500){}
        write_GP7(0);
        _CP0_SET_COUNT(0);
        while(_CP0_GET_COUNT() < 12000*500){}
        */
    }
}

void write_GP7(unsigned char state){
    i2c_master_start();
    
    i2c_master_send(0b01000000);
    i2c_master_send(0x0A);
    
    if(state == 1){
        i2c_master_send(0b10000000);
    }
    else{
        i2c_master_send(0b00000000);
    }
    i2c_master_stop();
}

int read_GP0(){
    i2c_master_start();
    
    i2c_master_send(0b01000000);
    i2c_master_send(0x09);
    
    i2c_master_restart();
    i2c_master_send(0b01000000 |1);
    unsigned char r = i2c_master_recv();
 
    i2c_master_ack(1);
    i2c_master_stop();
    
    return (r&0b00000001);
}