# Learning about List in python and all the operation that can be done with and on them.

mylist = [1,2,3,4,5,6,7,8,9]

# Accessing element in the list using indexing
print(mylist[2])
print(mylist[-1])

# Slicing a listing
print(mylist[1:5])
print(mylist[2:4])

#reversing a list or accessing the element in a list
print(mylist[::-3])
print(mylist[1:2:8])

# changing elements in a list
mylist[4] = True
print(mylist)

# adding item to a list
mylist.append(70) # add to end of the list
mylist.append('Walon')
print(mylist)

mylist.insert(2,'Walon') # add element to the specified index
print(mylist)

#Removing elements from a list
mylist.remove('Walon')
print(mylist)

mylist.pop(2)
print(mylist)

#using for loop to add 5 to element in  a  list
newlist = []
mylist2 = [1,2,3,4,5]
for i in mylist2:
    result = i + 5
    newlist.append(result)

print(newlist)

# using the map function to add 10 to element in a list

def add_ten(num):
    return num + 10

added_list = list(map(add_ten,mylist2))
print(added_list)