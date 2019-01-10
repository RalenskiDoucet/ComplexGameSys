#this class will be used for holding the symbols and other things for the expression.
class CNFSatisfiablityExpression():
    def init_(self,expression):
        self.literals = []
        self.values = [1,1,1,1,1,1]
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
class Paser():
    def init_(self,filename):
        self.file = filename
        self.file_to_open = open(self.file,"r")
        self.lines = self.file_to_open.readlines()

n = Paser("CNFSatisfiablity.txt")
for line in n.lines:
    j = CNFSatisfiablityExpression(line)

