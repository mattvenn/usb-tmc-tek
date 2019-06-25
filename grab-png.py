from datetime import datetime
import visa, time
resources = visa.ResourceManager('@py')

scope = resources.open_resource('USB0::1689::924::C010251::0::INSTR', read_termination="\n", write_termination="\n")
scope.timeout = 10000
print(scope.query('*IDN?'))

print(scope.write("SAVe:IMAGe:FILEFormat PNG"))
print(scope.write("SAVe:IMAGe:INKSaver OFF"))
print(scope.write("HARDCopy STARt"))


print("capture image data...")
imgData = scope.read_raw()
print("done")

# Generate a filename based on the current Date & Time
dt = datetime.now()
fileName = dt.strftime("%Y%m%d_%H%M%S.png")

imgFile = open(fileName, "wb")
imgFile.write(imgData)
imgFile.close()

scope.close()
