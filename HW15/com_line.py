# requires adafruit_ov7670.mpy and adafruit_st7735r.mpy in the lib folder
import time
from displayio import (
    Bitmap,
    Group,
    TileGrid,
    FourWire,
    release_displays,
    ColorConverter,
    Colorspace,
)
from adafruit_st7735r import ST7735R
import board
import busio
import digitalio
from adafruit_ov7670 import (
    OV7670,
    OV7670_SIZE_DIV1,
    OV7670_SIZE_DIV8,
    OV7670_SIZE_DIV16,
)

from ulab import numpy as np

# in your init area
uart = busio.UART(board.GP4, board.GP5, baudrate=9600) #tx pin, rx pin

release_displays()
spi = busio.SPI(clock=board.GP2, MOSI=board.GP3)
display_bus = FourWire(spi, command=board.GP0, chip_select=board.GP1, reset=None)
display = ST7735R(display_bus, width=160, height=128, rotation=90)


# Ensure the camera is shut down, so that it releases the SDA/SCL lines,
# then create the configuration I2C bus

with digitalio.DigitalInOut(board.GP10) as reset:
    reset.switch_to_output(False)
    time.sleep(0.001)
    bus = busio.I2C(board.GP9, board.GP8) #GP9 is SCL, GP8 is SDA

# Set up the camera (you must customize this for your board!)
cam = OV7670(
    bus,
    data_pins=[
        board.GP12,
        board.GP13,
        board.GP14,
        board.GP15,
        board.GP16,
        board.GP17,
        board.GP18,
        board.GP19,
    ],  # [16]     [org] etc
    clock=board.GP11,  # [15]     [blk]
    vsync=board.GP7,  # [10]     [brn]
    href=board.GP21,  # [27/o14] [red]
    mclk=board.GP20,  # [16/o15]
    shutdown=None,
    reset=board.GP10,
)  # [14]

width = display.width
height = display.height

bitmap = None
# Select the biggest size for which we can allocate a bitmap successfully, and
# which is not bigger than the display
for size in range(OV7670_SIZE_DIV1, OV7670_SIZE_DIV16 + 1):
    #cam.size = size # for 4Hz
    #cam.size = OV7670_SIZE_DIV16 # for 30x40, 9Hz
    cam.size = OV7670_SIZE_DIV8 # for 60x80, 9Hz
    if cam.width > width:
        continue
    if cam.height > height:
        continue
    try:
        bitmap = Bitmap(cam.width, cam.height, 65536)
        break
    except MemoryError:
        continue

print(width, height, cam.width, cam.height)
if bitmap is None:
    raise SystemExit("Could not allocate a bitmap")
time.sleep(4)
g = Group(scale=1, x=(width - cam.width) // 2, y=(height - cam.height) // 2)
tg = TileGrid(
    bitmap, pixel_shader=ColorConverter(input_colorspace=Colorspace.BGR565_SWAPPED)
)
g.append(tg)
display.show(g)

t0 = time.monotonic_ns()
display.auto_refresh = False

# arrays for color / brightness data
reds = np.zeros(60,dtype=np.uint16)
greens = np.zeros(60,dtype=np.uint16)
blues = np.zeros(60,dtype=np.uint16)
bright = np.zeros(60)

while True:
    cam.capture(bitmap)

    ### Find com of line ###
    # Get single colors of bitmap row
    row = 40
    for i in range(1,10): # rectangle in middle of image, rows above
        bitmap[row+i,30] = 0x3F<<5
        bitmap[row+i,29] = 0x3F<<5
        bitmap[row+i,31] = 0x3F<<5

    for i in range(0,60):
        reds[i] = ((bitmap[row,i]>>5)&0x3F)/0x3F*100
        greens[i] = ((bitmap[row,i])&0x1F)/0x1F*100
        blues[i] = (bitmap[row,i]>>11)/0x1F*100
        bright[i] = (reds[i]+greens[i]+blues[i])/3.0

    avg_b = 0
    for i in range(0,60):
        avg_b += bright[i]/60.0

    sum_color = 0
    sum_idx = 0
    for i in range(0,60):
            if(bright[i] > avg_b):
                bitmap[row,i] = 0xFFFF
                sum_idx += i
                sum_color += 1
            else:
                bitmap[row,i] = 0x0000

    COM = 30 # middle of image
    if sum_color !=0 and sum_idx !=0:
        COM = sum_idx/sum_color

    for i in range(1,10): # rectangle at detected COM, rows below
        bitmap[row-i,int(COM)] = 0xE65B
        if(COM >= 1):
            bitmap[row-i,int(COM)-1] = 0xE65B
        if(COM <= 59):
            bitmap[row-i,int(COM)+1] = 0xE65B

    print(f"COM = {COM}")
    # in while True: after reading an image and finding the line
    value_str = str(COM)+'\n'
    uart.write(value_str.encode())

    # update display
    bitmap.dirty()
    display.refresh(minimum_frames_per_second=0)
    t1 = time.monotonic_ns()
    #print("fps", 1e9 / (t1 - t0))
    t0 = t1
