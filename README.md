# Eight Queens Puzzle
In this repository, we will solve the eight queens puzzle using the following algorithms:

## 1 - Stochastic hill climbing
Stochastic Hill Climbing is a variation of the Hill Climbing algorithm that makes small random modifications to candidate solutions and accepts the new solution if it improves the objective function. Unlike traditional Hill Climbing, it may accept non-optimal changes to avoid getting stuck in local maxima/minima, allowing for broader exploration of the search space.

### Fluxogram


### Results
Running the Stochastic Hill Climbing 50 times, with a MAXFAILS = 500, we obtain the following metrics:

- ITERATIONS NUMBERS
    * Average: 493.66
    * Standard deviation: 69.67886623647087
- EXECUTION TIME
    * Average: 0.004920492172241211
    * Standard deviation: 0.0008095206644539864
- FITNESSES
    * Average: 25.288888888888888
    * Standard deviation: 0.5820355934981687

With this configuration, the 5 best solutions obtained were:
* 1 - Solution N1: [2, 5, 1, 4, 7, 0, 6, 3]; Fitness: 28
* 2 - Solution N1: [2, 5, 0, 6, 2, 2, 4, 2]; Fitness: 27
* 3 - Solution N1: [0, 4, 1, 6, 1, 6, 4, 2]; Fitness: 27
* 4 - Solution N1: [5, 0, 3, 1, 4, 3, 5, 7]; Fitness: 26
* 5 - Solution N1: [2, 6, 3, 2, 2, 3, 1, 4]; Fitness: 26

## 2 - Genetic Algorithm
The Genetic Algorithm (GA) is an optimization algorithm inspired by the process of natural selection. It employs genetic concepts such as mutation, crossover, and selection to evolve solutions over multiple generations. Fitter solutions have a higher chance of passing their characteristics to the next generation, enabling efficient exploration of the solution space in search of the optimal answer.

### Fluxogram


### Results