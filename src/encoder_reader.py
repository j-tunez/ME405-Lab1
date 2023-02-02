import pyb

class EncoderReader:
    """!
    This class is used to read and keep track of the position of an encoder.

    Attributes:
        encpin1 (Pin): Pin object for encoder pin A
        encpin2 (Pin): Pin object for encoder pin B
        timer (Timer): Timer object for timing
        encthen (int): Counter value of the encoder during the last read
        position (int): Current position of the encoder
        encnow (int): Current counter value of the encoder
        tch1 (Channel): Channel object for timer channel 1
        tch2 (Channel): Channel object for timer channel 2
        delt (int): Change in encoder position since the last read

    """
    def __init__(self,enca,encb,tim):

        """
        Constructor method for the EncoderReader class.

        Parameters:
            enca (Pin): Pin object for encoder pin A
            encb (Pin): Pin object for encoder pin B
            tim (Timer): Timer object for timing

        """

        self.encpin1 = enca
        self.encpin2 = encb
        self.timer = tim
        self.tch1 = self.timer.channel (1, pyb.Timer.ENC_AB, pin=enca)
        self.tch2 = self.timer.channel (2, pyb.Timer.ENC_AB, pin=encb)
        
        
        self.encthen = 0
        self.position = 0
        
        self.encnow = 0
        
        


    def zero(self):

        """
        Reset the position of the encoder to zero.

        Returns:
            int: Current position of the encoder

        """
        
        self.position = 0

    def read(self):

        """
        Read the current position of the encoder.

        Returns:
            int: Current position of the encoder

        """
        
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
    
