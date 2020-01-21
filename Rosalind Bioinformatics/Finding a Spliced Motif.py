# http://rosalind.info/problems/sseq/


def main():
    from Bio import SeqIO

    strings, result = [], ""
    fasta_sequences = SeqIO.parse(open(f"{input('file name here: ')}.txt"), 'fasta')
    for fasta in fasta_sequences:
        strings.append(str(fasta.seq))

    start = 0
    for subsequence_pointer in strings[1]:
        for index, character in enumerate(strings[0]):
            # I am  aware that I could instead enumerate(strings[0][start]) and
            # modify start, updating to each index everytime, much cost efficient too
            if (subsequence_pointer is character) and (index > start):
                result += str(index + 1) + " "
                start = index
                break

    print(result)


if __name__ == '__main__':
    main()
