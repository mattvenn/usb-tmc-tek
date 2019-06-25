from datetime import datetime
import visa, time

class scope():

    def __init__(self):

        resources = visa.ResourceManager('@py')

        self.scope = resources.open_resource('USB0::1689::924::C010251::0::INSTR', read_termination="\n", write_termination="\n")
        self.scope.timeout = 2000
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
            fh.write(imgData)

    def single(self):
        self.scope.write("TRIGger:MODe NORMal") # set trigger normal
        #print(scope.write("ACQuire:STOPAfter RUNSTop")) # continuous
        self.scope.write("ACQuire:STOPAfter SEQ") # single shot
        self.scope.query("ACQ?")
        self.scope.write("ACQuire:STATE RUN") # acquire single trigger
        print("waiting for trigger...")

    def __del__(self):
        self.scope.close()


if __name__ == '__main__':
    scope = mso2004()
    scope.single()
    time.sleep(2)
    scope.grab_png()
