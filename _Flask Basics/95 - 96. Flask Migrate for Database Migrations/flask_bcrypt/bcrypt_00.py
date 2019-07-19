from flask_bcrypt import Bcrypt

bcrypt = Bcrypt()

password = 'supersecretpassword'

hashed_password = bcrypt.generate_password_hash(password=password)
print(hashed_password)

check_hased_password = bcrypt.check_password_hash(hashed_password, 'wrongpassword')
print(check_hased_password)

check_hased_password = bcrypt.check_password_hash(hashed_password, 'supersecretpassword')
print(check_hased_password)