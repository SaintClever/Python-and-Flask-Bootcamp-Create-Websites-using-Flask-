from myproject import db, login_manager #! imports from the __init__.py file
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin

## Loads the current user info after login
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)

class User(db.Model, UserMixin):

    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(64), unique=True, index=True) ## String(64) limits emailname length and prevents spam; unique prevents dublicate email address
    username = db.Column(db.String(64), unique=True, index=True)
    password_hash = db.Column(db.String(128))

    def __init__(self, email, username, password):
        self.email = email
        self.username = username
        self.password_hash = generate_password_hash(password) #! We save the password_hash not the password

    def check_password(self, password):
        return check_password_hash(self.password_hash, password) ## check to see if self.password_hash matches password