
### Functions
#
# Formally, a function is a useful device that groups together a set of statements so they can be run more than once. They can also let us specify parameters that can serve as inputs to the functions.
#
# On a more fundamental level, functions allow us to not have to repeatedly write the same code again and again. If you remember back to the lessons on strings and lists, remember that we used a function len() to get the length of a string. Since checking the length of a sequence is a common task you would want to write a function that can do this repeatedly at command.
#
# Functions will be one of most basic levels of reusing code in Python, and it will also allow us to start thinking of program design (we will dive much deeper into the ideas of design when we learn about Object Oriented Programming).

# ## The def Statement
#
# To create a function we use the **def** keyword. This is the general form of a function:



def lowercase_function_name(argument1,argument2,argument3='default value'):
    '''
    This is the DocString of the function. It is where you can write a helpful
    description for anyone who will use your function.
    '''
    # After the docstring you write code that does stuff.


# We begin with def then a space followed by the name of the function. Try to keep names relevant, for example len() is a good name for a length() function. Also be careful with names, you wouldn't want to call a function the same name as a built-in function in Python (such as len).
#
# Next come a pair of parenthesis with a number of arguments separated by a comma. These arguments are the inputs for your function. You'll be able to use these inputs in your function and reference them. After this you put a colon.
#
# Now here is the important step, you must indent to begin the code inside your function correctly. Python makes use of whitespace to organize code. Lots of other programing languages do not do this, so keep that in mind.
#
# Next you'll see the doc-string, this is where you write a basic description of the function. Using iPython and iPython Notebooks, you'll be able to read these doc-strings by pressing Shift+Tab after a function name. Doc strings are not necessary for simple functions, but its good practice to put them in so you or other people can easily understand the code you write.

# ____
#
# **Let's now walk through lots of examples of different functions.**
# ___

# ### Example 1



def report_person():
    print("Reporting Person")


# If you call the function without parenthesis it won't run, instead it will just report back what the object is:

print(report_person)


# Use parenthesis to run the function:
report_person()


# ### Example 2
# ** Passing in arguments/parameters **
def report(name):
    print("Reporting {}".format(name))




# Notice the error
report()




report('Bond')


# ### Example 3
# ** Default arguments can be used to set a default value. **



def report(name='Jason'):
    print('Reporting {}'.format(name))


report()




report('Kay')


# ## The return keyword
# So far all of our functions have only been printing results, but what if we wanted to save the actual results of a function to another variable? How could we do this? Let's first see what happens with just print()


def add(n1,n2):
    print(n1+n2)




add(2,3)




result = add(2,3)




print(result)




print(type(result))


# Notice how we aren't able to save the result of the print() function. That is because it is not **returning** anything. Let's now use the return keyword.



def add(n1,n2):
    return n1+n2




add(2,3)




result = add(2,3)



print(result)








# ### Solving Problems with Functions
#
# Functions are a core building block for scripts and code. Let's show how you could solve a problem with a function.

# ** Write a function that returns a boolean (True/False) indicating if the word 'secret' is in a string. **



def secret_check(mystring):
    return 'secret' in mystring


# In[39]:

secret_check('This is a secret.')


# In[40]:

secret_check('SECRET')


# We can fix this with .lower()

# In[41]:

def secret_check(mystring):
    return 'secret' in mystring.lower()


# In[43]:

secret_check('SECRET!')


# _____

# ** Create a code maker function. This function will take in a string name and replace any vowels with the letter x.**

# In[53]:

def code_maker(mystring):
    output = list(mystring)
    for i,letter in enumerate(mystring):
        for vowel in ['a','e','i','o','u']:
            if letter.lower() == vowel:
                output[i] = 'x'

    output = ''.join(output)
    return output


# Let's see what **''.join(output)** does:



''.join(['a','b','c'])




'--'.join(['a','b','c'])




'-x-'.join(['a','b','c'])




code_maker('Edward')




code_maker('John')


# OTHER USEFUL Operators
print(max(2,3))

mylist = ['a','b','c']

for x in mylist:
    print(x)

for x in enumerate(mylist):
    print(x)

for i, letter in enumerate(mylist):
    print(i)
    print(letter)


#  Since functions are crucial to becoming a competent Python programmer,
# up next we will have some tasks for you to complete with functions. Good luck!
