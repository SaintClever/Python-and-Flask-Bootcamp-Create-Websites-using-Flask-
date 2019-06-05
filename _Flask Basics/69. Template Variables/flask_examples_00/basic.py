from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    name = 'Nesta'
    characters_in_name = list(name)
    user_name = {'name':'Saint. Clever'}
    return render_template('basic.html', name=name,           
                            characters_in_name=characters_in_name,
                            user_name=user_name
                            )

if __name__ == '__main__':
    app.run(debug=True)