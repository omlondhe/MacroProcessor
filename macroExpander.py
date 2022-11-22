from tables import MAT, MDT, MNT
import variables

def expand(instructionData: list[str]):
    parameters: list[str] = []
    if instructionData.__len__() >= 2:
        for i in range(1, instructionData.__len__()):
            parameters.append(instructionData[i])
    
    i, argumentStart = MNT[instructionData[0]][1] + 1, MNT[instructionData[0]][0]
    while MDT[i] != "MEND":
        macroRowData: list[str] = MDT[i].strip().replace(',', ' ').split(' ')

        for j in range(0, macroRowData.__len__()):
            if macroRowData[j].startswith('#'):
                macroRowData[j] = parameters[MAT[argumentStart + (int)(macroRowData[j].replace('#', ''))][1]]
        
        if macroRowData[0] in MNT:
            expand(macroRowData)
        else:
            variables.assemblyCode += " ".join(macroRowData) + '\n'
        i += 1


def expandMacros():
    instructions: list[str] = variables.code.split('\n')

    for instruction in instructions:
        instructionData: list[str] = instruction.strip().replace(',', ' ').split(' ')

        if instructionData[0] in MNT:
            expand(instructionData)
        else:
            variables.assemblyCode += instruction + '\n'
