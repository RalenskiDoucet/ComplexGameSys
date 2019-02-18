import random
from ExpressionAndParser import CNFSatisfiablityExpression
from ExpressionAndParser import Parser
class Gene():
    '''
    expression => (a+b) * (c+a)  this is an expression in Conjunctive Normal Form
    literals => a,b,c
    symbols => (, ), +, !, *,  ,
    clauses => (a+b), (c+a)

    fitness =>  number of clauses that evaluate to true after substituting the "gene"
    gene => series of 1s or 0s that match the length of variables
    for example:

    '''
    def __init__(self,info):
        self.info = str(info)
    def make_gene(self,size):
        self.info = ""
        self.literals = ['a','b','c']
        self.values = ""
        for _ in self.literals:
            self.values.append()
        for i in range(0, size -1,1):
            temprandom= random.randint(0,1)
            self.info += str(temprandom)

    def gene_info(self):
        return self.info

    #def mutate(self, gene):
    #    '''input: string with format of 111000 or any sequence of 1s and 0s'''
    #    '''output: string "mutated"'''
    #    '''example: if input is 111111 and mutation rate is set to 1 then output would be 000000'''
    #    '''example: mutate("111111", 1) => "000000"'''
    #    '''example: mutate("000000", 0) => "111111"'''
    #    mutated_gene = []
    #    mutation_chance = .25

    #    for i in gene:
    #        if random.random() < mutation_chance:
    #            if i == 1:
    #               mutated_gene.append(0)
    #            else:
    #                mutated_gene.append(1)
    #        else:
    #            mutated_gene.append(i)

    #   return mutated_gene

    def gen_population(self, size):
        for i in range(0, len(Gene)):
            values = []
        for j in self.expression:
            values.append(random.randint(0,1))
            self.population.append()
            print(self.population)
    def cross_over(self, geneNumOne, geneNumTwo, pivot):
        g1 =""
        g2= ""
        for i in range(0,pivot):
            g1 += str(geneNumOne.info[i])
            g2 += str(geneNumTwo.info[i])
        for i in range(pivot, len(geneNumOne.info)):
            g1 += str(geneNumOne.info[i])
            g2 += str(geneNumTwo.info[i])
        g1 =  Gene
        g2 = geneNumTwo(g1)
        return (newGene)
a =  Parser("CNFSatisfiablity.txt")
for line in a.lines:
    a = CNFSatisfiablityExpression(line)
f= Gene(a)
f.make_gene(len(a.clauses))

