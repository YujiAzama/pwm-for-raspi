from multiprocessing import Process
from time import sleep


PIN_RED = 3
PIN_GREEN = 4
PIN_BLUE = 5


class PWM(object):

    def __init__(self, pin, duty=50, freq=1000):
        self.pin = pin
        self.duty = duty
        self.freq = freq
        self.process = Process(target=self.__loop, args=(duty, freq))

    def start(self):
        self.process.start()

    def stop(self):
        self.process.terminate()

    def restart(self):
        self.stop()
        self.process = Process(target=self.__loop, args=(self.duty, self.freq))
        self.start()

    def update_duty(self, duty):
        self.duty = duty
        if self.process.pid:
            self.restart()

    def __set_high(self):
        print "HIGH!", self.pin

    def __set_low(self):
        print "LOW!", self.pin

    def __loop(self, duty, freq):
        while True:
            self.__set_high()
            sleep(self.duty / self.freq / 100.0)

            self.__set_low()
            sleep((100.0 - self.duty) / self.freq / 100.0)

    def cleanup():
        self.set_low()


class LED(object):

    def __init__(self, pwm=PWM(1 ,80, 1)):
        self.pwm = pwm

    def on(self):
        self.pwm.start()

    def off(self):
        self.pwm.stop()

    def terminate():
        self.off()
        self.pwm.cleanup()


class FullColorLED(object):

    def __init__(self, red= 0, green=255, blue=255, color_code=None, freq=1000):
        self.led_red = LED(PWM("red", red*100/255, freq))
        self.led_green = LED(PWM("green", green*100/255, freq))
        self.led_blue = LED(PWM("blue", blue*100/255, freq))

    def on(self):
        self.led_red.on()
        self.led_green.on()
        self.led_blue.on()

    def off(self):
        self.led_red.off()
        self.led_green.off()
        self.led_blue.off()

    def terminate(self):
        self.led_red.terminate()
        self.led_green.terminate()
        self.led_blue.terminate()


if __name__ == '__main__':

    try:
        fcl = FullColorLED(255, 255, 255)
        fcl.on()
        sleep(3)
        fcl.off()
    except KeyboardInterrupt:
        fcl.terminate()

#    pwm = PWM(1, 70, 10)
#    pwm.update_duty(50)
#
#    try:
#        led = LED(pwm=pwm)
#        led.on()
#        sleep(2)
#        pwm.update_duty(80)
#        sleep(5)
#        led.off()
#
#    except KeyboardInterrupt:
#        led.terminate()
