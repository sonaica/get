import RPi.GPIO as GPIO
import sys
GPIO.setmode(GPIO.BCM)

dac = [8, 11, 7, 1, 0, 5, 12, 6]

GPIO.setup(dac, GPIO.OUT)

def dec2bin(n):
    return [int(elem) for elem in bin(n)[2:].zfill(8)]

try:
    while True:
        print('input number 0-255')
        value = input()
        if value == 'q': sys.exit()
        if value.isdigit() and int(value)%1 ==0 and 0 <= int(value) <= 255:
            GPIO.output(dac, dec2bin(int(value)))
            v = 5.0 / 256 * int(value)
            print(v)
        elif not value.isdigit():
            print('input number 0-255')

except ValueError:
    print('input number 0-255')
except KeyboardInterrupt:
    print('done')
finally:
    GPIO.output(dac, 0)
    GPIO.cleanup()
    print('program finished')
