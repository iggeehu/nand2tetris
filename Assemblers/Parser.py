
def clean_asm(line:str)->str:
    line=line.replace(" ", "")
    return line.split("//")[0]
    

class Parser:
    ROM_address: int = 0

    def __init__(self, path: str):
        with open(path, 'r') as file:
            self.lines = [clean_asm(line) for line in file]
            print(self.lines)
            self.i: int = 0 # what the curr line is

    def has_more_commands(self) -> bool:
        return self.i < len(self.lines)
    
    def advance(self):
        self.i += 1
        if self.has_more_commands() and (self.lines[self.i]=="" or self.lines[self.i]=="\n"):
                self.advance() 

    def increment_rom(self):
        self.ROM_address += 1

    def command_type(self) -> str:
        """Returns the type of the current command:
        m A_COMMAND for @Xxx where
        Xxx is either a symbol or a
        decimal number
        m C_COMMAND for
        dest=comp;jump
        m L_COMMAND (actually, pseudocommand) for (Xxx) where Xxx
        is a symbol.    
        """
        if self.i>len(self.lines)-1:
            return "END"
        if self.lines[self.i][0]=="@":
            return "A_COMMAND"
        if self.lines[self.i][0]=="(":
            return "L_COMMAND"
        else:
            return "C_COMMAND"


        pass
    def symbol(self) -> str:
        """Returns the symbol or decimal Xxx of the current command @Xxx or (Xxx). 
        Should be called only when commandType() is
        A_COMMAND or L_COMMAND."""
        if self.command_type()=="A_COMMAND":
            return self.lines[self.i][1:-1] if self.lines[self.i][-1]=="\n" else self.lines[self.i][1:]
        if self.command_type()=="L_COMMAND":
            return self.lines[self.i][1:-2] if self.lines[self.i][-1]=="\n" else self.lines[self.i][1:-1]
        

    def dest(self) -> str:  
        """Returns the dest mnemonic in
        the current C-command (8 possibilities). Should be called only
        when commandType() is C_COMMAND."""
        if self.lines[self.i].find('=')!=-1:
            dest, _ = self.lines[self.i].split('=', 1)
            return dest
        else:
            return None
    
    def comp(self) -> str:
        """
        Reurns the comp mnemonic in
        the current C-command (28 possibilities). Should be called only
        when commandType() is
        C_COMMAND.

        """
        if self.lines[self.i].find('=')!=-1:
            _ , compMnemonic = self.lines[self.i].split('=', 1)
            return compMnemonic[:-1] if compMnemonic[-1]=="\n" else compMnemonic
        elif self.lines[self.i].find(';')!=-1:
            compMnemonic, _ = self.lines[self.i].split(';', 1)
            return compMnemonic

    def jump(self) -> str:
        """Returns the jump mnemonic in
        the current C-command (8 possibilities). Should be called only
        when commandType() is
        C_COMMAND"""
        if self.lines[self.i].find('J')!=-1:
            return self.lines[self.i][-4:-1] if self.lines[self.i][-1]=="\n" else self.lines[self.i][-3:]
        else:
            return None
        
    def is_jump(self) -> bool:
        return self.jump() is not None