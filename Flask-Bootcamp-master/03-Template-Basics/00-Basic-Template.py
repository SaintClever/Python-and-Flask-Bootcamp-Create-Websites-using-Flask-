from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
def index():
    # Connecting to a template (html file)
    return render_template('00-Basic-Template.html')

if __name__ == '__main__':
    app.run(debug=True)
