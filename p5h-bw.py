#!/usr/bin/python3
import serial
import time
from mso2004 import Scope
port = "/dev/ttyUSB0"
print("open %s" % port)
ser=serial.Serial()
ser.port=port
ser.baudrate=9600
ser.open()

def finish():
    ser.write(0x18) # universal device clear
    exit(0)

def clear_error():
    ser.write("*CLS\n")

def command(command):
    ser.write(str.encode(command + "\n"))

if __name__ == '__main__':
    scope = Scope()

    command("SINE")
    command("EMFPP 0.1")
    command("DCOFFS 0.0")
    command("OUTPUT ON")
    with open("results.csv", 'w') as fh:
        for freq in range(50000, 2000000, 10000):
            command("FREQ %d" % freq)
            time.sleep(0.1)
            amp = scope.measure()
            fh.write("%f,%f\n" % (freq, amp))

    command("OUTPUT OFF")

finish()
