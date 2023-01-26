"""@package docstring
Lab 1 - Encoder
"""

import time

def setup():
    pass
    

    

    
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
      
      pinPA10 = pyb.Pin (pyb.Pin.board.PA10, pyb.Pin.OUT_PP)
      pinPB4 = pyb.Pin (pyb.Pin.board.PB4, pyb.Pin.OUT_PP)
      pinPB5 = pyb.Pin (pyb.Pin.board.PB5, pyb.Pin.OUT_PP)
      
      t3ch1 = tim3.channel (1, pyb.Timer.PWM, pin=pinB4)
      t3ch2 = tim3.channel (2, pyb.Timer.PWM, pin=pinB5)
      
      t3ch1.pulse_width_percent (50)
      t3ch2.pulse_width_percent (50)
      

      while True:
          print(tim8.counter())
          time.sleep(0.1)
    

if __name__ == '__main__':
    setup()
    main()

