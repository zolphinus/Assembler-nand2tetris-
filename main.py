__author__ = 'Cheech Wife'
import symbolTable

newTable = symbolTable.SymbolTable()
line = 'THAT'
newTable.__init__()

print newTable

print(newTable.table)
print newTable.getAddress('ARG')
newTable.checkTable('LCL')

newTable.addEntry('Hey', 15)
print newTable.getAddress('Hey')
print newTable