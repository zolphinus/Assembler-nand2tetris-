#Assembler for cs271
#tutorialspoint.com for syntax reference

__author__ = 'Cheech Wife'
import symbolTable
import Parser

newTable = symbolTable.SymbolTable()
newFile = Parser.Parser("Max.asm", "Max.hack")
line = 'THAT'
newTable.__init__()
newFile.__init__("Max.asm", "Max.hack")
newFile.parseFile()

print newTable

print(newTable.table)
print newTable.getAddress('ARG')
print newTable.getAddress(line)
newTable.checkTable('LCL')

newTable.addEntry('Hey', 15)
print newTable.getAddress('Hey')
print newTable