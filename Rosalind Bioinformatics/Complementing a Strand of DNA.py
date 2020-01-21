# Sample Dataset: AAAACCCGGT
# Expected Output: ACCGGGTTTT

# Functions


def complementing_a_strand_of_dna(dna_string):
    """
    given a string of sequences of nucleotides, return the reverse complimentary string
    :param dna_string: string of length n
    :return: reverse complimentary string of n
    """
    # ini variables
    temp_list, reverse_complimentary_list = [], []

    # lol this is incredibly inefficient, maybe look back into this later. change string to list then reverse list.
    for nucleotide in dna_string:
        temp_list.append(nucleotide)
    temp_list.reverse()

    # add complimentary strand to a list to return, else is only reached if character is G
    for nucleotide2 in temp_list:
        if nucleotide2 is "A":
            reverse_complimentary_list.append("T")
        elif nucleotide2 is "T":
            reverse_complimentary_list.append("A")
        elif nucleotide2 is "C":
            reverse_complimentary_list.append("G")
        else:
            reverse_complimentary_list.append("C")

    # list to string
    complimentary_string = ''.join(reverse_complimentary_list)

    return complimentary_string


# code
input_string = input("input dna string here ")
print(complementing_a_strand_of_dna(input_string))
