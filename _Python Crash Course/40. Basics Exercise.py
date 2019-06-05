#####################################
#### PART 6: EXERCISE REVIEW  #######
#####################################

# Time to review all the basic data types we learned! This should be a
# relatively straight-forward and quick assignment.

###############
## Problem 1 ##
###############

# Given the string:
s = 'flask'

# Use indexing to print out the following:
# 'f'
print(s[0])

# 's'
print(s[3])

# 'ask'
print(s[2:])

# 'las'
print(s[1:4])

# 'k'
print(s[4])
print(s[-1])

# Bonus: Use indexing to reverse the string
print(s[::-1])
print('')

###############
## Problem 2 ##
###############

# Given this nested list:
mylist = [3,7,[1,4,'hello']]
# Reassign "hello" to be "goodbye"
print(mylist[2][2])
mylist[2][2] = 'goodbye'
print(mylist)
print('')

###############
## Problem 3 ##
###############

# Using keys and indexing, grab the 'hello' from the following dictionaries:

d1 = {'simple_key':'hello'}
print(d1['simple_key'])

d2 = {'k1':{'k2':'hello'}}
print(d2['k1']['k2'])

d3 = {'k1':[{'nest_key':['this is deep',['hello']]}]}
print(d3['k1'][0]['nest_key'][1][0])
print('')

###############
## Problem 4 ##
###############

# Use a set to find the unique values of the list below:
mylist = [1,1,1,1,1,2,2,2,2,3,3,3,3]
print(set(mylist))

###############
## Problem 5 ##
###############

# You are given two variables:
age = 4
name = "Sammy"

# Use print formatting to print the following string:
"Hello my dog's name is Sammy and he is 4 years old"

print("Hello my dog's name is {} and he is {} years old".format(name,age))
print("Hello my dog's name is {name} and he is {age} years old".format(name=name,age=age))
print(f"Hello my dog's name is {name} and he is {age} years old")
