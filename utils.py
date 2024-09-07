import random
import time
from statistics import mean, pstdev

def fitness(vector, binary=False):
    # 8 queen's max value
    fitness = 28
    vector = vector.copy()

    # if it's binary, changes back to decimal
    if binary:
        for i in range(len(vector)):
            # debugging
            vector[i] = int(vector[i], 2)

    # This frame verify colisions in lines.
    for i in range(len(vector)):
        # there is 3 colision cases:
        # 1. horizontal colision
        # 2. lower diagonal colision
        # 3. Upper diagonal colision
        colided = [False, False, False]
        for j in range(i + 1, len(vector)):
            # if horizontal colision
            if not(colided[0]) and vector[i] == vector[j]:
                fitness -= 1
                colided[0] = True
            
            # if lower diagonal colision!
            if not(colided[1]) and vector[i] - (j - i) == vector[j]:
                fitness -= 1
                colided[1] = True
            
            # if upper diagonal colision
            if not(colided[2]) and vector[i] + (j - i) == vector[j]:
                fitness -= 1
                colided[2] = True
            
            if all(colided):
                break
            
    return fitness

def stochasticHillClimbing(stepMode = 0, verbose = False):
    initialTime = time.time()
    vector = [random.randint(0, 7) for _ in range(8)]
    fitnessVector = fitness(vector)

    # initial state
    if verbose:
        print(f"Initial state: {vector}, fitness: {fitnessVector}")

    MAXFAILS = 500
    fails = 0
    iterations = 0
    
    while fails < MAXFAILS:
        iterations += 1
        if fitness(vector) == 28:
            finalTime = time.time()
            return vector, iterations, fitnessVector, finalTime - initialTime

        if stepMode == 0:
        # taking a single step (1 unit) in a random direction
            randomIndex = random.randint(0, 7)
            if vector[randomIndex] == 0:
                vector[randomIndex] += 1
            elif vector[randomIndex] == 7:
                vector[randomIndex] -= 1
            else:
                randomValue = random.randint(0, 1)
                vector[randomIndex] += 1 if randomValue == 1 else -1
                
        elif stepMode == 1:
            # putting 1 queen in 1 random position
            vector[random.randint(0, 7)] = random.randint(0, 7)

        # if the new fitness is better than the old one
        # we take the step
        newFitness = fitness(vector)
        
        if newFitness > fitnessVector:
            fitnessVector = newFitness
        else:
            fails += 1
    
    finalTime = time.time()
    return vector, iterations, fitnessVector, finalTime - initialTime

def rouletteSelection(population, fitnesses):
  fitnessSum = sum(fitnesses)
  pointer = random.uniform(0, fitnessSum)
  cumulatedSum = 0
  for i, fitness in enumerate(fitnesses):
    cumulatedSum += fitness
    if pointer <= cumulatedSum:
      return population[i]

def geneticAugorithm(populationSize = 20, mutationRate = 0.03, crossoverRate = 0.8, maximumGenerations = 1000):
    initialTime = time.time()
    population = [[''.join(random.choices('01', k=3)) for _ in range(8)] for _ in range(populationSize)]
    iterations = 0
    while iterations < maximumGenerations:
        fitnesses = []
        # roll the roullet populationSize times, in order to select the parents
        # respecting fitnesses values
        bestIndividual = [None, 0]
        for individual in population:
            fitnessIndividual = fitness(individual, binary=True)
            if fitnessIndividual == 28:
                finalTime = time.time()
                return individual, iterations, fitnessIndividual, finalTime - initialTime
            fitnesses.append(fitnessIndividual)
            if bestIndividual[1] < fitnessIndividual:
                bestIndividual = [individual, fitnessIndividual]

        selectedParents = [rouletteSelection(population, fitnesses) for _ in range(populationSize)]
        
        # crossover
        for i in range(0, populationSize, 2):
            if random.random() < crossoverRate:
                crossoverPoint = random.randint(0, 7)
                parent1 = selectedParents[i]
                parent2 = selectedParents[i + 1]
                child1 = parent1[:crossoverPoint] + parent2[crossoverPoint:]
                child2 = parent2[:crossoverPoint] + parent1[crossoverPoint:]
                # mutation
                if random.random() < mutationRate:
                    queenIndex = random.randint(0, 7)
                    bitIndex = random.randint(0, 2)
                    child1[queenIndex] = child1[queenIndex][:bitIndex] + ('1' if child1[queenIndex][bitIndex] == '0' else '0') + child1[queenIndex][bitIndex + 1:]
                if random.random() < mutationRate:
                    queenIndex = random.randint(0, 7)
                    bitIndex = random.randint(0, 2)
                    child2[queenIndex] = child2[queenIndex][:bitIndex] + ('1' if child2[queenIndex][bitIndex] == '0' else '0') + child2[queenIndex][bitIndex + 1:]
                # elitism replacement
                population[i] = child1
                population[i + 1] = child2
        # the best individu survives
        population[random.randint(0, populationSize - 1)] = bestIndividual[0]

        iterations += 1

    finalTime = time.time()
    return individual, iterations, fitnessIndividual, finalTime - initialTime

def showStatistics(algorithm = 0, tests=50):
    
    statistics = {"iterations":[], "times":[], "fitnesses":[]}
    solutions = []

    if algorithm == 0:
        print(f"{20 * "="}Stochastic Hill Climbing{20 * "="}")
        for _ in range(tests):
            vector, iterations, fitness, time = stochasticHillClimbing()
            solutions.append(vector)
            statistics["iterations"].append(iterations)
            statistics["fitnesses"].append(fitness)
            statistics["times"].append(time)
    if algorithm == 1:
        print(f"{20 * "="}Genetic Algorithm{20 * "="}")
        for _ in range(tests):
            vector, iterations, fitness, time = geneticAugorithm()
            solutions.append(vector)
            statistics["iterations"].append(iterations)
            statistics["fitnesses"].append(fitness)
            statistics["times"].append(time)

    print("Top 5 solutions")
    for i in range(5):
        idxMax = statistics["fitnesses"].index(max(statistics["fitnesses"]))
        print(f"Solution N{i + 1}: {solutions[idxMax]}; Fitness: {statistics['fitnesses'][idxMax]}\n")
        del statistics["fitnesses"][idxMax]
        del solutions[idxMax]

    for key, value in statistics.items():
        print(f"{20 * "="}{key}{20 * "="}")
        print(f"Average: {mean(value)}; Standard deviation: {pstdev(value)}\n")

showStatistics(algorithm=1)