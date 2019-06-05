from flask import Flask
from flask import request
app = Flask(__name__)


@app.route('/')
def index():
    # Grab the visitors User Agent information
    browser_info = request.headers.get('User-Agent')
    return '<h2>Here is your browser info:</h2> <p>{}</p>'.format(browser_info)

if __name__ == '__main__':
    app.run(debug=True)
