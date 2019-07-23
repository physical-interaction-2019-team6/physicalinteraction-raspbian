from time import sleep

import RPi.GPIO as GPIO


def main():
    print("LED blink")

    while True:  # Run forever
        GPIO.output(8, GPIO.HIGH)  # Turn on
        print("HIGH")
        sleep(1)  # Sleep for 1 second
        GPIO.output(8, GPIO.LOW)  # Turn off
        print("LOW")
        sleep(1)  # Sleep for 1 second


if __name__ == "__main__":
    main()
