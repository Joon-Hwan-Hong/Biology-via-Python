def main():
    # rounded values to 4 decimal places as it appears to work that way
    mass_table = {'A': 71.0371,  'C': 103.0092, 'D': 115.0269, 'E': 129.0426, 'F': 147.0684,
                  'G': 57.0215,  'H': 137.0589, 'I': 113.0841, 'K': 128.0950, 'L': 113.0841,
                  'M': 131.0405, 'N': 114.0429, 'P': 97.0528,  'Q': 128.0586, 'R': 156.1011,
                  'S': 87.0320,  'T': 101.0477, 'V': 99.0684,  'W': 186.0793, 'Y': 163.0633}

    # inverted table for use in matching according to mass spec values
    inverted_table = {value: key for key, value in mass_table.items()}

    # obtain list of all values given in text file
    with open('rosalind_spec.txt', 'r') as file:
        L_list = [float(line) for line in file]

    # collect list of amino acid masses; mass(n+1) - mass(n) = aa_mass of n
    aa_masses = []
    for index in range(len(L_list) - 1):
        aa_mass = round(L_list[index + 1] - L_list[index], 4)
        aa_masses.append(aa_mass)

    # deduce which protein it is from looking at each mass and dictionary
    protein_string = ''
    for amino_acid_mass in aa_masses:
        protein_string += inverted_table[amino_acid_mass]

    # ans
    print(protein_string)


if __name__ == '__main__':
    main()
