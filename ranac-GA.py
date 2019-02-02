import sys
from numpy import genfromtxt
import random
import time

#Prva kolona predstavlja vrednost, a druga tezinu svakog predmeta

#Parametri
POPULATION = 10
THRESHOLD = 0.5
MUTATION = 0.1

#Memorisanje pocetnog vremena
pocetno_vreme = time.time()

class knapsack_population:
    def __init__(self):
        population = []

    def create_population(self, data, max_weight, num):
        #Stvaranje populacije
        population = []
        for i in range(num):
            total_value = 0
            total_weight = 0
            chromosome = [0] * len(data)
            for j in range(len(data)):
                if random.uniform(0, 1) > THRESHOLD and total_weight < max_weight:
                    chromosome[j] = 1
                    total_value += data[j, 0]
                    total_weight += data[j, 1]
            population.append(chromosome)
        return population

    #Fitenes funckija    
    def fitnesFunkcija(self, my_data, population, chromosome):
        
        d = {}
        for i in range(len(population)):
            value = chromosome.calculate_value(my_data, population[i])
            d[value] = population[i]
        keys = sorted(d,reverse=True)
        new_d = {}
        for k in keys:
            new_d[k]=d[k]
        return new_d


class item_chromosome:
    def __init__(self):
        self.chromosome = []


    #Ukrstanje
    def combine(self, my_data, parent1, parent2, weight, chromosome, gene):
        child = [0]*len(parent1)
        first_half = int(len(parent1) / 2)
        second_half = len(parent2) - first_half
        for i in range(first_half):
            child[i] = parent1[i]
        for i in range(first_half, first_half + second_half):
            child[i] = parent2[i]
        child = gene.mutate(child)
        while self.calculate_weight(my_data, child) > weight:
            child = chromosome.remove_item(child)
        return child

    #Uklanjanje predmeta koji prevazilazi zadati kapacitet
    def remove_item(self, chromosome):
        while True:
            bit = random.randint(0, len(chromosome) - 1)
            if chromosome[bit] == 1:
                chromosome[bit] = 0
                return chromosome
    
    #Racunanje ukupne vrednosti hromozoma
    def calculate_value(self, my_data, chromosome):
        value = 0
        for i in range(len(chromosome)):
            if  chromosome[i] == 1:
                value += my_data[i, 0]
        return value

    #Racunanje ukupne tezine hromozoma    
    def calculate_weight(self, my_data, chromosome):
        weight = 0
        for i in range(len(chromosome)):
            weight += chromosome[i] * my_data[i, 1]
        return weight


class item_gene:
    def __init__(self, my_data):
        self.gene = []

    #Mutacija
    def mutate(self, chromosome):
        if random.uniform(0, 1) < MUTATION:
            bit = random.randint(0, len(chromosome)-1)
            if chromosome[bit] == 0:
                chromosome[bit] = 1
            else:
                chromosome[bit] = 0
        return chromosome


def main():
    args = sys.argv
    max_weight = int(args[1])
   

    try:
        my_data = genfromtxt(args[2], delimiter=' ')
    except:
        print('Greska prilikom otvaranja fajla')
        
        testknapsack = knapsack_population()
        testchromosome = item_chromosome()
        testgene = item_gene(my_data)
        assert testknapsack.fitnesFunkcija(testknapsack,testchromosome)
        assert testchromosome.combine(my_data,testchromosome,testchromosome,max_weight,testchromosome,testgene)
        assert testchromosome.calculate_value(my_data,testchromosome)
        assert testchromosome.calculate_weight(my_data,testchromosome)
        assert testgene.mutate(testchromosome)
    
    knapsack = knapsack_population()
    chromosome = item_chromosome()
    gene = item_gene(my_data)
    population = knapsack.create_population(my_data, max_weight, POPULATION)
    for i in range(500):
        new_population = []
        population_scores = knapsack.fitnesFunkcija(my_data, population, chromosome)
        sorted_population = []
        for k, v in population_scores.items():
            sorted_population.append(population_scores[k])
        for j in range(len(sorted_population) - 1):
            for m in range(len(sorted_population) - 1):
                if m != j:
                    child = chromosome.combine(my_data, sorted_population[j], sorted_population[m], max_weight,
                                               chromosome, gene)
                    new_population.append(child)

        population = new_population
        new_population_score = knapsack.fitnesFunkcija(my_data, population, chromosome)

    best = max(new_population_score.keys(), key=lambda x: len(new_population_score[x]))

    print ('Najveca vrednost:', best)
    print ('Hromozom:', new_population_score[best])
    print ('Tezina:',chromosome.calculate_weight(my_data, new_population_score[best]))
    print ('Vreme izvrsavanja:%s sekundi' % (time.time() - pocetno_vreme))

if __name__ == "__main__":
    main()