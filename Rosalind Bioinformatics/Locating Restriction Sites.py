# Given: A DNA string of length at most 1 kbp in FASTA format.
# Return: The position and length of every reverse palindrome in the string having length between 4 and 12.


def main():
    """
    Returns all position and length of every reverse palindrome in the string having
    length between 4 and 12. A string sequence is a reverse palindrome if the reverse
    compliment is equivalent to itself. (position begins at 1)
    :return: nothing. Position Length of reverse palindromes are printed
    """
    # import SeqIO for parsing FASTA file
    # import Seq to determine reverse complimentary strands
    from Bio import SeqIO as SeqIO
    from Bio import Seq

    # open FASTA file and obtain string - representing DNA sequence.
    fasta_sequence = SeqIO.parse(open(f"{input('file name here: ')}.txt"), 'fasta')
    for fasta in fasta_sequence:
        sequence = fasta.seq

    # determines length of search inside the total DNA sequence
    for length in range(12, 3, -2):

        # determines where within the sequence to view
        for index in range(len(sequence)):

            # checks to prevent searching index beyond the length of sequence
            if (index + length) < len(sequence) + 1:

                # generates sequence with given length, and create reverse complimentary
                possible_palindrome = sequence[index: index + length]
                reverse_comoplimentary = Seq.reverse_complement(possible_palindrome)

                # definition of reverse palindrome: sequence == reverse complimentary
                if possible_palindrome == reverse_comoplimentary:
                    print(str(index + 1) + f" {length}")


if __name__ == '__main__':
    main()
