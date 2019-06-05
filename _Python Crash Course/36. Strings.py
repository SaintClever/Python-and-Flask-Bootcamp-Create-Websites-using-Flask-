print('hello')
print(len('hello'))
print(len('hel   lo'))

mystring = 'hello'
print(mystring[0])
print(mystring[1])

print(mystring[4])
# or
print(mystring[-1])

mystring = 'abcdefghij'
# The start position is inclusive and the end position is exclusive
print(mystring[0:3]) # abc
print(mystring[4:7]) # efg
print(mystring[7:10]) #hij
print('')

# SLICING
# [start:stop:step]
print(mystring[0:7:2]) # aceg
print(mystring[0:7]) # or print(mystring[:7])
print(mystring[7:0]) # print(mystring[7:])
print('')

print(mystring[::]) # Get everything
print(mystring[::2]) # Get everything but every second item
print(mystring[::-1]) # Reverse a string
print('')

mystring = 'abcdefghij'
'''mystring[0] = 'z' Strings are immutable when it comes to a single item/index change.
This is refered to as immutability'''

print(mystring + mystring)
print('hello ' + 'Nesta')
print('')

mystring = 'Hello World'
print(mystring.upper())
print(mystring.lower())
print(mystring.split())
print(mystring.split('W'))
print('')

username = 'Sammy'
color = 'blue'

print('The {} favorite is {}'.format(username, color))

# f string literals - ONLY in Python 3.6 and ABOVE!!
print(f'{username} chose {color}')
