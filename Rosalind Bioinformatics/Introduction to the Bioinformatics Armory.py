
def main():
    from Bio.Seq import Seq
    dna = Seq(input("input dna here: "))
    print(''.join(
        str(dna.count("A")) + " " +
        str(dna.count("C")) + " " +
        str(dna.count("G")) + " " +
        str(dna.count("T")) + " "))



if __name__ == '__main__':
    main()