import tables
import variables

def printMNT():
    print("\nMNT:")
    for key in tables.MNT:
        print(f"{key}\t({tables.MNT[key][0]}, {tables.MNT[key][1]})")

def printMAT():
    print("\nMAT:")
    for value in tables.MAT:
        print(f"({value[0]}, {value[1]})")

def printMDT():
    print("\nMDT:")
    for line in tables.MDT:
        print(line)

def printMATDICT():
    print("\nMATDICT:")
    for line in tables.MAT_DICT:
        print(line)

def printAssemblyCode():
    print("\nAssembly code:")
    print(variables.assemblyCode)
