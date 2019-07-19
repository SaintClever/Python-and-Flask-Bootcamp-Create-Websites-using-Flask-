from werkzeug.security import generate_password_hash, check_password_hash

hashed_pass = generate_password_hash('mypassword')
print(hashed_pass)

check_pass = check_password_hash(hashed_pass, 'wrongpassword')
print(check_pass)

check_pass = check_password_hash(hashed_pass, 'mypassword')
print(check_pass)