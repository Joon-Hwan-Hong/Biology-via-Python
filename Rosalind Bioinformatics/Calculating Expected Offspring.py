def main():
    # open file and obtain the number of couples in each genotype
    with open('rosalind_iev.txt', 'r') as file:
        values = [int(integer) for integer in file.readline().split()]

    # probability that the offspring will have a dominant phenotype.
    dom_prob_list = [1, 1, 1, 0.75, 0.5, 0]

    expected = 0
    for index in range(6):
        # there are 2 offsprings per parents
        expected += 2*values[index]*dom_prob_list[index]

    return expected


if __name__ == '__main__':
    print(main())
