"""@package docstring
Lab 1 - Encoder
"""

import time
import motordriver


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
        self.enab_pin = enab_pin
        self.in1pin = in1pin
        self.in2pin = in2pin
        self.timer = timer

#         self.enab_pin = pyb.Pin(enab_pin, Pin.OUT_OD, pull = Pin.PULL_UP)
#         self.in1pin = pyb.Pin(in1pin, pyb.Pin.OUT_PP)
#         self.in2pin = pyb.Pin(in2pin, pyb.Pin.OUT_PP)

#         tim3 = pyb.Timer (3, freq=20000)

        self.t3ch1 = timer.channel (1, pyb.Timer.PWM, pin=in1pin)
        self.t3ch2 = timer.channel (2, pyb.Timer.PWM, pin=in2pin)

    def set_duty_cycle (self, level):
        """!
        This method sets the duty cycle to be sent
        to the motor to the given level. Positive values
        cause torque in one direction, negative values
        in the opposite direction.
        @param level A signed integer holding the duty
               cycle of the voltage sent to the motor 
        """
        self.enab_pin.high()
        
        if level > 0:
            print("level > 0")
            self.t3ch1.pulse_width_percent(0)
            self.t3ch2.pulse_width_percent(level)
       
        elif level < 0:
            print("level < 0")
            self.t3ch1.pulse_width_percent(-level)
            self.t3ch2.pulse_width_percent(0)
        
        else:
            self.t3ch1.pulse_width_percent(0)
            self.t3ch2.pulse_width_percent(0)
        print (f"Setting duty cycle to {level}")
    
def main():
    
#     pinB6 = pyb.Pin (pyb.Pin.board.PB6, pyb.Pin.OUT_PP) 
#     tim4 = pyb.Timer (4, freq=30)
#     ch1 = tim4.channel (1, pyb.Timer.ENC_AB, pin=pinB6)

      tim8 = pyb.Timer (8, freq=30)
      tim3 = pyb.Timer (3, freq=20000)
      tim5 = pyb.Timer (5, freq=20000)

      pinC6 = pyb.Pin (pyb.Pin.board.PC6, pyb.Pin.OUT_PP) 
      t8ch1 = tim8.channel (1, pyb.Timer.ENC_AB, pin=pinC6)
    
      pinC7 = pyb.Pin (pyb.Pin.board.PC7, pyb.Pin.OUT_PP) 
      t8ch2 = tim8.channel (2, pyb.Timer.ENC_AB, pin=pinC7)
      
      ENA = pyb.Pin (pyb.Pin.board.PA10, pyb.Pin.OUT_OD, pyb.Pin.PULL_UP)
      IN1A = pyb.Pin (pyb.Pin.board.PB4, pyb.Pin.OUT_PP)
      IN2A = pyb.Pin (pyb.Pin.board.PB5, pyb.Pin.OUT_PP)
      
      ENA.high()
      
      mdriver = Motordriver(ENA, IN1A, IN2A, tim3)
      
      p = True

      while True:
          print(tim8.counter())
          time.sleep(1)
          if p == True:
              mdriver.set_duty_cycle(-20)
              p = False
          else:
              mdriver.set_duty_cycle(99)
              p = True
              
    

if __name__ == '__main__':
    main()

