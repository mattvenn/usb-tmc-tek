import usbtmc
# ms2004b 0699, idProduct=039c
scope = usbtmc.Instrument(int("0699", 16),int("039c", 16))
print(scope.ask("*IDN?"))

# read horizontal timescale
scope.write("HORIZONTAL:MAIN:SCALE?")                                                                                                                                                                     
timescale = float(scope.read(20))

# save to a file, once triggered
scope.write("SAVE:IMAG:FILEF PNG")
scope.write("HARDCOPY START") 
screenData = scope.read_raw()
with open("data.png", 'w') as fh:
    fh.write(screenData)  
