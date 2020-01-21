# Sample Dataset: SKADYEK
# Sample Output: 821.392


def protein_mass_calculator(protein_string):
    """
    Given a string with capital letters representing proteins, determine its total mass. Iterates
    through string and visits dictionary with assigned weight values to sum up total mass.
    :param protein_string: String P with length n
    :return: total weight of protein string, with monoisopotic mass table given.
    """
    # ini variables
    protein_mass = 0
    monoisopotic_mass_table = {
        "A": 71.03711, "C": 103.00919, "D": 115.02694,
        "E": 129.04259, "F": 147.06841, "G": 57.02146,
        "H": 137.05891, "I": 113.08406, "K": 128.09496,
        "L": 113.08406, "M": 131.04049, "N": 114.04293,
        "P": 97.05276, "Q": 128.05858, "R": 156.10111,
        "S": 87.03203, "T": 101.04768, "V": 99.06841,
        "W": 186.07931, "Y": 163.06333}

    # iterate through protein string given, sum corresponding character mass.
    for protein_character in protein_string:
        protein_mass += monoisopotic_mass_table[protein_character]

    return protein_mass


print(protein_mass_calculator(input("input protein string P here: ")))
