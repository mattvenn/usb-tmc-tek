import usbtmc
# ms2004b 0699, idProduct=039c
scope = usbtmc.Instrument(int("0699", 16),int("039c", 16))
print(scope.ask("*IDN?"))

# read horizontal timescale
scope.write("HORIZONTAL:MAIN:SCALE?")                                                                                                                                                                     
timescale = float(scope.read(20))

""" doesn't work
#CH1,CH2,REFA,REFB
source = "CH1"
#scope.write("DATA:SOURCE " + source)

# Get the voltage scale
scope.write("WFMP:" + source + ":YMULT?")
ymult = float(scope.read(20))

# And the voltage offset
scope.write("WFMP:" + source + ":YOFF?")
yoff = float(scope.read(20))

# And the voltage zero
scope.write("WFMP:" + source + ":YZERO?")
yzero = float(scope.read(20))
"""
# get scale
scope.write('ch1:scale?')
print float(scope.read(20))

import ipdb; ipdb.set_trace()

# save to a file, once triggered
scope.write("SAVE:IMAG:FILEF PNG")
scope.write("HARDCOPY START") 
screenData = scope.read_raw()
with open("data.png", 'w') as fh:
    fh.write(screenData)  
