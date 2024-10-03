import RPi.GPIO as gpio
import time
gpio.setmode(gpio.BCM)

dac = [8, 11, 7, 1, 0, 5, 12, 6]
comp = 14
troyka = 13

gpio.setup(dac, gpio.OUT)
gpio.setup(troyka, gpio.OUT, initial=gpio.HIGH)
gpio.setup(comp, gpio.IN)

def dec2bin(n):
    return [int(elem) for elem in bin(n)[2:].zfill(8)]

def adc():
    for i in range(0, 256):
        d = dec2bin(i)
        gpio.output(dac, d)
        time.sleep(0.1)
        c = gpio.input(comp)
        if c == 1:
            return i

try:
    while True:
        v = adc()
        print(v, 3.3*v/256)

finally:
    gpio.output(dac, 0)
    gpio.cleanup()
