#this class will be used for holding the symbols and other things for the expression.
class CNFSatisfiablityExpression(object):
    def init_(self,expression):

        #A empty list for literals.
        self.literals = ["a","b","c","d","e","f"]
        #creates a list for values.
        self.values = [1,1,1,1,1,1]

        #A list for symbols used in the expression

        self.symbols =["!","|","+","*"]

        self.clauses = expression.split("*")

        for character in expression:
            if character not in self.symbols:
                self.literals.append(character)
                self.literals = list(set(self.literals))
                self.literals.sort()
        for character in self.literals:
            for value in self.values:
                character = value
        print(self.literals)

#this class will read from the file.
class Paser(object):
    def init_(self,filename):
        self.filename
        self.file = filename
        self.file_to_open = open(file,"r")
        self.lines = self.file_to_open.readlines()
    def openFile(self):
        self.filename=("CNFSatisfiablity.txt")
n  = Paser()

    for line in n.lines:
    j = CNFSatisfiablityExpression(line)
    
