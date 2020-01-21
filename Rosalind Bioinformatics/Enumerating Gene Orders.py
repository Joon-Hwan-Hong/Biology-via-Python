# Sample Dataset: 3
# Sample Output:
# 6, 1 2 3, 1 3 2, 2 1 3, 2 3 1, 3 1 2, 3 2 1

# imported libraries
import math
from itertools import permutations

# code
input_digit = int(input("input permutation integer here: "))

# n! is always the permutation possibility on condition that each value is unique
total_combination = math.factorial(input_digit)

# empty list to use itertools permutation library
num_to_n = list()
for index in range(1, input_digit+1):
    num_to_n.append(index)

# determine permutation possibilities
permutations_generated = permutations(num_to_n)

# printing results
# print total number
print(total_combination)
for permutation in list(permutations_generated):
    prin_string = ""
    for number in permutation:
        prin_string += str(number) + " "
    print(prin_string)


