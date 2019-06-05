if 1 < 2:
    print('Yep!')

if 1 == 2:
    print('Yep!')

username = "admin"
check = "admin"

if username == check and 1 == 1:
    print("Access Granted!")
else:
    print("All above conditions, were not true!")

# test/check two
if 1 == 2:
    print("Access Granted!")
elif 1 == 1:
    print("Middle condition true!")
elif 4 == 4:
    print("Third condition!")
else:
    print("All above conditions, were not true!")

username = "Nesta"
permission = False

if username == "admin" and permission:
    print("Full Access")
elif username == "admin" and permission == False:
    print("Admin access only, no full permission")
else:
    print("NO access")
