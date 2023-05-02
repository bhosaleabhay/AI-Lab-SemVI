import random

# Define the problem
distances = [
    [0, 10, 20, 5],
    [10, 0, 15, 20],
    [20, 15, 0, 10],
    [5, 20, 10, 0]
]

num_cities = len(distances)

# Set GA parameters
population_size = 20
mutation_rate = 0.01
generations = 100

# Define functions

# Calculate the fitness of an individual
def fitness(individual):
    total_distance = 0
    for i in range(num_cities - 1):
        total_distance += distances[individual[i]][individual[i+1]]
    total_distance += distances[individual[-1]][individual[0]]
    return 1/total_distance

# Generate a random individual
def generate_individual():
    individual = list(range(num_cities))
    random.shuffle(individual)
    return individual

# Generate a population of individuals
def generate_population():
    population = []
    for i in range(population_size):
        population.append(generate_individual())
    return population

# Select two parents from the population
def selection(population):
    fitnesses = [fitness(individual) for individual in population]
    total_fitness = sum(fitnesses)
    probabilities = [fitness/total_fitness for fitness in fitnesses]
    parent1, parent2 = random.choices(population, probabilities, k=2)
    return parent1, parent2

# Crossover the two parents to generate a child
def crossover(parent1, parent2):
    child = [-1] * num_cities
    start = random.randint(0, num_cities-1)
    end = random.randint(0, num_cities-1)
    if start > end:
        start, end = end, start
    for i in range(start, end+1):
        child[i] = parent1[i]
    for i in range(num_cities):
        if parent2[i] not in child:
            for j in range(num_cities):
                if child[j] == -1:
                    child[j] = parent2[i]
                    break
    return child

# Mutate an individual
def mutation(individual):
    for i in range(num_cities):
        if random.random() < mutation_rate:
            j = random.randint(0, num_cities-1)
            individual[i], individual[j] = individual[j], individual[i]
    return individual

# Run the genetic algorithm
def run_ga():
    # Generate initial population
    population = generate_population()
    
    # Run generations
    for gen in range(generations):
        print(f"Generation {gen+1}")
        new_population = []
        
        # Elitism - keep the best individual
        best_individual = max(population, key=fitness)
        new_population.append(best_individual)
        
        # Crossover and mutate to generate new population
        while len(new_population) < population_size:
            parent1, parent2 = selection(population)
            child = crossover(parent1, parent2)
            child = mutation(child)
            new_population.append(child)
        
        # Update population
        population = new_population
    
    # Output best individual
    best_individual = max(population, key=fitness)
    print(f"Best individual: {best_individual}")
    print(f"Fitness: {fitness(best_individual)}")

# Run the program
run_ga()
