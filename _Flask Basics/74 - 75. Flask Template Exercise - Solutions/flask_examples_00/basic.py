from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/report')
def report():

    username = request.args.get('username')

    char_isupper = False
    char_islower = False
    char_int = False

    char_isupper = any(char.isupper() for char in username)
    char_islower = any(char.islower() for char in username)
    char_int = username[-1].isdigit()

    requirements_met = char_isupper and char_islower and char_int

    return render_template('report.html', requirements_met=requirements_met,char_isupper=char_isupper, char_islower=char_islower, char_int=char_int)


if __name__ == '__main__':
    app.run(debug=True)