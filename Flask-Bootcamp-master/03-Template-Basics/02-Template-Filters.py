from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
def index():
    # Pass in a puppy name
    # We insert it to the html with jinja2 templates!
    return '<h1> Go to /puppy/name </h1>'

@app.route('/puppy/<name>')
def puppy_name(name):
    # Pass in a puppy name
    # We insert it to the html with jinja2 templates!
    return render_template('02-Template-Filters.html',name=name)



if __name__ == '__main__':
    app.run(debug=True)
