from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/report')
def report():

    username = request.args.get('username')

    char_islower = False
    char_isupper = False
    char_isdigit = False

    char_islower = any(character.islower() for character in username)
    char_isupper = any(character.isupper() for character in username)
    char_isdigit = username[-1].isdigit()

    requirements_met = char_islower and char_isupper and char_isdigit

    return render_template('report.html', username=username, char_islower=char_islower, char_isupper=char_isupper, requirements_met=requirements_met)


@app.errorhandler(404)
def error_handler(error):
    return render_template('404.html'), 404

if __name__ == '__main__':
    app.run(debug=True)