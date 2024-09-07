# Eight Queens Puzzle
The 8 Queens problem is a classic chess problem that involves placing 8 queens on an 8x8 chessboard in such a way that no queen can attack another. This means that no two queens can be in the same row, column, or diagonal. This problem is an example of a constraint satisfaction problem and has been widely studied in artificial intelligence and computer science theory.

## Algorithms Used
In this repository, we will solve the 8 Queens problem using the following algorithms:

### 1 - Stochastic Hill Climbing
Stochastic Hill Climbing is a variation of the Hill Climbing algorithm that makes small random modifications to candidate solutions and accepts the new solution if it improves the objective function. Unlike traditional Hill Climbing, it may accept non-optimal changes to avoid getting stuck in local maxima/minima, allowing for broader exploration of the search space.

#### Fluxogram

![Stochastic Hill Climbing Fluxogram](attachments/HillBlack.png)

#### Results
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

### 2 - Genetic Algorithm
The Genetic Algorithm (GA) is an optimization algorithm inspired by the process of natural selection. It employs genetic concepts such as mutation, crossover, and selection to evolve solutions over multiple generations. Fitter solutions have a higher chance of passing their characteristics to the next generation, enabling efficient exploration of the solution space in search of the optimal answer.

#### Fluxogram

![Genetic Algorithm Fluxogram](attachments/GeneticBlack.png)

#### Results
Running the Genetic Algorithm 50 times, with populationSize = 20, mutarioRate = 0.03, crossoverRate = 0.8 and maximumGenerations = 100, we obtain the following metrics:

- ITERATIONS NUMBERS
    * Average: 802.08
    * Standard deviation: 339.16732389780714
- EXECUTION TIME
    * Average: 0.11257909774780274
    * Standard deviation: 0.047787798139628274
- FITNESSES
    * Average: 26.755555555555556
    * Standard deviation: 0.9226906440900753

With this configuration, the 5 best solutions obtained were:
* 1 - Solution N1: ['001', '100', '110', '000', '010', '111', '101', '011']; Fitness: 28
* 2 - Solution N2: ['011', '110', '000', '111', '100', '001', '101', '010']; Fitness: 28
* 3 - Solution N3: ['010', '000', '110', '100', '111', '001', '011', '101']; Fitness: 28
* 4 - Solution N4: ['011', '001', '111', '100', '110', '000', '010', '101']; Fitness: 28
* 5 - Solution N5: ['000', '110', '011', '101', '111', '001', '100', '010']; Fitness: 28

## Machine Specifications
The results above were obtained using the following machine specifications:

- **Processor**: AMD Ryzen 7 5700G @ 3.80GHz
- **RAM**: 32 GB
- **Operating System**: Windows 11 Pro 64-bit
- **Python Version**: 3.12.5
