#include "nu32dip.h"

// Motor direction pins
#define MOTOR_RIGHT_DIRECTION LATBbits.LATB8 // Forward 0; Backward 1
#define MOTOR_LEFT_DIRECTION LATBbits.LATB9 // Forward 0; Backward 1

// Motor PWM
#define MOTOR_RIGHT_SPEED OC1RS
#define MOTOR_LEFT_SPEED OC2RS

// Timer 3
#define PR3_PERIOD 2400

// P Controller parameters
#define SETPOINT 30 // setpoint COM in middle of image
#define Kp 0.6
#define PWM_MAX 50 // max speed of wheel: 80% duty cycle
#define PWM_MIN 20 // min speed of wheel: 20% dc
// #define PWM_0 30 // base speed of wheel: 30% dc

void init_motor();

void set_pwm_dir(int e);