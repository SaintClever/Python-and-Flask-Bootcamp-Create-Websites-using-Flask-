from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/report')
def report():

    lower_letter = False
    upper_letter = False
    num_end = False

    user_name = request.args.get('user_name')
    
    lower_letter = any(c.islower() for c in user_name)
    upper_letter = any(c.isupper() for c in user_name)
    num_end = user_name[-1].isdigit()

    report = lower_letter and upper_letter and num_end

    return render_template('report.html', report=report, lower=lower_letter, upper=upper_letter, num_end=num_end) 

if __name__ == '__main__':
    app.run(debug=True)