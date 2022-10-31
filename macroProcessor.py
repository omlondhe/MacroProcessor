# Roll No: 321091
# GR No: 22120276
# Name: Om Prashant Londhe

from io import TextIOWrapper
from macroHandler import handleMacro
from utils import printMAT, printMDT, printMNT
from variables import intermediateCode


with open('./input.txt', 'r') as script:
    # reading the script
    code: str = script.read()
    # getting instruction list
    instructions: list[str] = code.split('\n')
    numberOfInstructions: int = instructions.__len__()
    # defining the output file
    outputFile: TextIOWrapper = open('output.txt', 'w')

    handleMacro(instructions)

    printMNT()
    printMAT()
    printMDT()
