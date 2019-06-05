from flask import Flask

app = Flask(__name__)

@app.route('/') #
def index():
    return '<p>Hello world!</p>'

@app.route('/info')
def info():
    return '<p>Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.</p>'

@app.route('/<name>')
def name(name):
    return f'Hello ther. my name is {name.upper()}'

if __name__ == '__main__':
    app.run()
