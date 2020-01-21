from Bio import SeqIO as Seq


def main():
    # ini variables
    dnas = []
    answer = ''

    # open and sequence the dna strings
    with open('rosalind_lcsm.txt', 'r') as file:
        fasta_sequences = Seq.parse(file, 'fasta')
        for fasta in fasta_sequences:
            dna = str(fasta.seq)
            dnas.append(dna)

    # sort the list, lowest value is smallest one, else needs to be compared
    sorted_list = sorted(dnas, key=len)
    short_seq = sorted_list[0]
    compare_seq = sorted_list[1:]

    # this is like O(n^3) lol, pretty much brute forcing it but it works!
    for index in range(len(short_seq)):
        # only need to look at combinations in the smallest sequence first
        for jndex in range(index, len(short_seq)):
            candidate = short_seq[index:jndex + 1]
            # with the potential candidate for longest substring, check if in other sequences
            for sequence in compare_seq:
                if (candidate in sequence) and (len(candidate) > len(answer)):
                    answer = candidate
                else:
                    break
    # ans
    print(answer)
    return answer


if __name__ == '__main__':
    smol_boi_across_all_strings = main()
