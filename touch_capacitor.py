from adafruit_circuitplayground.express import cpx
import touchio
from time import sleep
from board import *

touch = touchio.TouchIn(A1)

while True:
    if cpx.button_a:
        print(cpx.temperature)
    if cpx.button_b:
        print(cpx.light)
    print(touch.raw_value)
    sleep(5)
