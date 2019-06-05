from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/sign_up')
def sign_up():
    return render_template('sign_up.html')

@app.route('/thank_you')
def thank_you():
    first_name = request.args.get('first_name')
    last_name = request.args.get('last_name')

    return render_template('thank_you.html', first_name=first_name, last_name=last_name)

@app.errorhandler(404)
def error_handler(e):
    return render_template('404.html'), 404

if __name__ == '__main__':
    app.run(debug=True)