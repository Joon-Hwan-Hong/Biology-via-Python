# Sample Dataset: AUGGCCAUGGCGCCCAGAACUGAGAUCAAUAGUACCCGUAUUAACGGGUGA
# Sample Output: MAMAPRTEINSTRING

# im just going to brute force this

# function


def rna_to_protein_generator(mrna):
    """
    Given an RNA string s, return protein encoded by s based on the 3 codon results.
    Stop on stop codons and assume start on AUG
    :param mrna: string that is the mRNA sequence
    :return: string protein_string, which is the sequence of amino acids abbreviated to 1 letter.
    """
    # ini variable
    protein_string = ""

    # start at 0, until len(mrna), count by 3 basis
    for index in range(0, len(mrna), 3):
        # look at 3 mRNA sequence from index to index+3, which are the 3 to make a codon, look up recognized values
        corresponding_protein = table_for_translation[mrna[index:index + 3]]
        # if stop codon sequence, end iterating through the mRNA
        if corresponding_protein is "STOP":
            break

        # summation of all codons
        protein_string += corresponding_protein

    return protein_string


# ini variables
table_for_translation = {
    'UUU': 'F', 'CUU': 'L', 'AUU': 'I', 'GUU': 'V',
    'UUC': 'F', 'CUC': 'L', 'AUC': 'I', 'GUC': 'V',
    'UUA': 'L', 'CUA': 'L', 'AUA': 'I', 'GUA': 'V',
    'UUG': 'L', 'CUG': 'L', 'AUG': 'M', 'GUG': 'V',
    'UCU': 'S', 'CCU': 'P', 'ACU': 'T', 'GCU': 'A',
    'UCC': 'S', 'CCC': 'P', 'ACC': 'T', 'GCC': 'A',
    'UCA': 'S', 'CCA': 'P', 'ACA': 'T', 'GCA': 'A',
    'UCG': 'S', 'CCG': 'P', 'ACG': 'T', 'GCG': 'A',
    'UAU': 'Y', 'CAU': 'H', 'AAU': 'N', 'GAU': 'D',
    'UAC': 'Y', 'CAC': 'H', 'AAC': 'N', 'GAC': 'D',
    'UAA': 'STOP', 'CAA': 'Q', 'AAA': 'K', 'GAA': 'E',
    'UAG': 'STOP', 'CAG': 'Q', 'AAG': 'K', 'GAG': 'E',
    'UGU': 'C', 'CGU': 'R', 'AGU': 'S', 'GGU': 'G',
    'UGC': 'C', 'CGC': 'R', 'AGC': 'S', 'GGC': 'G',
    'UGA': 'STOP', 'CGA': 'R', 'AGA': 'R', 'GGA': 'G',
    'UGG': 'W', 'CGG': 'R', 'AGG': 'R', 'GGG': 'G'}

# code
mrna_input = input("insert RNA string here: ")
print(rna_to_protein_generator(mrna_input))
