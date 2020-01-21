# Sample Dataset: GATGGAACTTGACTACGTAAATT
# Expected output: GAUGGAACUUGACUACGUAAAUU

# functions


def transcribing_dna_into_rna(dna_string):
    """
    given a string with sequence consisting of ATGC, convert all T with U
    :param dna_string: a string having length n
    :return: new string with all T changed to U
    """
    # ini values, lets use for loops this time
    rna_string = ""

    # iterate through dna string, if T add U instead, if else just keep adding to return(rna string)
    for nucleotide in dna_string:
        if nucleotide is "T":
            rna_string += "U"
        else:
            rna_string += nucleotide

    return rna_string


# code
input_string = input('Input string here: ')
print(transcribing_dna_into_rna(input_string))
