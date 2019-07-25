from time import sleep

import RPi.GPIO as GPIO


def main():
    motorA = 7  # Pin number,motorA
    motorB = 8  # Pin number,motorB
    emo_my = 0  # My emotion,not happy=0,happy=1
    emo_ano = 0  # Another people emotion,not happy=0,happy=1
    print("Motor")
    GPIO.setwarnings(False)  # Ignore warning for now
    GPIO.setmode(GPIO.BOARD)  # Use physical pin numbering
    GPIO.setup(motorA, GPIO.OUT, initial=GPIO.LOW)  # Set pin 7 to be an output pin and set initial value to low (off)
    GPIO.setup(motorB, GPIO.OUT, initial=GPIO.LOW)  # Set pin 8 to be an output pin and set initial value to low
    while True:
        if emo_my == emo_ano and 1 == emo_my:
            GPIO.output(motorA, GPIO.HIGH)  # Turn on
            print("MotorA HIGH")
            sleep(1)  # Sleep for 1 second
            GPIO.output(motorA, GPIO.LOW)  # Turn off
            print("MotorA LOW")
            sleep(0.5)  # Sleep for 0.5 second
            GPIO.output(motorB, GPIO.HIGH)  # Turn on
            print("MotorB HIGH")
            sleep(1)  # Sleep for 1 second
            GPIO.output(motorB, GPIO.LOW)  # Turn off
            print("MotorB LOW")
            sleep(1)  # Sleep for 1 second


if __name__ == "__main__":
    main()
