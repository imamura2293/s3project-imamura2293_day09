from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    return '<h1>Hello World!</h1>'


@app.route('/home')
def home():
    return 'homeだよ～'


@app.route('/greet/<string:name>')
def greet(name: str):
    return f'Hello! {name}'


@app.route('/shout/<string:name>')
def shout(name: str):
    return f'{name.upper()}!!!'


if __name__ == '__main__':
    app.run(debug=True)
