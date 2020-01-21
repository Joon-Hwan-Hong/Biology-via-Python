# using already created .py files and their functions.
# given a DNA string, and collection of substrings as introns, return a protein string from
# transcribing and translating the exons of string

# so since i have already developed "Transcribing DNA to RNA.py" and "Translating RNA into Protein.py"
# ill just reuse them! I have read somewhere that functions should be defined outside main(), so trying that


def intron_finder(file_readlines):
    """
    iterates through FASTA file, ignoring first gene string, continually append intron strings into
    returning list. then return list containing all strings representing introns
    :param file_readlines: file.readlines
    :return: list containing all strings representing introns.
    """
    # flag when second ">" begins, indicating list of introns from there
    intron_begins_index = 1
    for lines in file_readlines[1:]:
        if lines[0] is not ">":
            intron_begins_index += 1
        else:
            break

    # now iterate through starting where introns begin + 1, to avoid the first ">", continually append introns
    list_introns = []
    intron_string = ""
    for lines2 in file_readlines[intron_begins_index + 1:]:
        if lines2[0] is not ">":
            # concatenate cleaned string without \n
            intron_string += lines2.rstrip("\n\r")
        else:
            list_introns.append(intron_string)
            intron_string = ""

        # edge case on last intron gene sequence
        if lines2 == file_readlines[len(file_readlines) - 1]:
            list_introns.append(intron_string)

    return list_introns


def splice_string(dna_string, list_introns):
    for intron in list_introns:
        dna_string = dna_string.replace(intron, '')
    return dna_string


def dna_to_rna(cleaned_dna_string):
    """
    uses .py module in DNA to RNA previously made due to past ROSALIND task.
    :param cleaned_dna_string: dna_string
    :return: RNA_string
    """
    # TODO Because im a dumb fuck and didnt expect to reuse, and too lazy to go back
    #     and edit the old python file, have to copy and paste instead of doing automatically.
    #     maybe do this later.
    import importlib

    # copy and paste this string into "input string here: "
    print(cleaned_dna_string)
    RNA_string = importlib.import_module("Transcribing DNA into RNA")

    return RNA_string


def rna_to_protein(rna_string):
    """
    uses .py module in DNA to RNA previously made due to past ROSALIND task.
    :param cleaned_dna_string: dna_string
    :return: RNA_string
    """
    # TODO Because im a dumb fuck and didnt expect to reuse, and too lazy to go back
    #     and edit the old python file, have to copy and paste instead of doing automatically.
    #     maybe do this later.
    import importlib

    # copy and paste this string into "input string here: "
    print(rna_string)
    Protein_string = importlib.import_module("Translating RNA into Protein")

    return Protein_string


def find_dna_string(file_lines):
    """
    continually concatenates file lines until next ">" is detected, which indicates
    end of DNA sequence and beginning of substrings acting as introns.
    :param file_lines: file.readlines() of whatever file name was inputted.
    :return: DNA_string, s
    """
    # find DNA string
    DNA_String = ""
    for line in file_lines[1:]:
        if line[0] is not ">":
            clean_line = line.rstrip("\n\r")
            DNA_String += clean_line
        else:
            break

    return DNA_String


def main():
    # open file and readlines:
    file_lines = open(f"{input('input text name here: (need same domain)')}.txt", "r").readlines()

    # determine DNA String
    DNA_string = find_dna_string(file_lines)

    # creates list of introns
    intron_list = intron_finder(file_lines)

    # splice out any introns from intron list, viewing DNA string
    exon_string = splice_string(DNA_string, intron_list)

    # convert exon_strong to rna
    RNA_converted_string = dna_to_rna(exon_string)

    # convert rna string to protein string
    rna_to_protein(RNA_converted_string)


if __name__ == "__main__":
    main()
