# two.py

import one

print('Top level in two.py')

one.func()

if __name__ == '__main__':
	print('Two.py is being ran directly!')
else:
	print('Two.py has been imported!')