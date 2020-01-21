# Sample Dataset: FASTA format of at most 10 DNA strings
# return a consensus string and profile matrix for the collection


def main():
    import numpy as np

    ini_list = []
    # type in textfile name, and opens text file
    textfile_name = input("input textfile name here: (have to be on same directoy as .py)")
    FASTA_string = open(f"{textfile_name}.txt", "r")

    # assign variable to iterable and iterate through lines
    lines = FASTA_string.readlines()
    lines.pop(0)
    gene_string = ""
    for line in lines:
        # removes all gene tags (which start with '>'), and adds collected gene_string
        if line[0] is ">":
            ini_list.append(gene_string)
            gene_string = ""
        # collects gene string as they can span multiple lines
        else:
            clean_line = line.rstrip("\n\r")
            gene_string += clean_line

        # edge case where the last DNA sequence is not counted due to appending when > is present next
        if line == lines[len(lines) - 1]:
            ini_list.append(gene_string)

    # ************ convert string into matrix! ************
    ini_matrix = []
    for DNA_sequence in ini_list:
        # list comprehension to put all nucleotide into matrix
        ini_matrix.append([nucleotide for nucleotide in DNA_sequence])

    matrix = np.array(ini_matrix).reshape(len(ini_matrix), len(ini_matrix[0]))

    # character lists to put later
    A = []
    C = []
    G = []
    T = []
    final_A_string = "A: "
    final_C_string = "C: "
    final_G_string = "G: "
    final_T_string = "T: "

    # len(ini_list[0]) is the length of the list, or how many columns there are in the matrix
    for column in range(len(ini_list[0])):
        # nucleotide counts, resets every column
        a = c = g = t = 0
        for nuc_character in matrix[:, column]:
            if nuc_character == "A":
                a += 1
            if nuc_character == "C":
                c += 1
            if nuc_character == "G":
                g += 1
            if nuc_character == "T":
                t += 1
        # after iterating through column of matrix, append counts to each respective list
        A.append(a), C.append(c), G.append(g), T.append(t)

    # now make consensus string
    def return_max_character(location, matrix1, matrix2, matrix3, matrix4):
        """
        recursive solution to finding which matrix has the greatest value, is this efficient? NO!,
        there are tons of different methods that are way quicker and better.
        I wanted to practice recursion and therefore I did it this way, since im not good at it
        NEEDS comparable data types.
        :param location: index of where the matrix will compare values
        :param matrix1: a matrix
        :param matrix2: another matrix
        :param matrix3: another matrix 2
        :param matrix4: another matrix 3
        :return: matrix with largest value when comparing at index
        """
        base = matrix1[location]
        if base < matrix2[location]:
            return return_max_character(location, matrix2, matrix2, matrix3, matrix4)
        if base < matrix3[location]:
            return return_max_character(location, matrix3, matrix2, matrix3, matrix4)
        if base < matrix4[location]:
            return return_max_character(location, matrix4, matrix2, matrix3, matrix4)
        else:
            return matrix1

    # iterates through all matrices, determines which has the greatest value at given index. appends string
    consensus_string = ""
    for index in range(len(A)):
        character = return_max_character(index, A, C, G, T)
        if character == A:
            consensus_string += "A"
        if character == C:
            consensus_string += "C"
        if character == G:
            consensus_string += "G"
        if character == T:
            consensus_string += "T"

    for number in range(len(A)):
        final_A_string += f"{A[number]} "
        final_C_string += f"{C[number]} "
        final_G_string += f"{G[number]} "
        final_T_string += f"{T[number]} "

    # final output
    print(consensus_string)
    print(f"{final_A_string} \n{final_C_string} \n{final_G_string} \n{final_T_string}")


if __name__ == "__main__":
    main()
