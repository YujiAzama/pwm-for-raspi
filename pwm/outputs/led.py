from RPi import GPIO


class LED(object):

    def __init__(self, pin):
        self.pin = pin
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(pin, GPIO.OUT)

    def turn_on(self):
        GPIO.output(self.pin, 1)

    def turn_off(self):
        GPIO.output(self.pin, 0)
