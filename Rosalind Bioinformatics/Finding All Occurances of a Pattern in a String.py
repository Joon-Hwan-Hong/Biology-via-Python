class StringOccurance:
    # initialize with necessary information
    def __init__(self, pattern, genome):
            self.pattern = pattern
            self.patternLength = len(pattern)
            self.genome = genome
            self.genomeLength = len(genome)
            self.answer = ''

    # defines what is returned when class is printed
    def __str__(self):
        return self.answer

    # iterate through, if substring of genome == pattern, add index
    def find(self):
        for index in range(self.genomeLength):
            if (self.genome[index: index + self.patternLength] == self.pattern) \
                    and(index + self.patternLength < self.genomeLength):
                self.answer += f'{index} '


def main():

    # extract two strings needed
    with open('rosalind_ba1d.txt', 'r') as file:
        substring_pattern = file.readline().rstrip()
        total_genome = file.readline().rstrip()

    # create class, practicing OOP concepts learned today
    return_answer = StringOccurance(substring_pattern, total_genome)
    return_answer.find()
    print(return_answer)


if __name__ == '__main__':
    main()
