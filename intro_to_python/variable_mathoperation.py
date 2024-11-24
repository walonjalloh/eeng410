# we learnt how to create a variable, understood data types,basic math operations and the rules in naming them

myVar = 'Walon' #string data type
myNumber = 89 # int data type
myBool = False # boolean data type
myFloat = 3.456 # float data type
myChar = 'a' # char data type

print(myVar)
print(myNumber)
print(myBool)
print(myFloat)
print(myChar)


x = 9
y = 10

myTimes  = x * y # multiplication
myAdd = x + y # adddition
mySub = y - x  #subtraction
myDivide = x / y  # divide
myFloor = x//y #floor division
myRemainder  = x % y # remainder division
mySquare = x ** 2 or y **2 # gives the square of x or y

print(myRemainder)
print(myAdd)
print(mySub)
print(myDivide)
print(myFloat)
print(myFloor)
print(mySquare)


## learnt how to use the map function in python
myList = [1,2,3,4,5,6]

def add_five(n):
    return n + 5
squared = list(map(lambda x: x**2, myList))
added_five = list(map(add_five,myList))
print(f'squared list = {squared}')
print(added_five)

