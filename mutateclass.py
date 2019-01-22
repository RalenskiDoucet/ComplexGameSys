import random
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


    def cross_over(self, genNumeOne, geneNumTwo, pivot):
        newGene = (geneNumOne[pivot:] + geneNumTwo[:pivot])
        return (newGene)