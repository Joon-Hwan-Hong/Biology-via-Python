class KmpSearch:

    def __init__(self, string):
        # initialization, failure array set up
        self.string = string
        self.failure_array = [0] * len(string)

    def run(self):
        pos_from_cand = 0
        for position in range(2, len(self.string) + 1):

            # condition for the change of position from candidate viewed
            while pos_from_cand > 0 and self.string[pos_from_cand] != self.string[position - 1]:
                pos_from_cand = self.failure_array[pos_from_cand - 1]

            # change of the position away from candidate once the told condition form rosalind
            if self.string[pos_from_cand] == self.string[position - 1]:
                pos_from_cand += 1

            self.failure_array[position - 1] = pos_from_cand

        # rosalind does not accept the list input, so converting it to a string
        answer = ''
        for number in self.failure_array:
            answer += str(number) + ' '
        print(answer)

        # ans
        return answer


def fasta_to_string():
    """
    obtain string from second line of text file.
    text file must be in same directory as .py file.
    :return: string representing dna sequence
    """
    with open('rosalind_kmp.txt', 'r') as file:
        file.readline()
        dna_string = ''

        # iterate through, concatenate string
        for line in file:
            line = line.replace("\n", "")
            dna_string += line.strip()

        # ans
        return dna_string


def main():
    input_string = fasta_to_string()
    search = KmpSearch(input_string)
    search.run()


if __name__ == '__main__':
    main()
