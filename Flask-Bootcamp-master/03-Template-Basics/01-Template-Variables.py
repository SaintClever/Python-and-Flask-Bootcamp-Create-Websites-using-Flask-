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
    return render_template('01-Template-Variables.html',name=name)

@app.route('/advpuppy/<name>')
def adv_puppy_name(name):
    letters = list(name)
    pup_dict = {'pup_name':name}
    return render_template('01-Template-Variables.html',
                           name=name,mylist=letters,mydict=pup_dict)


if __name__ == '__main__':
    app.run(debug=True)
