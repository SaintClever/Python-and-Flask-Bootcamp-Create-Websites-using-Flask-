print(1 > 2)
print(3 > 2)
print(3 >= 2)
print(3 == 3)
print(3 != 3)
print('')

username = "Admin"
check = "Admin"
print(username == check)
has_permission = False
logged_in = True
print('')

# print((1 == 2) and (2 < 3) or (4 == 4))
print(username == check and has_permission)

has_permission = True
print(username == check and has_permission)

print(logged_in and has_permission)
