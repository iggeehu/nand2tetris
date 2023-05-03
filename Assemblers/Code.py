from typing import ByteString, BinaryIO

def dest(string: str)->BinaryIO:
    if string == None:
        return 0b0000000000000000
    if string == "M":
        return 0b0000000000001000
    if string == "D":
        return 0b0000000000010000
    if string == "MD":
        return 0b0000000000011000
    if string == "A":
        return 0b0000000000100000
    if string == "AM":
        return 0b0000000000101000
    if string == "AD":
        return 0b0000000000110000
    if string == "AMD":
        return 0b0000000000111000
    else:
        return ValueError("Invalid input")
    
def comp(string: str)->int:
    
    if string == "0":
        return 0b0000101010000000
    if string == "1":
        return 0b0000111111000000
    if string == "-1":
        return 0b0000111010000000
    if string == "D":
        return 0b0000001100000000
    if string == "A":
        return 0b0000110000000000
    if string == "!D":
        return 0b0000001101000000
    if string == "!A":
        return 0b0000110001000000
    if string == "-D":
        return 0b0000001111000000
    if string == "-A":
        return 0b0000110011000000
    if string == "D+1":
        return 0b0000011111000000
    if string == "A+1":
        return 0b0000110111000000
    if string == "D-1":
        return 0b0000001110000000
    if string == "A-1":
        return 0b0000110010000000
    if string == "D+A":
        return 0b0000000010000000
    if string == "D-A":
        return 0b0000010011000000
    if string == "A-D":
        return 0b0000000111000000
    if string == "D&A":
        return 0b0000000000000000
    if string == "D|A":
        return 0b0000010101000000
    if string == "M":
        return 0b0001110000000000
    if string == "!M":
        return 0b0001110001000000
    if string == "-M":
        return 0b0001110011000000
    if string == "M+1":
        return 0b0001110111000000
    if string == "M-1":
        return 0b0001110010000000
    if string == "D+M":
        return 0b0001000010000000
    if string == "D-M":
        return 0b0001010011000000
    if string == "M-D":
        return 0b0001000111000000
    if string == "D&M":
        return 0b0001000000000000
    if string == "D|M":
        return 0b0001010101000000
    else:
        raise ValueError("Invalid input")


def jump(string: str)->BinaryIO:
    if string == None:
        return 0b0000000000000000
    if string == "JGT":
        return 0b0000000000000001
    if string == "JEQ":
        return 0b0000000000000010
    if string == "JGE":
        return 0b0000000000000011
    if string == "JLT":
        return 0b0000000000000100
    if string == "JNE":
        return 0b0000000000000101
    if string == "JLE":
        return 0b0000000000000110
    if string == "JMP":
        return 0b0000000000000111
    else:
        raise ValueError("Invalid input")
    
