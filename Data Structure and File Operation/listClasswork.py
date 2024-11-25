# calculating the resistance for resistors in parallel
# formula (1/R1 + 1/R2 + 1/Rn) ** -1

def calculate_parallel_resistance(resistor):
    total_sum = sum(1/r for r in resistor)
    return  1/total_sum


resistor = [1,2,3]
total_parallel_resistance = calculate_parallel_resistance(resistor)

print(f'total resistance = {total_parallel_resistance} ohms')