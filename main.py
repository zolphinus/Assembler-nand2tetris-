#Assembler for cs271
#tutorialspoint.com for syntax reference

__author__ = 'Cheech Wife'
import symbolTable
import Parser

#newTable = symbolTable.SymbolTable()
#newTable.__init__()
print ('creating file')
newFile = Parser.Parser("Max.asm", "Max.hack")
while newFile.hasMoreCommands() == True:
    currentLine = newFile.advanceInFile()
    newFile.parseFile(currentLine)

# print newTable
# print(newTable.table)
# print newTable.getAddress('ARG')
# print newTable.getAddress(line)
# newTable.checkTable('LCL')
# newTable.addEntry('Hey', 15)
# print newTable.getAddress('Hey')
# print newTable
#
# asmInstructions = self.asmFile.readline()
#         cIndex = asmInstructions.find("/")  #finds all instances of comment identifiers
#         asmInstructions = asmInstructions[:cIndex]  #finds the comment indicator
#         asmInstructions = asmInstructions.strip() + "\n"  #removes all whitespace and returns, adds \n
#         print ("instructions are", asmInstructions)