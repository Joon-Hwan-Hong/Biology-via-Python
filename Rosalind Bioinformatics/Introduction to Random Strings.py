def main():

    # used for logarithm function
    import math

    # obtain needed strings
    with open('rosalind_prob.txt', 'r') as file:
        dna_string = file.readline().rstrip()
        floats = list(map(float, file.readline().rstrip().split()))

    # ini variables
    probabilities = []
    at_count = 0
    gc_count = 0

    # determine GC and AT count
    for character in dna_string:
        if (character is 'A') or (character is 'T'):
            at_count += 1
        if (character is 'G') or (character is 'C'):
            gc_count += 1

    # determine logged probability value
    for value in floats:
        prob = math.log10((((1 - value) / 2) ** at_count) * (value / 2) ** gc_count)
        # rounds to 3 decimal places
        probabilities.append('%0.3f' % prob)

    # print iterations in probabilities with separations as spaces
    print(*probabilities, sep=' ')


if __name__ == '__main__':
    main()
