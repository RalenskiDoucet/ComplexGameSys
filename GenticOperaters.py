import random
from ExpressionAndParser import CNFSatisfiablityExpression
from ExpressionAndParser import Parser
def mutate(rate,inputstring):
    rate=.25
    mutated_string = []
    for i in inputstring:
        if random.random()<rate:
            if i ==1:
                mutated_string.append(0)
            else:
                mutated_string.append(1)
        else:
                mutated_string.append(1)
    return mutated_string

l1=[]
a = Parser("CNFSatisfiablity.txt")
for i in l1:
    a=CNFSatisfiablityExpression(l1)
mutate(100,a)
