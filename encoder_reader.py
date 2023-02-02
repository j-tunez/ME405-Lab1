import pyb

class EncoderReader:
    """!This class does something. Nobody knows what it does.
    """
    def __init__(self,enca,encb,tim):
        self.encpin1 = enca
        self.encpin2 = encb
        self.timer = tim
        self.tch1 = self.timer.channel (1, pyb.Timer.ENC_AB, pin=enca)
        self.tch2 = self.timer.channel (2, pyb.Timer.ENC_AB, pin=encb)
        
        
        self.encthen = 0
        self.position = 0
        
        self.encnow = 0
        
        


    def zero(self):
        
        self.position = 0

    def read(self):
        
        self.delt = self.encnow - self.encthen
        self.encthen = self.encnow
        print("encnow", self.encnow)
        print("encthen", self.encthen)
        print("delt", self.delt)
        reset = 32768
        if self.delt > reset:
            self.encthen = self.encnow
            self.delt -= 2*reset
            self.position = self.position + self.delt
        elif self.delt < -reset:
            self.encthen = self.encnow
            self.delt += 2*reset
            self.position = self.position + self.delt
        else:
            self.position = self.position + self.delt
        self.encnow = self.timer.counter()
        return self.position
    
