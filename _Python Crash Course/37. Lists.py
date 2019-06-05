mylist = ['a', 'b', 'c', 'd', 'e']

print(mylist)
print(len(mylist))

print(mylist[1])
print(mylist[1:-1]) # or print(mylist[1:4])
print('')

mylist.append('z') # append adds to end of list
print(mylist)

mylist.insert(0, 'z') # two params; insert('index location', 'item to insert')
print(mylist)

popped_item = mylist.pop(0) # remove firsgt index. If no index is given by default it removes the last item within the list/array
print(mylist)
print(popped_item)

new_popped_item = mylist.pop(3)
print(mylist)
print(new_popped_item)
print('')

mylist1 = [0,1,3]
mylist2 = [3,4,5]
mylist3 = [6,7,8]

mega_list = [mylist1, mylist2, mylist3]
print(mega_list)
print(len(mega_list))
print(mega_list[2][1])
