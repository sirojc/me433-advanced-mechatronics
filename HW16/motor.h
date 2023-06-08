#include "nu32dip.h"

// Motor direction pins
#define MOTOR_RIGHT_DIRECTION LATBbits.LATB8 // Forward 0; Backward 1
#define MOTOR_LEFT_DIRECTION LATBbits.LATB9 // Forward 0; Backward 1

// Motor PWM
#define MOTOR_RIGHT_SPEED OC2RS
#define MOTOR_LEFT_SPEED OC1RS

// Timer 3
#define PR3_PERIOD 2400

// P Controller parameters
#define SETPOINT 30 // setpoint COM in middle of image
#define Kp 0.03
#define Ki 0.05
#define PWM_MAX 33 // max speed of wheel
#define PWM_MIN 27 // min speed of wheel
#define PWM_0 30 // base speed of wheel

void init_motor();

void set_pwm_dir(float e, float e_intg);