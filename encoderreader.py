import pyb

class Encoderreader:
    """!This class does something. Nobody knows what it does.
    """
    def __init__(self,enca,encb,tim):
        self.encpin1 = enca
        self.encpin2 = encb
        self.timer = tim
        self.encthen = self.timer.read()

    def read(self):
        self.encnow = self.timer.read()
        self.delt = self.encnow - self.encthen
        self.encthen = self.encnow
        self.position = self.position + self.delt
        return self.position

    def zero(self):
        self.encnow = self.timer.read()
        self.delt = self.encnow - self.encthen
        reset = 32768
        if self.delt > reset:
            self.encthen = self.encnow
            self.delt -= 65536
            self.position = self.position + self.delt
        elif self.delt < -reset:
            self.encthen = self.encnow
            self.delt += 65536
            self.position = self.position + self.delt
        else:
            self.position = self.position + self.delt