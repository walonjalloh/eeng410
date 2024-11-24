# in this classwork we wrote a function that prints out the truth table for boolean AND and OR gates
from itertools import product

#itertool can iterate over any array to give all the possible outcomes..

def truthtable(gate_type, inputs):
    gate_type = gate_type.upper()
    if gate_type not in ['AND', 'OR']:
        raise ValueError("Incorrect gate type!!!")
    

    print(f"{'A':<5}{'B':<5}{'A AND B':<10}{'A OR B':<10}")
    print("-" * 30)
    combination = list(product([0,1], repeat=inputs))
    for input in combination:
        if gate_type == 'AND':
            result = all(input)
        elif gate_type == 'OR':
            result = any(input) 
        else:
            print('gate error')

        format_str = ''.join(map(str,input))     
        print(f'{format_str} | {int(result)}')       
    
truthtable('OR',6)    
