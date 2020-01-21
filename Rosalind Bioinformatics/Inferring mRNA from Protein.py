# background context for myself to remember since i learned this in class
# basically protein is degenerate, multiple possibilities of mRNA sequences for the same protein

# Sample Dataset: MA
# Sample Output: 12 ( as M = AUG, A = 4 possibilities, STOP = 3 possibilities, 1x3x4 = 12)


def mrna_infer(protein_str):
    """
    Given a string with protein sequences, return total # of different RNA strings from
    which the protein could have been translated, modulo 1 000 000.
    :param protein_str: string of Capital letters representing protein
    :return: total number of different RNA strings it can produce due to degeneracy
    """
    # important to note degeneracy value of 1 actually means only single possibility
    num_degenerate_combos = 1
    for protein_selected in protein_str:
        # determine how many different possible mRNA sequence there can be for each letter
        corresponding_degeneracy_val = values_of_degeneracy[protein_selected]
        # multiply current possible values by the degeneracy combination value
        num_degenerate_combos *= corresponding_degeneracy_val

    # n * 3 due to 3 stop codon choices
    return (num_degenerate_combos * 3) % 1000000


# how many different 3 rna sequences each letters can result in
values_of_degeneracy = {'A': 4, 'C': 2, 'D': 2, 'E': 2,
                        'F': 2, 'G': 4, 'H': 2, 'I': 3,
                        'K': 2, 'L': 6, 'M': 1, 'N': 2,
                        'P': 4, 'Q': 2, 'R': 6, 'S': 6,
                        'T': 4, 'V': 4, 'W': 1, 'Y': 2}

protein_string = input("input protein string here: ")
print(mrna_infer(protein_string))
