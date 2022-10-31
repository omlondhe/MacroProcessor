import re
import variables
from tables import MAT_DICT, MNT, MAT, MDT


def getFormattedInstruction(instruction: str) -> str:
    return re.sub("\s\s+", ' ', instruction).replace(", ", ',')


def handleMacro(instructions: list[str]):
    i: int = 0
    while i < instructions.__len__():
        instruction: str = getFormattedInstruction(instructions[i])
        if instruction.__len__() == 0:
            i += 1
            continue

        if not instruction.upper().startswith("MACRO"):
            variables.intermediateCode += f"{instruction}\n"
            i += 1
            continue
        
        if instruction.upper().strip() == "MACRO": 
            i += 1
            instruction = getFormattedInstruction(instructions[i])
        else: 
            instruction = instruction[6:]
        
        instruction.replace(',', ' ')
        MDT.append(instruction)
        macroDefinition: list[str] = instruction.split(' ')
        parameters: list[str] = macroDefinition[1].split(',') if macroDefinition.__len__() > 1 else []
        MNT[macroDefinition[0]] = [MAT.__len__() if parameters.__len__() != 0 else -1, MDT.__len__() - 1]
        i += 1
        instruction = getFormattedInstruction(instructions[i])

        if parameters.__len__():
            for position in range(parameters.__len__()):
                parameter: str = parameters[position]
                if parameter.__contains__('='):
                    parameter = parameters[position].split('=')[0]
                MAT.append((parameter, position))
                MAT_DICT[parameter] = position

        while not instruction == "MEND":
            for key in MAT_DICT:
                instruction = instruction.replace(f"{key}", f"#{MAT_DICT[key]}")
            MDT.append(instruction)
            i += 1
            instruction = getFormattedInstruction(instructions[i])
        
        MAT_DICT.clear()
        MDT.append("MEND")
        i += 1


    