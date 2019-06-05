from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('04-Home.html')

@app.route('/puppy/<name>')
def pup_name(name):
    return render_template('04-Puppy.html',name=name)



if __name__ == '__main__':
    app.run(debug=True)
