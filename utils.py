from tables import MAT, MDT, MNT


def printMNT():
    print("\nMNT:")
    for key in MNT:
        print(f"{key}\t({MNT[key][0]}, {MNT[key][1]})")

def printMAT():
    print("\nMAT:")
    for value in MAT:
        print(f"({value[0]}, {value[1]})")

def printMDT():
    print("\nMDT:")
    for line in MDT:
        print(line)

