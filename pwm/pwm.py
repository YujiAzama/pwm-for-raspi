import time

from RPi import GPIO


class PWM(object):

    def __init__(self, pin):
        self.pin = pin
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(pin, GPIO.OUT)

    def start(self, duty=50.0, freq=1000.0):
        while True:
            GPIO.output(self.pin, GPIO.HIGH)
            time.sleep(duty / freq / 100.0)

            GPIO.output(self.pin, GPIO.LOW)
            time.sleep((100.0 - duty) / freq / 100.0)


if __name__ == "__main__":
    pwm = PWM(pin=1)
    pwm.start(duty=50.0)
