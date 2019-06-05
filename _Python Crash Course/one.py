# one.py

def func():
	print('Func() in one.py')


# def function_00():
# 	pass

# def function_01():
# 	pass


print('Top level in one.py')

if __name__ == '__main__':
	print('one.py is being ran directly!')
else:
	print('one.py has been imported')

	# used for organizing functions when working with large packages
	# function_00
	# function_01