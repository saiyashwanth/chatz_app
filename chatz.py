from flask import Flask 
from flask_socketio import SocketIO, send
from flask import render_template


app = Flask(__name__)
app.config['SECRET_KEY'] = 'mysecret'
socketio = SocketIO(app)

def messageRecived():
  print( 'message was received!!!' )

@socketio.on('my event')
def handleMessage( json ):
	print('Message: ' + str(json))
	socketio.emit('my response', json)

@app.route("/")
def get_news():
	return render_template("home.html")


if __name__ == '__main__':
	socketio.run(app)