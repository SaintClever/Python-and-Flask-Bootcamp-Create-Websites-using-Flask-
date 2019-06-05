# Set up your imports here!
# import ...
from flask import Flask

app = Flask(__name__)

@app.route('/') # Fill this in!
def index():
    # Welcome Page
    # Create a generic welcome page.
    return '<h1>Go to puppy_name/name and see the result!</h1>'

@app.route('/puppy_latin/<name>') # Fill this in!
def puppylatin(name):
    # This function will take in the name passed
    # and then use "puppy-latin" to convert it!
    # ex: rufus = rufusy | spotty = spottiful

    # HINT: Use indexing and concatenation of strings
    # For Example: "hello"+" world" --> "hello world"


    if name[-1] == 'y':
        name = name[:-1] + 'iful'
    else:
        name = name + 'y'

    # return '<h1>Your puppy latin name is: {}</h1>'.format(name.capitalize())
    return f'<h1>Your puppy latin name is: {name.capitalize()}</h1>'


if __name__ == '__main__':
    # Fill me in!
    app.run(debug=True)
