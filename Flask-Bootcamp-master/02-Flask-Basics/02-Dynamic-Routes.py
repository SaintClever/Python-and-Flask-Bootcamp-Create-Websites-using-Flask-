from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Hello Puppy!</h1>'

@app.route('/information')
def info():
    return '<h1>Puppies are cute!</h1>'

@app.route('/puppy/<name>')
def puppy(name):
    # Page for an individual puppy.
    return '<h1>This is a page for {}<h1>'.format(name)

if __name__ == '__main__':
    app.run()
