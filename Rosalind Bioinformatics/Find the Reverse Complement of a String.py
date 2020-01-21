def main():
    # im just going to do use bio library,
    # from previous rosalind questions I already have tools to do this too.
    with open('rosalind_ba1c.txt', 'r') as file:
        dna = file.readline().rstrip()

    sequence = Seq.reverse_complement(dna)
    print(sequence)
    return sequence


if __name__ == '__main__':
    # does it matter if i import in this or in main()? dont know tbh
    from Bio import Seq
    main()
