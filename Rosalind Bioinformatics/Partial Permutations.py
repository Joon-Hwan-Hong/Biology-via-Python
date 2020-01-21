class PartialPermutation:
    """
    when printed, if returned 0. error. finds partial permutation.
    """
    def __init__(self, n, k):
        assert((n >= 1) and (k >= 1))

        self.int1 = n
        self.int2 = k

    def __str__(self):
        return f"{self.solve(self.int1, self.int2) % 1000000}"

    def solve(self, integer1, integer2):
        if integer2 is 1:
            return integer1
        return self.solve(integer1 - 1, integer2 - 1) * integer1


def main():
    """
    given positive integers n and k such that 0-n-100, and 0-k-10
    return the total number of partial permutations % 1000000
    :return: The total number of partial permutations P(n,k), modulo 1,000,000.
    """
    with open("rosalind_pper.txt", "r") as file:
        integers = list(map(int, file.readline().rstrip().split()))

    print(integers)
    print(PartialPermutation(integers[0], integers[1]))


if __name__ == '__main__':
    main()
