# we also learnt about loops that is for, while,do-while and others


#trying to iterate over the characters of any given name
name = input('Enter your name: ')

number = [1,2,3,4,5,6,7,8,9,10]

for i in name :
    print(i)


#getting the total sum using for loops
total_number =  0
for i  in range(0,12):
    total_number += i

print(total_number)


#geting total sum using python sum properties
total = sum(number)
print(total)