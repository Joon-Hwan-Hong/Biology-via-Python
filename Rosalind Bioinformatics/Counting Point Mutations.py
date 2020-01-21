# Sample dataset: GAGCCTACTAACGGGAT, CATCGTAATGACGGCCT
# Sample Output: 7

# code
input_dna1 = input("input DNA seq here: ")
input_dna2 = input("input DNA seq2 here: ")

Hamming_distance, index = 0, 0
while index < len(input_dna1):
    if not input_dna1[index] == input_dna2[index]:
        Hamming_distance += 1
    index += 1

print(Hamming_distance)


