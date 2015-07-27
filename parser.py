__author__ = 'Cheech Wife'
# Parser API:
#   Remove whitespace and comments
#   Get,read line
#   Evaluate line information ( A, C, L commands)
#   Based on command type returns symbol name for A, dest for C

class Parser(object):
    def __init__(self, inputFile, outputFile):
        self.asmFile = open(inputFile, "r")
        self.hackFile = open(outputFile, "w")
        self.checkIt = open("Check.txt", "w")
        asmInstructions = ""

    def __del__(self):
        print ('end')

    def parseFile(self):
        readLine = self.asmFile.readline()
        if readLine == '':
            print ('Empty')
        else:
            while readLine:  # while there is still information in the .asm file to read
                cIndex = readLine.find("/")  #finds all instances of comment identifiers
                readLine = readLine[:cIndex]  #finds the comment indicator
                readLine = readLine.strip() + "\n"  #removes all whitespace and returns, adds \n
                if '@' in readLine:
                    print "A_command"
                else:
                    print "C_command"
                print("current", readLine)
                print ("line to print", readLine)
                readLine = self.asmFile.readline()
