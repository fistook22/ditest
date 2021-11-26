# This challenge is about Biology that will put emphasis on your knowledge of classes, inheritance and polymorphism.

# Build a DNA object. DNA is composed of chromosomes which is itself composed of Genes.
# A Gene is a single value 0 or 1, it can mutate (flip).
# A Chromosome is a series of 10 Genes. It also can mutate, meaning a random number of genes can randomly flip (1/2 chance to flip).
# A DNA is a series of 10 chromosomes, and it can also mutate the same way Chromosomes can mutate.

# Implement these classes as you see fit.

# Create a new class called Organism that accepts a DNA object and an environment parameter that sets the probability for its DNA to mutate.

# Instantiate a number of Organism and let them mutate until one gets to a DNA which is only made of 1s. Then stop and record the number of generations (iterations) it took.
# Write your results in you personal biology research notebook and tell us your conclusion :).

# class DNA:
#     def __init__(self, value):
#         self.value = value

#     def mutate_0(self):
#         pass

#     def mutate_1(self):
#         pass


# class Chromosome(DNA):
#     pass

# class Gene(Chromosome, DNA):
#     pass


from typing import List
import random


class Gene:
    def __init__(self, value):
        self.value = value

    def flip(self):
        self.gene = random.randint(0, 1)


class Chromosome:
    def __init__(self, genes: List):
        if len(genes) != 10:
            raise Exception("The number of genes must be 10")

        self.genes = genes  # this is a list of 10 genes

    def flip(self):
        self.Chromosome = random.randint(0, 1)

    def is_ones(self):
        for gene in self.gene:
            if gene.value == 0:
                return False

        return True

    def show(self):
           for gene in self.genes:
                  print(gene, .end='')
        

    def mutate(self):
        for i in range(len(self.genes)):
            self.genes[i].flip()

    


class DNA:
    def __init__(self, Chromosome: list):
        if len(Chromosome) != 10:
            raise Exception("The number of genes must be 10")

        self.Chromosome = Chromosome

    def flip(self):
        self.Chromosome = random.randint(0, 1)

    def is_ones(self):
        for chrom in self.Chromosome:
            if not chrom.is_ones():
                return False
        return True


class Organism:
    def __init__(self, dna):
        self.dna = dna

    def flip_and_show(self):
        while not (self.dna.is_ones()):
            self.dna.show()
            self.dna.flip()

genes = [Gene(0), Gene(0), Gene(0), Gene(0), Gene(0), Gene(0), Gene(0), Gene(0), Gene(0), Gene(0),]
chromosome = Chromosome(genes)
dna = DNA(chromosome)
organism = Organism(dna)
organism.flip_and_show()

# from typing import List
# import random


# class Gene:
# 	def __init__(self, value: int):
# 		self.value = value

# 	def flip(self):
# 		self.value = random.randint(0, 1)


# class Chromosome:
# 	def __init__(self, genes: List[Gene]):
# 		if len(genes) != 10:
# 			raise Exception("you must provide 10 genes")

# 		self.genes = genes

# 	def flip(self) -> None:
# 		for i in range(len(self.genes)):
# 			self.genes[i].flip()

# 	def is_ones(self) -> bool:
# 		for gene in self.genes:
# 			if gene.value == 0:
# 				return False

# 		return True

# 	def show(self) -> None:
# 		for gene in self.genes:
# 			print(gene, end='')


# class DNA:
# 	def __init__(self, chromosomes: List[Chromosome]):
# 		if len(chromosomes) != 10:
# 			raise Exception("you must provide 10 chromosomes")

# 		self.chromosomes = chromosomes

# 	def flip(self) -> None:
# 		for i in range(len(self.chromosomes)):
# 			self.chromosomes[i].flip()

# 	def is_ones(self) -> bool:
# 		for chromosome in self.chromosomes:
# 			# if chromosome.is_ones() == False:
# 			if not chromosome.is_ones():
# 				return False

# 		return True

# 	def show(self) -> None:
# 		for chromosome in self.chromosomes:
# 			chromosome.show()

# 		print('')

# class Organism:
# 	def __init__(self, dna: DNA):
# 		self.dna = dna

# 	def flip_and_show(self) -> None:
# 		while not self.dna.is_ones():
# 			self.dan.show()
# 			self.dna.flip()

# 		self.dna.show()


# genes1 = [Gene(0),Gene(0),Gene(0),Gene(0),Gene(0),Gene(0),Gene(0),Gene(0),Gene(0),Gene(0)]
# genes2 = [Gene(0),Gene(0),Gene(1),Gene(0),Gene(0),Gene(1),Gene(0),Gene(0),Gene(0),Gene(0)]

# chromosome1 = Chromosome(genes1)
# chromosome2 = Chromosome(genes2)

# chromosomes = [chromosome1, chromosome2, chromosome2 ,chromosome2,chromosome1,chromosome1,chromosome1,chromosome1,chromosome1,chromosome2]

# dna = DNA(chromosomes)

# organism = Organism(dna)
# organism.flip_and_show()