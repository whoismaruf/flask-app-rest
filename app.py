from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World from Maruf Khan!!'


@app.route('/hi')
def say_hi():
	return "Hi from signed commit"


if __name__ == '__main__':
    app.run()
