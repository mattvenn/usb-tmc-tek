from datetime import datetime
import pyvisa as visa
import time

class Scope():

    def __init__(self):

        resources = visa.ResourceManager('@py')

        self.scope = resources.open_resource('USB0::1689::924::C010251::0::INSTR', read_termination="\n", write_termination="\n")
        self.scope.timeout = 8000
        print(self.scope.query('*IDN?'))
        self.scope.write("SAVe:IMAGe:FILEFormat PNG")
        self.scope.write("SAVe:IMAGe:INKSaver OFF")

    def grab_png(self, image_name=None):
        if image_name is None:
            # Generate a filename based on the current Date & Time
            dt = datetime.now()
            fileName = dt.strftime("%Y%m%d_%H%M%S.png")

        print("grabbing image")
        print(self.scope.write("HARDCopy STARt"))
        imgData = self.scope.read_raw()

        with open(fileName, "wb") as fh:
            print("written to %s" % fileName)
            fh.write(imgData)

    def single(self):
        self.scope.write("TRIGger:MODe NORMal")         # set trigger normal
        self.scope.write("ACQuire:STOPAfter SEQ")       # single shot
        self.scope.write("ACQuire:STATE RUN")           # run
        print("waiting for trigger...")
        while True:
            state = self.scope.query("TRIGger:STATE?")  # get trigger state
            print(state)
            if(state == "SAV"):
                break
            time.sleep(0.1)

    def measure(self):
        #self.scope.write('*rst')
        self.scope.query('*opc?')
        self.scope.write('acquire:state off')
        self.scope.write('acquire:stopafter sequence')
        self.scope.write("MEASUrement:IMMed:SOURCE CH1")
        self.scope.write("MEASUrement:IMMed:TYPE FREQuency")
        self.scope.write('acquire:state on')
        self.scope.query('*opc?')
        return self.scope.query("MEASUrement:IMMed:VALue?")

    def __del__(self):
        self.scope.close()


if __name__ == '__main__':
    scope = Scope()
   # scope.grab_png()
#    scope.single()
    print(scope.measure())
   # scope.grab_png()
