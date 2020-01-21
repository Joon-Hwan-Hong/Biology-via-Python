class Count:
    # initialize, default instance of 0 to begin with
    def __init__(self, text, pattern, instance=0):
        self.text = text
        self.pattern = pattern
        self.instances = instance

    # iterate through string, if substring == pattern, increase counter/ instance
    def __str__(self):
        for index in range(len(self.text) - len(self.pattern) + 1):
            if self.text[index: index + len(self.pattern)] == self.pattern:
                self.instances += 1
        return str(self.instances)


def main():
    # read file then close after obtaining text and pattern to search for
    with open('rosalind_ba1a.txt', 'r') as file:
        text = file.readline().rstrip()
        pattern = file.readline().rstrip()
    # determine answer then print
    answer = Count(text, pattern)
    print(answer)
    # return for potential future use
    return answer


if __name__ == '__main__':
    main()
