# learned a bit about Biopython online, trying out, lol its way better than previously doing all manually


def main():
    from Bio import SeqIO as seq
    from Bio.SeqUtils import GC

    # initialize values
    fasta_ID, highest = "", 0
    fasta_sequences = seq.parse(open(f"{input('file name here: ')}.txt"), 'fasta')

    # iterate through gene sequences with their respective id, if their gc content is higher then
    # the previous max, it becomes the new max
    for fasta in fasta_sequences:
        name, sequence = fasta.id,  str(fasta.seq)
        gc_content = GC(sequence)
        if gc_content > highest:
            highest = gc_content
            fasta_ID = name

    print(f"{fasta_ID} \n{highest}")


if __name__ == '__main__':
    main()
