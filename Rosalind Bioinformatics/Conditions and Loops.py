def main():
    # given two integers a and b, return sum of all integers from a through b inclusively
    with open("rosalind_ini4.txt", "r") as file:
        # obtain list containing the two numbers
        number = list(map(int, file.readline().rstrip().split()))

    answer = 0
    for index in range(number[0], number[1], 2):
        # answer is the sigma(i from a to b)
        answer += index

    print(answer)
    return answer


if __name__ == '__main__':
    main()
