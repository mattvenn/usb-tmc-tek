import visa, time
resources = visa.ResourceManager('@py')

scope = resources.open_resource('USB0::1689::924::C010251::0::INSTR', read_termination="\n", write_termination="\n")
#Return the Rigol's ID string to tell us it's there
print(scope.query('*IDN?'))
print(scope.write("TRIGger:MODe NORMal")) # set trigger normal
#print(scope.write("ACQuire:STOPAfter RUNSTop")) # continuous
print(scope.write("ACQuire:STOPAfter SEQ")) # single shot
print(scope.query("ACQ?"))
print(scope.write("ACQuire:STATE RUN")) # acquire single trigger
"""
print(scope.query("ACQ?"))
#print(scope.query("MEASU?"))
print(scope.query("MEASUrement:MEAS1:MEAN?"))
print(scope.query("CH1:OFFSet?"))
print(scope.write("CH1:OFFSet 0.02"))
print(scope.query("CH1:OFFSet?"))

# try to grab a capture
print(scope.write("data:source ch1"))
print(scope.write("curve?"))
data = scope.read_values()
print(len(data))
x = range(len(data))


import matplotlib.pyplot as plt
fig = plt.figure()
ax = fig.add_subplot(1,1,1)
ax.plot(x, data)
plt.show()
"""
