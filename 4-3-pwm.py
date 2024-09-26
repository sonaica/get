import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)

GPIO.setup(27, GPIO.OUT)

pwm = GPIO.PWM(27, 1000)
pwm.start(0)

try:
    while True:
        print('input duty cycle %:')
        duty = input()
        if duty.isdigit():
            pwm.ChangeDutyCycle(int(duty))
        print(3.3/100*int(duty))
finally:
    GPIO.output(27, 0)
    GPIO.cleanup()
    print('program finished')

