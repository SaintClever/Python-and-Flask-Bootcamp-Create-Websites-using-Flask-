# FOR LOOP
seq = [1,2,3,4,5]

# for num in seq:
#     print(num**2)
#     # print('Hello')

mystring = 'hello'

# for char in mystring:
#     print(char)


salaries = {'John':10, 'Sally':20, 'Lisa':30}

for employee in salaries:
    print(employee) # gets keys by default
    print('has a salary of:')
    print(salaries[employee]) # gets value
    print('')

# Iterating through tuples
mypairs = [('a',1), ('b',2), ('c',3)]
print(len(mypairs))

for item in mypairs:
    print(item)


print('') # space


# TUPLE UNPACKING
for (item1, item2) in mypairs:
    print(item1)
    print(item2)


print('') # space


# TUPLE UNPACKING. Don't really need the paranthesis
for letter, num in mypairs:
    print(letter, num)


print('') # space


# WHILE LOOP:
i = 1

while i < 5:
    print(f'i is currently: {i}')
    # i = i + 1
    # i = i + i
    i += i


print('') # space

# RANGE
for x in range(0,5):
    print(x)


print('') # space


# RANGE with (START, STOP, STEP_SIZE)
for x in range(0, 11, 2):
    print(x)

# CASTING to create a list
result = list(range(0,11,2))
print(result)


print('') # space


# IN: keyword
print('s' in 'asdjdkfasjlfdjafiewuriheqithbf')
print('z' in 'asdjdkfasjlfdjafiewuriheqithbf')
print('1' in 'dsfasfaiuhfyr1')
print('z' in [1,2,3])
print(1 in [1,2,3])
