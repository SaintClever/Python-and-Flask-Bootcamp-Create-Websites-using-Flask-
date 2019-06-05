# WINDOWS: set OAUTHLIB_INSECURE_TRANSPORT=1
# Macos/linux: export OAUTHLIB_INSECURE_TRANSPORT=1
#  https://flask-dance.readthedocs.io/en/latest/quickstarts/google.html

###########################################################################
###########################################################################
# Visit the Google Developers Console at https://console.developers.google.com and
# create a new project. In the “APIs & auth” section, click on “Credentials”, and
# then click the “Create a new Client ID” button. Select “Web Application” for
# the application type, and click the “Configure consent screen” button. Put in
# your application information, and click Save. Once you’ve done that, you’ll
# see two new fields: “Authorized JavaScript origins” and “Authorized redirect
# URIs”. Put http://localhost:5000/login/google/authorized into “Authorized
# redirect URIs”, and click “Create Client ID”. Take note of the “Client ID”
# and “Client Secret” for the application.
###########################################################################
###########################################################################

###########################################################################
#### IMPORTANT NOTE!!! HERE IS SOME CODE FOR THIS TO WORK LOCALLY ########
#### YOU SHOULD ONLY NEED THIS CODE FOR LOCAL TESTING  ##################
#### PLEASE REFER TO THE FLASK_DANCE DOCS FOR MORE INFO ################
#######################################################################
import os
os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = '1'
os.environ["OAUTHLIB_RELAX_TOKEN_SCOPE"] = '1'
#######################################################################
#######################################################################
from flask import Flask, redirect, url_for, render_template, session
from flask_dance.contrib.google import make_google_blueprint, google

app = Flask(__name__)



app.config['SECRET_KEY'] = 'mysecretkey'


blueprint = make_google_blueprint(
    client_id="######.apps.googleusercontent.com",
    client_secret="####",
    # reprompt_consent=True,
    offline=True,
    scope=["profile", "email"]
)
app.register_blueprint(blueprint, url_prefix="/login")

@app.route('/')
def index():
    return render_template("home.html")

@app.route('/welcome')
def welcome():
    resp = google.get("/oauth2/v2/userinfo")
    assert resp.ok, resp.text
    email=resp.json()["email"]

    return render_template("welcome.html",email=email)

@app.route("/login/google")
def login():
    if not google.authorized:
        return render_template(url_for("google.login"))

    resp = google.get("/oauth2/v2/userinfo")
    assert resp.ok, resp.text
    email=resp.json()["email"]

    return render_template("welcome.html",email=email)


if __name__ == "__main__":
    app.run()
