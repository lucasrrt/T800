import serial 
ser = serial.Serial('/dev/cu.usbmodem1421', 9600) 

while True: 
    print ser.readline() 
    ser.write("0;")
    ser.write("0;")
    ser.write("0;")
    ser.write("true;")
