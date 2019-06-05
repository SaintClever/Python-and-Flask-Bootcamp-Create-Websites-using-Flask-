# Hints and Help for Function Tasks
# Hi there!
#
# Up next are your function tasks. I want to quickly mention a few functions that may be useful to you that you may not have seen yet. Specifically these functions will be useful for Task #7 , the last task.
#
# The modulus operator
#
# This % mod operator returns back the remainder after a division. For example 3 divided by 2 and be shown to be 1 remainder 1. Since 2 goes into 3 one time, with a remainder of 1 (2+1=3). You can use the % operator in Python to view the remainder. For example:
#
# 3 % 2
#
# returns 1
#
# 17 % 15
#
# returns 2 (since its the remainder after the division of 17/15)
#
# 100 % 10
#
# returns 0, since 10 goes into 100 evenly.
#
# This is really useful for figuring out if a number is even or not. You just simply check if the number % 2 returns 0. If it does, then its even.

def even_check(num):
    if num % 2 == 0:
        print("Number was even")
    else:
        print("Odd number")


The sum() # function

# Just like max() and min(), Python also has a built in sum() function that can return the sum() of all the numbers in a list.

sum([1,2,3,4])  # will return back 10.
