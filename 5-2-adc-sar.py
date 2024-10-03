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

def bin2dec(n):
    d = 0
    p = 1
    for i in range(7, -1, -1):
        d += p * n[i]
        p *= 2
    return d

def adc():
    d = [0]*8
    for i in range(0, 8):
        d[i] = 1
        gpio.output(dac, d)
        time.sleep(0.1)
        c = gpio.input(comp)
        if c == 1:
            d[i] = 0
    return bin2dec(d)

try:
    while True:
        v = adc()
        print(v, 3.3*v/256)

finally:
    gpio.output(dac, 0)
    gpio.cleanup()
