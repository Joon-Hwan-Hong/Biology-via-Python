def recursive_combinations(chars, size, combination='', result=[]):
    """
    a recursive solution to finding all combinations, since the given character list is already in
    increasing order, can just do a for loop to always create string1 < string2
    :param chars: list of characters where item(n) < item(n+1)
    :param size: the length of the permutation needed
    :param combination: initially empty, but continually append characters as continues, this will be combination
    :param result: list which will be returned, containing all combinations
    :return: returns result (list of permutations)
    """
    # base case, when there is no more "length" to continue, append the total concatenated combination
    if size is 0:
        result.append(combination)
    else:
        # important to note that for each recursive call(!) this loop will begin again
        for character in chars:
            recursive_combinations(chars, size - 1, combination + character, result)

    return result


def main():
    with open('rosalind_lexf.txt', 'r') as file:
        # obtain list of characters, and the size of each permutation
        characters = file.readline().rstrip().split()
        string_size = int(file.readline().rstrip())

    # determine list of combinations recursively, iterate through
    for combination in recursive_combinations(characters, string_size):
        print(combination)


if __name__ == '__main__':
    main()
