import random
from ExpressionAndParser import CNFSatisfiablityExpression
from ExpressionAndParser import Parser
class Gene():
    def __init__(self, values):
        self.values = values


    def mutate(self, gene):
        mutated_gene = []
        mutation_chance = .25

        for i in gene:
            if random.random() < mutation_chance:
                if i == 1:
                    mutated_gene.append(0)
                else:
                    mutated_gene.append(1)
            else:
                mutated_gene.append(i)

        return mutated_gene

    def gen_population(self, size):
        for i in range(0, size):
            values = []
        for j in self.expression:
            values.append(random.randint(0,1))
            self.population.append()
            print(self.population)
    def cross_over(self, genNumeOne, geneNumTwo, pivot):
        newGene = (geneNumOne[pivot:] + geneNumTwo[:pivot])
        return (newGene)
a = Parser("CNFSatisfiablity.txt")
for line in a.lines:
    a = CNFSatisfiablityExpression(line)
f= Gene(a)
f.gen_population(a.values.count)
f.mutate(a.values)