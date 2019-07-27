from time import sleep

import RPi.GPIO as GPIO


class Vibrator:
    def __init__(self):
        self.pinMotorA = 7
        self.pinMotorB = 8

        GPIO.setwarnings(False)
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(self.pinMotorA, GPIO.OUT, initial=GPIO.LOW)
        GPIO.setup(self.pinMotorB, GPIO.OUT, initial=GPIO.LOW)

    def vibrate(self):
        print("vibrate")
        GPIO.output(self.pinMotorA, GPIO.HIGH)
        sleep(0.1)
        GPIO.output(self.pinMotorA, GPIO.LOW)
        GPIO.output(self.pinMotorB, GPIO.HIGH)
        sleep(0.1)
        GPIO.output(self.pinMotorB, GPIO.LOW)
