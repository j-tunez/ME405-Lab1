
import pyb

class Motordriver:
    """!
    This class implements a motor driver for an ME405 kit.  
    """
    def __init__(self, enab_pin, in1pin, in2pin, timer):
        """!
        Creates a motor driver by initializing GPIO
        pins and turning off the motor for safety. 
        @param enab_pin (There will be several pin parameters)
        
        """
        #self.enab_pin = enab_pin
        #self.in1pin = in1pin
        #self.in2pin = in2pin
        self.timer = timer

        self.enab_pin = pyb.Pin(enab_pin, Pin.OUT_OD, pull = Pin.PULL_UP)
        self.in1pin = pyb.Pin(in1pin, pyb.Pin.OUT_PP)
        self.in2pin = pyb.Pin(in2pin, pyb.Pin.OUT_PP)

        tim3 = pyb.Timer (3, freq=20000)
        self.t3ch1 = tim3.channel (1, pyb.Timer.PWM, pin=self.in1pin)
        self.t3ch2 = tim3.channel (2, pyb.Timer.PWM, pin=self.in2pin)

    def set_duty_cycle (self, level):
        """!
        This method sets the duty cycle to be sent
        to the motor to the given level. Positive values
        cause torque in one direction, negative values
        in the opposite direction.
        @param level A signed integer holding the duty
               cycle of the voltage sent to the motor 
        """
        if level > 0 and self.enab_pin == True:
            self.t3ch1.pulsewidthpercent(0)
            self.t3ch2.pulsewidthpercent(level)
       
        elif level < 0 and self.enab_pin == True:
            self.t3ch1.pulsewidthpercent(level)
            self.t3ch2.pulsewidthpercent(0)
        
        else:
            self.t3ch1.pulsewidthpercent(0)
            self.t3ch2.pulsewidthpercent(0)
        print (f"Setting duty cycle to {level}")