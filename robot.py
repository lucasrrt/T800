import serial 
ser = serial.Serial('/dev/cu.usbmodem1421', 9600) 

while True: 
    print ser.readline() 
    ser.write("180;")
    ser.write("180;")
    ser.write("180;")
    ser.write("false;")
