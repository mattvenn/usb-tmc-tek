from datetime import datetime
import visa, time
resources = visa.ResourceManager('@py')

scope = resources.open_resource('USB0::1689::924::C010251::0::INSTR', read_termination="\n", write_termination="\n")

scope.write("SAVe:IMAGe:FILEFormat PNG")
scope.write("SAVe:IMAGe:INKSaver OFF")
scope.write("HARDCopy STARt")
imgData = scope.read_raw()

# Generate a filename based on the current Date & Time
dt = datetime.now()
fileName = dt.strftime("%Y%m%d_%H%M%S.png")

imgFile = open(fileName, "wb")
imgFile.write(imgData)
imgFile.close()

scope.close()
