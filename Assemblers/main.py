from Parser import Parser
from Code import dest, comp, jump
from SymbolTable import SymbolTable
import sys
import os

def int_to_15_bit_string(i: int) -> str:
    binary = bin(i)[2:]
    return str(binary.zfill(15))


def main(file_name:str):
    table = SymbolTable()
    path=os.path.join(os.getcwd(), file_name)
    parser = Parser(path)
    file_name_no_suffix = file_name.split(".")[0]

    f=open(file_name_no_suffix+".hack", "x")
    f.close()
    f=open(file_name_no_suffix+".hack", "w")


    while parser.has_more_commands():
        parser.advance()
    
        if parser.command_type()=='A_COMMAND' or parser.command_type()=='C_COMMAND':
            parser.ROM_address+=1
        if parser.command_type()=='L_COMMAND':
            symbol=parser.symbol()
            table.addEntry(symbol, parser.ROM_address)

    

    parser2 = Parser(path)
    print(table.symbol_table)

    while parser2.has_more_commands():
        parser2.advance()
        #if A command, look up symbol or add entry to table, produe string
        print(parser2.command_type())
        if parser2.command_type()=='A_COMMAND':
            
            symbol = parser2.symbol()
            if symbol.isnumeric():
                result="0"+int_to_15_bit_string(int(symbol))
                f.write(result)
            elif table.contains(symbol):
                address=table.get_address(symbol)
                result="0"+int_to_15_bit_string(address)
                f.write(result)
            else:
                table.addEntry(symbol, table.get_current_address())
                address = table.get_address(symbol)
                result="0"+int_to_15_bit_string(address)
                f.write(result)
                table.inc_currrent_address()
            f.write("\n")
            
        #if C command
        if parser2.command_type()=='C_COMMAND':
            binary_base=0b1110000000000000
            dest_string=parser2.dest()
            dest_bin=dest(dest_string)
            comp_string=parser2.comp()
            comp_bin=comp(comp_string)
            jump_string=parser2.jump()
            jump_bin=jump(jump_string)
            binary=binary_base+comp_bin+dest_bin+jump_bin
            f.write(str(bin(binary))[2:])
            f.write("\n")
        

    f.close()

if __name__ == "__main__":
    main(sys.argv[1])