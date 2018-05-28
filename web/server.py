import serial 
from flask import Flask, request, send_from_directory

ser = serial.Serial('/dev/cu.usbmodem1421', 9600) 
app = Flask(__name__)

@app.route('/')
def send_static():
    return send_from_directory('.', 'index.html')


@app.route("/send_data")
def send_data():
    alpha = int(float(request.args.get('alpha'))/2)
    beta = int((float(request.args.get('beta'))+180)/2)
    gamma = int((float(request.args.get('gamma'))+90))
    touch = request.args.get("touch")
    print(alpha)
    print(beta)
    print(gamma)
    
    ser.write("#")
    ser.write(str(alpha)+";")
    ser.write(str(beta)+";")
    ser.write(str(gamma)+";")
    ser.write(touch.encode("ascii", "ignore")+";")
    return "ok"
