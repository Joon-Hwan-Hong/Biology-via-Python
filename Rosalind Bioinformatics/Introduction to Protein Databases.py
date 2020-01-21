def main():
    from Bio import ExPASy
    from Bio import SwissProt

    ID = input("input id here: ")
    handle = ExPASy.get_sprot_raw(ID)
    record = SwissProt.read(handle)
    biological_processes = []

    for processes in record.cross_references:
        if processes[0] == "GO" and processes[2][0] == "P":
            biological_processes.append(processes[2].lstrip("P:"))

    answer = "\n".join(biological_processes)
    print("*"*50)
    print(answer)
    return answer


if __name__ == '__main__':
    main()
