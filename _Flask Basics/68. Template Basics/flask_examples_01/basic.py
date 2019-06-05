from flask import Flask, render_template

app = Flask(__name__)

@app.route('/') # http://127.0.0.1:5000/
def index():
    return 'hello world!'

@app.route('/info') # http://127.0.0.1:5000/info
def info():
    return 'additional route'

@app.route('/info/<name>') # http://127.0.0.1:5000/info/name
def name(name):
    # return f'Hello my name is {name}'
    return 'Hello my name is {}'.format(name)

@app.route('/template') # http://127.0.0.1:5000/template
def template():
    return render_template('basic.html')

if __name__ == '__main__':
    app.run(debug=True)