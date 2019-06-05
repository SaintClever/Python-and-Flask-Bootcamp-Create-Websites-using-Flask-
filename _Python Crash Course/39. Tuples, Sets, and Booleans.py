''' TUPLES '''
t = (1,2,3)
mylist = [1,2,3]
# print(t)
# print(t[0])

mylist[0] = 'NEW'
print(mylist)
print('')

# t[0] = 'NEW' ERROR bound because tuples are immutable
# print(t)

''' SETS '''
x = set() # set() - An unordered set of unique elements
print(x)
x.add(1)
x.add(2)
x.add(3)
x.add(3)
x.add(3)
print(x)

mylist = [1,3,12,3,44,6,7111,2,22,2,2,2,2,2,3,5]
print(set(mylist))

''' BOOLEANS '''
a = True
print(a)

b = False
print(b)

# SPECIAL KEYWORD
c = None
print(c)

print(1 > 2)
print(1 < 2)
