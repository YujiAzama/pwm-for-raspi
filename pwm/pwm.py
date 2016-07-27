import time

#from RPi import GPIO


class PWM(object):

    def __init__(self, pin):
        self.pin = pin
#        GPIO.setmode(GPIO.BCM)
#        GPIO.setup(pin, GPIO.OUT)

    def start(self, duty=50.0, freq=1000.0):
        while True:
#            GPIO.output(self.pin, 1)
            print "----+"
            print "    |"
            time.sleep(duty / freq / 100)

#            GPIO.output(self.pin, 0)
            print "+---+"
            print "|"
            time.sleep((100 - duty) / freq / 100)


if __name__ == "__main__":
    pwm = PWM(1)
    pwm.start(duty=50.0)
