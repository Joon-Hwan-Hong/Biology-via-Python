# put all words into a list
words = open("rosalind_ini6.txt", 'r')\
    .readline()\
    .rstrip()\
    .split()

# make dictionary to keep track of frequency of words occuring
frequency = dict()
# iterate through items in list containing all words
for word in words:
    # if already in before, add 1, else create one
    if word in frequency:
        frequency[word] += 1
    else:
        frequency[word] = 1

# print using f string
for key, value in frequency.items():
    print(f"{key} {value}")
