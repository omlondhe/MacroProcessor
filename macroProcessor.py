# Roll No: 321091
# GR No: 22120276
# Name: Om Prashant Londhe

from io import TextIOWrapper
from macroExpander import expandMacros
from macroHandler import handleMacros
from utils import printAssemblyCode, printMAT, printMATDICT, printMDT, printMNT
import variables


with open('./input.txt', 'r') as script:
    # reading the script
    code: str = script.read()
    # getting instruction list
    instructions: list[str] = code.split('\n')
    numberOfInstructions: int = instructions.__len__()
    # defining the output file
    outputFile: TextIOWrapper = open('output.txt', 'w')

    # First pass
    handleMacros(instructions)

    printMNT()
    printMAT()
    printMDT()
    # printMATDICT()

    # Second pass
    expandMacros()
    outputFile.write(variables.assemblyCode)
    outputFile.close()
    printAssemblyCode()
    