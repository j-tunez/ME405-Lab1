"""@package docstring
Lab 1 - Encoder
"""
import pyb
import time
import motor_driver
import encoder_reader





    
def main():
    
#     pinB6 = pyb.Pin (pyb.Pin.board.PB6, pyb.Pin.OUT_PP) 
#     tim4 = pyb.Timer (4, freq=30)
#     ch1 = tim4.channel (1, pyb.Timer.ENC_AB, pin=pinB6)

      tim8 = pyb.Timer (8, freq=30)
      tim3 = pyb.Timer (3, freq=20000)
      tim5 = pyb.Timer (5, freq=20000)

      pinC6 = pyb.Pin (pyb.Pin.board.PC6, pyb.Pin.OUT_PP) 
    
      pinC7 = pyb.Pin (pyb.Pin.board.PC7, pyb.Pin.OUT_PP)
      
      
      encreader = encoder_reader.EncoderReader(pinC6, pinC7, tim8)
      
    
   
      
      ENA = pyb.Pin (pyb.Pin.board.PA10, pyb.Pin.OUT_OD, pyb.Pin.PULL_UP)
      IN1A = pyb.Pin (pyb.Pin.board.PB4, pyb.Pin.OUT_PP)
      IN2A = pyb.Pin (pyb.Pin.board.PB5, pyb.Pin.OUT_PP)
      
      ENA.high()
      
      mdriver = motor_driver.MotorDriver(ENA, IN1A, IN2A, tim3)
      
      p = True

      while True:
          print(encreader.zero())
          time.sleep(1)
          if p == True:
              mdriver.set_duty_cycle(20)
              p = False
          else:
              mdriver.set_duty_cycle(90)
              p = True
              
    

if __name__ == '__main__':
    main()

