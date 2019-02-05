import random

#this class will be used for holding the symbols and other things for the expression.
class CNFSatisfiablityExpression(object):
    def __init__(self,expression):

        #A empty list for literals.
        self.literals = []
        #creates a list for values.
        self.speacial_literals = []
        self.values = []
        #A list for symbols used in the expression
        self.symbols = ["!","|","*","(",")"]
        self.clauses = expression.split("*")
        for character in expression:
            if character not in self.symbols:
                self.literals.append(character)                
                self.literals(character.expression.true)
                print("true")
                
        print(self.literals)


#this class will read from the file.
class Parser(object):
    def __init__(self,filename):
        self.file = filename
        self.file_to_open = open(self.file,"r")
        self.lines = self.file_to_open.readlines()

#needs to be able to evaluate the expression to be true of false  based on the symbols.
#needs to take in the expression as an argument.

# n  = Parser("CNFSatisfiablity.txt")
# for line in n.lines:
#     n = CNFSatisfiablityExpression(line)


