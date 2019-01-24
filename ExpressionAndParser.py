#this class will be used for holding the symbols and other things for the expression.
class CNFSatisfiablityExpression(object):
    def __init__(self,expression):

        #A empty list for literals.
        self.literals = {"a","b"}
        #creates a list for values.
        self.values = [1,1,1,1,1,1]
        self.clauses= expression.split()

        #A list for symbols used in the expression

        self.symbols = {"!","|","*"}
        self.symbols_meaning = ["not","or","and"]
        self.clauses = expression.split("*")

        for character in expression:
            if character not in self.symbols:
                self.literals.append(character)
                self.literals = list(set(self.literals))
                self.literals.replace("a","1")
                self.literals.replace("b","0")
        for character in self.literals:
            for value in self.values:
                character = value
        print(self.literals)


#this class will read from the file.
class Parser(object):
    def __init__(self,filename):
        self.file = filename
        self.file_to_open = open(self.file,"r")
        self.lines = self.file_to_open.readlines()

#needs to be able to evaluate the expression to be true of false  based on the symbols.
#needs to take in the expression as an argument.


n  = Parser("CNFSatisfiablity.txt")
for line in n.lines:
    n = CNFSatisfiablityExpression(line)

