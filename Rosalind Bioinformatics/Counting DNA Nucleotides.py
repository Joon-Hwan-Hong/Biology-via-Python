# sample Dataset
# AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC
# expected output: 20 12 17 21

# functions


def counting_dna_nucleotides(input_string):
    """
    Counts nucleotide frequency in string representing DNA sequence
    :param input_string: A DNA string s of length at length n
    :return: four integers, separated by spaces, counting the respective # of nucleotides in s
    """
    # initializing while loop index, and nucleotide(ACGT)count
    index, a_i, c_i, g_i, t_i = 0, 0, 0, 0, 0

    # pretty high complexity but oh well, not an issue atm, could also use for loop
    while index < len(input_string):
        if input_string[index] is "A":
            a_i += 1
        elif input_string[index] is "C":
            c_i += 1
        elif input_string[index] is "G":
            g_i += 1
        elif input_string[index] is "T":
            t_i += 1
        index += 1

    # now change nucleotide_index to strings to return, can be done in one line in return but for clarity
    a_val = str(a_i) + " "
    c_val = str(c_i) + " "
    g_val = str(g_i) + " "
    t_val = str(t_i)

    return a_val + c_val + g_val + t_val


# run
input_String = input("copy/type input String here: ")
print(counting_dna_nucleotides(input_String))
