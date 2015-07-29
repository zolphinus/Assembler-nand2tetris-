__author__ = 'Cheech Wife'
import symbolTable

#   Parser API:
#   Remove whitespace and comments
#   Get,read line
#   Evaluate line information ( A, C commands)
#   Based on command type returns symbol name for A, dest for C
newTable = symbolTable.SymbolTable()
newTable.__init__()

class Parser(object):
    def __init__(self, inputFile, outputFile):
        self.asmFile = open(inputFile, "r")
        self.hackFile = open(outputFile, "w")
        self.checkIt = open("Check.txt", "w")
    def __del__(self):
        print ('end')
    def hasMoreCommands(self):
        currentCommand = self.asmFile.readline()
        print (currentCommand)
        #print (self.asmFile)
        if currentCommand == '':
            print('Empty')
            return False
        else:
            print ('Not Empty')
            return True
    def advanceInFile(self):
        asmInstructions = self.asmFile.readline()
        cIndex = asmInstructions.find("/")
        asmInstructions = asmInstructions[:cIndex]
        asmInstructions = asmInstructions.strip()
        print(asmInstructions)
        return asmInstructions
    def parseFile(self, asmInstructions):
        if asmInstructions == '':
            print ('Empty')
        else:
            if '@' in asmInstructions:
                print "A_command"
                print ("I AM A COMMAND", asmInstructions)
            else:
                print "C_command"
                print (asmInstructions)
            print("current", asmInstructions)
            print ("line to print", asmInstructions)
