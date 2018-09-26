from gpiozero import Servo
from gpiozero import AngularServo
from time import sleep

#ports = [17,27,22,10,9]
ports = [27,22,10,9]
servos = []

for port in ports:
	print "Appending port " + str(port)
	servos.append(Servo(port))

while True:
	for index, servo in enumerate(servos, start=0):
		print "moving servo " + str(ports[index])
		servo.min()
		sleep(2)
	for index, servo in enumerate(servos, start=0):
		print "moving servo " + str(ports[index])
		servo.mid()
		sleep(2)
	for index, servo in enumerate(servos, start=0):
		print "moving servo " + str(ports[index])
		servo.max()
		sleep(2)
