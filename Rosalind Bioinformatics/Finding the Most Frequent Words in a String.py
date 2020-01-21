def main():
    # open and obtain needed values, dna string and k-value for k-mer
    with open('rosalind_ba1b.txt', 'r') as file:
        dna = file.readline()
        k_val = int(file.readline())

    # ini dictionary to keep track of frequency of substring occurance
    frequency = dict()
    for position in range(len(dna)):
        k_mer = dna[position: position + k_val]
        # if already exists, add 1, else initialize with 1
        if k_mer in frequency:
            frequency[k_mer] += 1
        else:
            frequency[k_mer] = 1

    # iterate through in list comprehension, if value of key is the max in dictionary append to list
    final = list(key for key, value in frequency.items()
                 if value is max(frequency.values()))

    # concatenate all highest frequency k-mer to string
    answer = ''
    for mer in final:
        answer += f'{mer} '

    # result
    print(answer)
    return answer


if __name__ == '__main__':
    main()
