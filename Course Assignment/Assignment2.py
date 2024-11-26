## Assignment 2 
## Mohamed Lamin Walon-Jalloh 50706

## To write a function that output the truth table for any number of input using AND or OR logical gates

from itertools import product 
## this python package allows us to iterate over this array [0,1] as many times as we want using the input as the times we want it to iterate for.


def truthTable(num_of_gates, num_of_input):
    num_of_gates = num_of_gates.upper()
    if(num_of_gates not in ['AND', 'OR']):
        raise ValueError('This is not a valid gate option')
    
    print(f'The truth table for a {num_of_input} input logical system')
    combination = list(product([0,1], repeat=num_of_input))

    for input in combination:
        if num_of_gates == 'AND':
            result = all(input)
        else:
            result = any(input)
         
        format_Str = ' | '.join(map(str, input))
        print(f'{format_Str} | {int(result)}')    


print('Welcome to my Truth Table generators \n')

truthTable('AND',3)    

                