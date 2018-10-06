from time import sleep
import socket
from gpiozero import Servo

#TCP Connection
TCP_IP = "192.168.1.9"
TCP_PORT = 5005
BUFFER_SIZE = 1024

SOCKET = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
SOCKET.bind((TCP_IP, TCP_PORT))


SOCKET.listen(1) #wait for connection
conn, addr = SOCKET.accept()
print 'Connection address: ', addr

#Raspberry Connection
#ports = [17, 27, 22, 10, 9]
PORTS = [27, 22, 10, 9]
SERVOS = []

for port in PORTS:
    print "Appending port " + str(port)
    SERVOS.append(Servo(port))

while True:

    position = conn.recv(BUFFER_SIZE)
    if not position: break
    print "received data: ", position.decode()

    #position = raw_input("prompt")

    position = position.split(" ")
    print position
    for index, servo in enumerate(SERVOS, start=0):
        print "moving servo " + str(PORTS[index])
        pos = float(position[index])# / 180 - 1
        if(pos < -1):
            pos = -1
        if(pos > 1):
            pos = 1
        print pos
        servo.value = pos
conn.close()
