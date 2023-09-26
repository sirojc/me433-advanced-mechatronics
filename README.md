# ME433_Joris
*ME433 Advanced Mechatronics* repository of Joris Chomarat

Spring 2023 @ Northwestern University

This repository contains the code deliverables for all assignments, to be found [here](https://github.com/ndm736/ME433_2023/wiki/Schedule). 

### Assignments
#### [HW2](HW2/) - 3.3V regulator, PIC32
[Assignment 2](https://github.com/ndm736/ME433_2023/wiki/HW2)
- Built a 3.3V regulator, to be able to power the PIC32 microchip and other sensors at 3.3V. Power comes from 5V (USB) or 6V (Battery Pack). A switch enables to change powering method, shown on the PCB in [HW4](/HW4).
- Connected the PIC32 microchip and LEDs to the circuit and wrote a loop to blink 2 LEDs in a certain frequency.

<img src="https://github.com/sirojc/me433-advanced-mechatronics/blob/main/HW2/IMG_2842.jpeg" height="300">

#### [HW3](HW3/HW3_send_sin.X) - USB to UART
[Assignment 3](https://github.com/ndm736/ME433_2023/wiki/HW3)
- Wrote a loop to send a sine wave from the PIC32 to a PC over UART communication at eveery push of a button in the circuit.

#### [HW4](HW4/) - PCB Design
[Assignment 4](https://github.com/ndm736/ME433_2023/wiki/HW4)
- Designed a PCB from scratch to use in the final [robot](/HW16)
- Used the same components as for previous assignments, as well as a power switch and holes for header pins to connect further PCBs on top later.

<img src="https://github.com/sirojc/me433-advanced-mechatronics/blob/main/HW4/Schematic.png" height="400"> <img src="https://github.com/sirojc/me433-advanced-mechatronics/blob/main/HW4/Layout_Board.png" height="400">

#### [HW5](HW5/) - SPI
[Assignment 5](https://github.com/ndm736/ME433_2023/wiki/HW5)
- Used SPI to write to an MCP4912 and send a sine and triangle wave.

<img src="https://github.com/sirojc/me433-advanced-mechatronics/blob/main/HW5/IMG_3014.jpeg" height="300">

#### [HW6](HW6/HW6_I2C.X) - I2C
[Assignment 6](https://github.com/ndm736/ME433_2023/wiki/HW6)
- Used I2C to communicate with an MCP23008. Made an LED blink at the push of a button, communicated through IC2.

#### [HW7](HW7/) - IMU
[Assignment 7](https://github.com/ndm736/ME433_2023/wiki/HW7)
- Read sensor measurements from an inertial measurement unit and plotted the x acceleration using I2C and UART.

#### [HW8](HW8/) - OLED Display
[Assignment 8](https://github.com/ndm736/ME433_2023/wiki/HW8)
- Printed z acceleration measurements from the IMU in [HW7](/HW7) to an OLED display.

#### [HW9](HW9/) - DSP
[Assignment 9](https://github.com/ndm736/ME433_2023/wiki/HW9)
- Digital Signal Processing on different data recordings using moving average, IIR, FIR to filter the signals, as well as performing FFT. A couple of plots are shown, the remainder of all plots can be found [here](HW9/plots).

<img src="https://github.com/sirojc/me433-advanced-mechatronics/blob/main/HW9/plots/SigB_movavg.png" height="350"> <img src="https://github.com/sirojc/me433-advanced-mechatronics/blob/main/HW9/plots/SigB_fir.png" height="350">

#### [HW10](HW10/) - RGB LED Array
[Assignment 10](https://github.com/ndm736/ME433_2023/wiki/HW10)
- Made a WS2812B LED array display a moving rainbow.

#### [HW11](HW11/) - RPi Pico FFT
[Assignment 11](https://github.com/ndm736/ME433_2023/wiki/HW11)
- Overlayed 3 sine waves and FFT filtered them in CircuitPython on a Raspberry Pi Pico W.
- Transmitted the filtered wave via UART.

<img src="https://github.com/sirojc/me433-advanced-mechatronics/blob/main/HW11/fft_3_sin.png" height="350">

#### [HW13](HW13/) - RPi Pico Website
[Assignment 13](https://github.com/ndm736/ME433_2023/wiki/HW13)
- Hosted a website on a Raspberry Pi Pico W.
- Displayed the time elapsed between two button pushes on the website.

<img src="https://github.com/sirojc/me433-advanced-mechatronics/blob/main/HW13/Screenshot_website.png" height="350">

#### [HW14](HW14/) - Servo Motor
[Assignment 14](https://github.com/ndm736/ME433_2023/wiki/HW14)
- Used PWM to control an Rc servo motor.

#### [HW15](HW15/) - Camera Line Detection
[Assignment 15](https://github.com/ndm736/ME433_2023/wiki/HW15)
- Developed an algorithm to detect the middle of a line of changing color (map shown [here](https://github.com/ndm736/ME433_2023/wiki/HW16).
- Best results were achieved by converting the image to grayscale and estimating the middle of the line based on brightness.
- Visualized detection results from the recorded image on the OLED display from [HW8](/hw8).

#### [HW16](HW16/) - Line following robot
[Assignment 16](https://github.com/ndm736/ME433_2023/wiki/HW16)
- Assembled a robot with custom 3D-printed and lasercutted parts and made it follow a line of changing color and curvature. 
- Tuned a PI controller to improve line following capabilities.
- Robot was able to follow a straight line, even of changing color, fairly well. Turns, however, did not work well.

<img src="https://github.com/sirojc/me433-advanced-mechatronics/blob/main/robot_final.png" height="450">



### Tips
- Connect to PIC via screen (on mac) with a baudrate of ```230400```.

