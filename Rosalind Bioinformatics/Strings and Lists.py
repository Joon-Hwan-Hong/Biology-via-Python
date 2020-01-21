def main():
    with open("rosalind_ini3.txt", "r") as file:
        # string containing letters
        string = file\
            .readline()\
            .rstrip()
        # four coordinates to splice string, maps them w/ integers, returns list
        positions = list(map(int, file.readline().rstrip().split()))

    answer = string[positions[0]:positions[1] + 1] + " " + string[positions[2]:positions[3] + 1]
    print(answer)
    return answer


if __name__ == '__main__':
    main()
