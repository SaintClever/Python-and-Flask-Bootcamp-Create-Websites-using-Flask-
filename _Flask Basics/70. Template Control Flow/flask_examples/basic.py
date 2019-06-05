from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    mylist = [1,2,3,4,5]
    puppies = ['Fluffy', 'Rufus', 'Spike']
    user_logged_in = True
    some_other_condition = True
    return render_template('basic.html', mylist=mylist, puppies=puppies,
                            user_logged_in=user_logged_in,
                            some_other_condition=some_other_condition)

if __name__ == '__main__':
    app.run(debug=True)