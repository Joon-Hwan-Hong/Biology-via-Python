# put all lines into list
text = open("rosalind_ini5.txt", "r").readlines()

# if even, %2 = 0 and print. else continue
even_check = 1
for line in text:
    if even_check % 2 is 0:
        print(line.rstrip())
    even_check += 1
