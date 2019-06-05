# max and min
print(max(2,3))
print(max([1,4,7,12,100]))
print(min([47,45,2,9,19]))
print('') #space


# enumerate
mylist = ['a','b','c']
index = 0

# WITHOUT Enumerate
for letter in mylist:
    print(letter)
    print('Is at index: {}'.format(index))
    index = index + 1
    # index += index # because this is set to 0 its always zero
    print('')
print('') #space


#WITH enumerate
for item in enumerate(mylist):
    print(item)
print('') #space


for index,item in enumerate(mylist):
    print(item)
    print(f'Is at index {index}')
    print('')


# .join
mylist = ['a','b','c','d']

print(''.join(mylist))
print('--'.join(mylist))
print('-x-'.join(mylist))


# PROBLEM 1
# Write a function that returns a boolean
# (True/False) indicating if the word 'secret'
# is in a string.

# My answer
def user_string(user_input):
    if 'secret' in user_input:
        # print(True)
        return True
    else:
        # print(False)
        return False

result = user_string('ecret')
print(result)
print('')

# Jose's answer
def secret_check(mystring):
    if 'secret' in mystring:
        return True
    else:
        return False

print(secret_check('simple')) # check the return
print(secret_check('this is a secret'))
print('')


# Refactored answer
def secret_check_refactored(mystring):
    return 'secret' in mystring.lower()

print(secret_check_refactored('simple')) # check return
print(secret_check_refactored('this is a secret'))
print(secret_check_refactored('SECRET'))
print('')
