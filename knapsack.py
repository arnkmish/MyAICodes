'''
ARNAB KUMAR MISHRA - arnkmish HW6 Submission
'''
import math
import sys
import random
import pickle
import numpy as np
import pandas as pd
from scipy.stats import norm

def fitness(max_volume,volumes,prices):
    # Fitness function returns total value of all the selected objects unless no object is selected or volume constraint is violated 
    if sum(volumes) > max_volume or sum(volumes) <= 0:
        fitness = 0
    else:
        fitness = sum(prices)

    return fitness

def randomSelection(population,fitnesses):
    # Roulette Wheel Selection
    summation = 0
    list2=[]
    for i in fitnesses:
        summation = summation + i
        list2 += [summation]
    
    num=random.uniform(1,summation)
    for i in range(0,len(list2)):
        if num <= list2[i]:
            return population[i]
 

def badChildDetector(child, world):
    # Let no child violate the volume constraint
    if sum(world[1]*np.array(child)) <= world[0]:
        return child
    else:
        while sum(world[1]*np.array(child)) > world[0]:
            child = mutate(child,0.1)
        return child
    
    

def reproduce(mom,dad,world, mutationProbability):
    # Single point crossover
    mid_index = len(mom) / 2

    mom = list(mom)
    dad = list(dad)

    firstHalfChild1 = mom[:mid_index]
    secondHalfChild1 = dad[mid_index:]
    child1 = firstHalfChild1 + secondHalfChild1
    child1 = mutate(child1, mutationProbability)
    child1 = badChildDetector(child1, world)


    firstHalfChild2 = dad[:mid_index]
    secondHalfChild2 = mom[mid_index:]
    child2 = firstHalfChild2 + secondHalfChild2
    child2 = mutate(child2, mutationProbability)
    child2 = badChildDetector(child2, world)
    
    return np.array([np.array(x) for x in child1]), np.array([np.array(y) for y in child2])

def mutate(mutatedChild,mutation_probability):
    # Mutate each bit of a child based on the given mutation probability
    for i in range(0, len(mutatedChild)):
        if random.randint(1, 1000) <= mutation_probability * 1000: # 1000 is to support upto 3 decimal spaces
            mutatedChild[i] = int(not mutatedChild[i])
    return mutatedChild

def compute_fitnesses(world,chromosomes):
    return [fitness(world[0], world[1] * chromosome, world[2] * chromosome) for chromosome in chromosomes]

def generateRandomChromosomes(world, popsize):
    # Generate first batch of random solutions, while making sure that all of them are valid solutions
    max_volume = world[0]
    volumes = world[1]
    numOfChromosomes = popsize
    wholePopulation = []
    
    while numOfChromosomes != 0:
        chromosome = []
        for i in range(len(volumes)):
            chromosome = chromosome + [(random.choice([0,1]))]
            
        if sum(world[1]*np.array(chromosome)) <= max_volume:
            wholePopulation.append(chromosome)
            numOfChromosomes = numOfChromosomes - 1

    rand_chromosomes = np.array([np.array(x) for x in wholePopulation])
    return rand_chromosomes

def genetic_algorithm(world,popsize,max_years,mutation_probability):
    # Generate the first random batch of solutions
    rand_chromosomes = generateRandomChromosomes(world, popsize)
    # Compute their fitnesses
    fitnesses = compute_fitnesses(world, rand_chromosomes)
    output = []
    selectedPopulations = rand_chromosomes[:]
    years = max_years
    terminate = False
    pick = 0
    while terminate == False:
        if years < 1:
            terminate = True
        else:
            # Perform natural selection
            selectedPopulations = [randomSelection(selectedPopulations, fitnesses) for i in range(popsize)]
            # Sort the population based on fitness values, so that good solutions are together, which ensures reproduction between good chromosomes
            selectedPopulations = np.array(selectedPopulations)
            fitnesses = np.array(fitnesses)
            inds = fitnesses.argsort()
            fitnesses = list(fitnesses).sort()
            selectedPopulations = list(selectedPopulations[inds])
            new_Generation = []
            new_Generation = selectedPopulations[:]
            # Select the amount of elitism
            elites = int(0.1 * popsize)+1
            # Perform crossover on the non elite chromosomes
            for i in range(0, len(selectedPopulations)-elites, 2): # Put 1 in place of elites to not do elitism
                new_Generation[i], new_Generation[i+1] = reproduce(selectedPopulations[i], selectedPopulations[i+1], world, mutation_probability)
            # Calculate the fitnesses of the newly created and probably mutated children
            fitnesses = compute_fitnesses(world, new_Generation)
            selectedPopulations = new_Generation[:]
            years = years - 1
            terminate = False
            output = output + [(selectedPopulations, fitnesses)]

    return output

