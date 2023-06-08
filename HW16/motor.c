#include "motor.h"
#include "nu32dip.h"

void init_motor(){
    // Select B8 and B9 pins for motor phase pins
    TRISBbits.TRISB8 = 0;  //set B8 to output
    TRISBbits.TRISB9 = 0;  //set B9 to output
    MOTOR_RIGHT_DIRECTION = 0; // Forward 0; Backward 1
    MOTOR_LEFT_DIRECTION = 0; // Forward 0; Backward 1

    // 20kHz Timer for PWM
    T3CONbits.TCKPS = 0b001;      // Timer3 prescaler 0b001
    PR3 = PR3_PERIOD - 1;         // Period
    TMR3 = 0;                     // initial TMR3 count is 0
    
    // Assign OC1 to B7 -> Motor Left PWM
    RPB7Rbits.RPB7R = 0b0101;
    OC1CONbits.OCM = 0b110;       // PWM mode without fault pin; other OC1CON bits are defaults
    MOTOR_LEFT_SPEED = 800;     // duty cycle = MOTOR_RIGHT_SPEED/(PR3+1) = 50%
    OC1R = 1000;                  // initialize before turning OC1 on; afterward it is read-only
    OC1CONbits.OCTSEL = 1;        // Use Timer 3
    // Assign OC2 to B11 -> Motor Right PWM
    RPB11Rbits.RPB11R = 0b0101;
    OC2CONbits.OCM = 0b110;       // PWM mode without fault pin; other OC2CON bits are defaults
    MOTOR_RIGHT_SPEED = 800;      // duty cycle = MOTOR_LEFT_SPEED/(PR3+1) = 50%
    OC2R = 1000;                  // initialize before turning OC2 on; afterward it is read-only
    OC2CONbits.OCTSEL = 1;        // Use Timer 3
    
    T3CONbits.ON = 1;             // turn on Timer3
    OC1CONbits.ON = 1;            // turn on OC1
    OC2CONbits.ON = 1;            // turn on OC2
}

void set_pwm_dir(float e, float e_intg){
    MOTOR_LEFT_DIRECTION = 0;
    MOTOR_RIGHT_DIRECTION = 0;
    
    int pwm_L = e * Kp + Ki * e_intg + PWM_0;
    int pwm_R = -e * Kp - Ki * e_intg + PWM_0;
    
    if (pwm_L >= PWM_MAX){
        MOTOR_RIGHT_SPEED = (int)(PR3_PERIOD*(float)PWM_MAX/100);
    }
    else if (pwm_L <= PWM_MIN){
        MOTOR_RIGHT_DIRECTION = 1;
        MOTOR_RIGHT_SPEED = (int)(PR3_PERIOD*(float)PWM_MIN/100);
    }
    else {
        MOTOR_RIGHT_SPEED = (int)(PR3_PERIOD*(float)pwm_L/100);
    }

    if (pwm_R >= PWM_MAX){
        MOTOR_LEFT_SPEED = (int)(PR3_PERIOD*(float)PWM_MAX/100);
    }
    else if (pwm_R <= PWM_MIN){
        MOTOR_LEFT_DIRECTION = 1;
        MOTOR_LEFT_SPEED = (int)(PR3_PERIOD*(float)PWM_MIN/100);
    }
    else {
        MOTOR_LEFT_SPEED = (int)(PR3_PERIOD*(float)pwm_R/100);
    }   
}