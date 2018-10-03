from gpiozero import Servo
from time import sleep

#ports = [17,27,22,10,9]
ports = [27,22,10,9]
servos = []

for port in ports:
    print "Appending port " + str(port)
    servos.append(Servo(port))

while True:
    position = raw_input("prompt")
    print position
    position = position.split(" ")
    print position[0]
    for index, servo in enumerate(servos, start=0):
        print "moving servo " + str(ports[index])
        pos = float(position[index]) / 180 - 1
        print pos
        servo.value = pos
