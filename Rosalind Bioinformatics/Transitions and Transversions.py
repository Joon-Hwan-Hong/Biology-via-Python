# I learned about:        with ________ as ____:       today, lets try it!


def main():
    # import to sequence fasta file
    from Bio import SeqIO

    # opens file and extracts dna sequences
    with open('rosalind_tran.txt', 'r') as file:
        fasta_file = SeqIO.parse(file, 'fasta')
        container = []
        for fasta in fasta_file:
            sequence = str(fasta.seq)
            container.append(sequence)

    # ini objects & variables. initialize counters, and create lists of possible combinations
    transitions = ["AG", "GA", "CT", "TC"]
    transversions = ["AC", "CA", "GT", "TG", "AT", "TA", "GC", "CG"]
    transitions_count = transversions_count = 0

    # iterate through sequences
    for index in range(len(sequence)):
        dna1 = container[0][index]
        dna2 = container[1][index]
        # if sequences are the same, next iteration in sequences
        if dna1 == dna2:
            continue
        # if concatenated string is in either posibility list, add to counter
        elif dna1 + dna2 in transitions:
            transitions_count += 1
        elif dna1 + dna2 in transversions:
            transversions_count += 1

    # basic math for ratio
    transition_transversion_ratio = transitions_count / transversions_count

    # result
    print(transition_transversion_ratio)
    return transition_transversion_ratio


if __name__ == '__main__':
    main()
