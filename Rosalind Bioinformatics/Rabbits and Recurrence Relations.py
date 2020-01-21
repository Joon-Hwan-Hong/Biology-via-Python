# Sample Dataset: 5 3
# Sample Output: 19

#function


def rabbits_and_recurrence_relations(months, birthed_pairs):
    """
    total number of pairs present after n sequence iterations recursively.
    :param months: number of months, n <= 40
    :param birthed_pairs: rabbit pairs, k <= 5
    :return: total # of rabbit pairs present after n months. (int)
    """
    # Base cases
    if months is 1:
        return 1
    elif months is 2:
        return birthed_pairs

    # fibbonacci sequence thing to follow: F(n) = F(n-1) + F(n-2)
    oneGeneration = rabbits_and_recurrence_relations(months - 1, birthed_pairs)
    secondGeneration = rabbits_and_recurrence_relations(months - 2, birthed_pairs)

    # upto 4 generations, can be added up here by rabbit polpulation 1 and 2 gen ago.
    if months <= 4:
        return oneGeneration + secondGeneration

    # beyond that, should be done this way,
    return oneGeneration + (secondGeneration * birthed_pairs)


# code
input_month = int(input("input n here: "))
input_rabbits = int(input("input k here: "))
print(rabbits_and_recurrence_relations(input_month, input_rabbits))
