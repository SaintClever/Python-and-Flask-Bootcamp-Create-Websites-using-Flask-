from flask import Flask

app = Flask(__name__)

@app.route('/') # http://127.0.0.1:5000/
def index():
    return '<h1>Hello world!</h1>'

@app.route('/information') # http://127.0.0.1:5000/information
def information():
    return '<h1>Welcome to Flask for python</h1>'

if __name__ == '__main__':
    app.run()
