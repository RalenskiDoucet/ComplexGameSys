class CNFSatisfiablity(object):
    def init_(self,expression):
        self.variables = ["a","b","c","d","e","f"]
        self.symbols =["!","|","&"]
        self.values = [1,1,1,1,1,1]
        self.literals = []
        for character in expression:
            if character not in self.symbols:
                self.literals.append(character)
                self.literals = list(set(self.literals))
                self.literals.sort()
        for character in self.literals:
        for value in self.values:
             character = value
        print(self.literals)
class Paser(object):
    def init_(self,filename):
        self.file = filename
        self.file_to_open = open(self.file,"r")
        self.lines = file_to_open.readlines()
a=Paser("CNFSatisfiablity.txt")
for line in a.lines
    j=expression(line)

