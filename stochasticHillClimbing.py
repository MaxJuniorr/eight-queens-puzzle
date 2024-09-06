import random
import time
from statistics import mean, pstdev, stdev

# 1 solution example
# vector = [4, 2, 0, 6, 1, 7, 5, 3]

def fitness(vector):
    fitness = 28

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
    #vector = [0, 0, 0, 0, 0, 0, 0, 0]
    #vector = [0, 1, 2, 3, 4, 5, 6, 7]
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
    #print(f"Final state: {vector}, fitness: {fitnessVector}, Iterations: {iterations + 1}")
    return vector, iterations, fitnessVector, finalTime - initialTime


def showStatistics(algoritm = 0, tests=50):
    
    statistics = {"iterations":[], "times":[], "fitnesses":[]}
    solutions = []

    if algoritm == 0:
        print(f"{20 * "="}Stochastic Hill Climbing{20 * "="}")
        for _ in range(tests):
            vector, iterations, fitness, time = stochasticHillClimbing()
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


showStatistics()