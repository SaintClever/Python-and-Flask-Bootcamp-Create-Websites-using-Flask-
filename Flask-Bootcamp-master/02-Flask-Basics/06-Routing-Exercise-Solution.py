from flask import Flask
from flask import request
app = Flask(__name__)


@app.route('/')
def index():
    # Welcome Page
    return "<h1>Welcome! Go to /puppy_latin/name to see your name in puppy latin!</h1>"

@app.route('/puppy_latin/<name>')
def puppylatin(name):
    # Puppy Latin the name that comes in!
    pupname = ''
    if name[-1]=='y':
        pupname = name[:-1]+'iful'
    else:
        pupname = name+'y'

    return "<h1>Hi {}! Your puppylatin name is {} </h1>".format(name,pupname)


if __name__ == '__main__':
    app.run(debug=True)