def run(popsize,max_years,mutation_probability):
    '''
    The arguments to this function are what they sound like.
    Runs genetic_algorithm on various knapsack problem instances and keeps track of tabular information with this schema:
    DIFFICULTY YEAR HIGH_SCORE AVERAGE_SCORE BEST_PLAN'''
    
    table = pd.DataFrame(columns=["DIFFICULTY", "YEAR", "HIGH_SCORE", "AVERAGE_SCORE", "BEST_PLAN"])
    sanity_check = (10, [10, 5, 8], [100,50,80])
    chromosomes = genetic_algorithm(sanity_check,popsize,max_years,mutation_probability)
    for year, data in enumerate(chromosomes):
        year_chromosomes, fitnesses = data
        table = table.append({'DIFFICULTY' : 'sanity_check', 'YEAR' : year, 'HIGH_SCORE' : max(fitnesses),
            'AVERAGE_SCORE' : np.mean(fitnesses), 'BEST_PLAN' : year_chromosomes[np.argmax(fitnesses)]}, ignore_index=True)
    easy = (20, [20, 5, 15, 8, 13], [10, 4, 11, 2, 9] )
    chromosomes = genetic_algorithm(easy,popsize,max_years,mutation_probability)
    for year, data in enumerate(chromosomes):
        year_chromosomes, fitnesses = data
        table = table.append({'DIFFICULTY' : 'easy', 'YEAR' : year, 'HIGH_SCORE' : max(fitnesses),
            'AVERAGE_SCORE' : np.mean(fitnesses), 'BEST_PLAN' : year_chromosomes[np.argmax(fitnesses)]}, ignore_index=True)
    medium = (100, [13, 19, 34, 1, 20, 4, 8, 24, 7, 18, 1, 31, 10, 23, 9, 27, 50, 6, 36, 9, 15],
                   [26, 7, 34, 8, 29, 3, 11, 33, 7, 23, 8, 25, 13, 5, 16, 35, 50, 9, 30, 13, 14])
    chromosomes = genetic_algorithm(medium,popsize,max_years,mutation_probability)
    for year, data in enumerate(chromosomes):
        year_chromosomes, fitnesses = data
        table = table.append({'DIFFICULTY' : 'medium', 'YEAR' : year, 'HIGH_SCORE' : max(fitnesses),
            'AVERAGE_SCORE' : np.mean(fitnesses), 'BEST_PLAN' : year_chromosomes[np.argmax(fitnesses)]}, ignore_index=True)
    hard = (5000, norm.rvs(50,15,size=100), norm.rvs(200,60,size=100))
    chromosomes = genetic_algorithm(hard,popsize,max_years,mutation_probability)
    for year, data in enumerate(chromosomes):
        year_chromosomes, fitnesses = data
        table = table.append({'DIFFICULTY' : 'hard', 'YEAR' : year, 'HIGH_SCORE' : max(fitnesses),
            'AVERAGE_SCORE' : np.mean(fitnesses), 'BEST_PLAN' : year_chromosomes[np.argmax(fitnesses)]}, ignore_index=True)
    for difficulty_group in ['sanity_check','easy','medium', 'hard']:# ,'hard','sanity_check','easy',
        group = table[table['DIFFICULTY'] == difficulty_group]
        bestrow = group.ix[group['HIGH_SCORE'].argmax()]
        print("Best year for difficulty {} is {} with high score {} and chromosome {}".format(difficulty_group,int(bestrow['YEAR']), bestrow['HIGH_SCORE'], bestrow['BEST_PLAN']))
    table.to_pickle("results.pkl") #saves the performance data, in case you want to refer to it later. pickled python objects can be loaded back at any later point.
    #print table

if __name__ == "__main__":
    run(int(sys.argv[1]),int(sys.argv[2]),float(sys.argv[3]))
