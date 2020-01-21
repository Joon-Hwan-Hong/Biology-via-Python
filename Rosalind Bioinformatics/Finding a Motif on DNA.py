# Sample Dataset:
# GATATATGCATATACTT
# ATAT
# Sample Output: 2 4 10

main_string = input("DNA String S here: ")
sub_string = input("DNA String t here: ")
printing_result = ""

for index in range(0, len(main_string)):
    # stops when length of substring is longer than the main string, in other words no more instance of substr
    if (index + 3) < len(main_string)\
            and main_string[index:index+len(sub_string)] == sub_string:
        # + 1 to index because index starts at 0, while location begins at 1.
        printing_result += str(index + 1) + " "

# result
print(printing_result)
