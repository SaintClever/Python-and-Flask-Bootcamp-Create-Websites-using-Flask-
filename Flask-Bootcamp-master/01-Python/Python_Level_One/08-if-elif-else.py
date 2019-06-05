##################################
### if,elif, else Statements #####
##################################

# Indentation is extremely important in Python and is basically Python's way of
# getting rid of enclosing brackets like {} we've seen in the past and are common
# with other languages. This adds to Python's readability and is huge part of the
# "Zen of Python". It is also a big reason why its so popular for beginners. Any
# text editor or IDE should be able to auto-indent for you, but always double check
# this if you ever get errors in your code! Code blocks are then noted by a colon (:).

# Now let's show some examples of if, elif, and else statements:

if 1 < 2:
    print('Yep!')

if 1 < 2:
    print('yep!')


# If Else - Make sure to line up the else with the if statement to "connect" them

if 1 < 2:
    print('first')
else:
    print('last')

###
###

if 1 > 2:
    print('first')
else:
    print('last')


# To add more conditions (like else if) you just use a single phrase "elif"

if 1 == 2:
    print('first')
elif 3 == 3:
    print('middle')
else:
    print('Last')
