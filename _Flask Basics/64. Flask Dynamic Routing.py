from flask import Flask

app = Flask(__name__)

@app.route('/') # http://127.0.0.1:5000/
def index():
    return '<h1>Hello Puppy!</h1>'

@app.route('/information') # http://127.0.0.1:5000/information
def info():
    return '<h1>Puppies are cute!</h1>'

@app.route('/puppy/<name>') # http://127.0.0.1:5000/puppy/my_variable
def puppy(name):
    # return '<h1>This is a page for {}</h1>'.format(name)
    return 'Upper case: {}'.format(name.upper())

if __name__ == '__main__':
    app.run()
