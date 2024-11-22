# in the lectures we learnt about function and how they save developers a lot of time

#simple addition function
def add(num1,num2):
    return num1 + num2

total = add(2,3)
print(total)

# a greeeting funtion
def sayHelloWithName(name):
    return print(f'hello {name}')

sayHelloWithName('walon')

print('*' * 20)



def guess():
    max_guess = 7 
    tries = 0
    guessed_value = 7

    while tries < max_guess:
        number = int(input('Guess the number: '))
        if(number == guessed_value):
            print('correct')
            break
        else:
            print('wrong ')
            continue
    tries += 1
               
guess()


def bool(num):
    value = 0
    while num != value:
        print('| A | | B | | C |')
    value +=1


bool(3)

