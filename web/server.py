from flask import Flask, request, send_from_directory
app = Flask(__name__)


@app.route('/')
def send_static():
    return send_from_directory('.', 'index.html')


@app.route("/send_data")
def send_data():
    request.args.get('alpha')
    request.args.get('beta')
    request.args.get('gamma')
    request.args.get('touch')
