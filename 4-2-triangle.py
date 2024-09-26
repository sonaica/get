import RPi.GPIO as GPIO
import time
import sys
GPIO.setmode(GPIO.BCM)

dac = [8, 11, 7, 1, 0, 5, 12, 6]

GPIO.setup(dac, GPIO.OUT)

def dec2bin(n):
    return [int(elem) for elem in bin(n)[2:].zfill(8)]

try:
    while True:
        print('input number')
        n = input()
        if n == 'q': sys.exit()
        if n.isdigit():
            t = int(n)/256/2
            for i in range(0, 256):
                GPIO.output(dac, dec2bin(i))
                time.sleep(t)
            for i in range(255, -1, -1):
                GPIO.output(dac, dec2bin(i))
                time.sleep(t)
finally:
    GPIO.output(dac, 0)
    GPIO.cleanup()
    print('program finished')