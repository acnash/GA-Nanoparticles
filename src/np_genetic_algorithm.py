import numpy as np
import random

NUM_ATOMS = 10
POP_SIZE = 50
GENERATIONS = 100
MUTATION_RATE = 0.2

# Genotype = list of 3D coordinates
def random_particle():
    return [np.random.uniform(-5, 5, size=3) for _ in range(NUM_ATOMS)]

# Fitness = compactness (lower average distance to center)
def fitness(particle):
    coords = np.array(particle)
    center = coords.mean(axis=0)
    distances = np.linalg.norm(coords - center, axis=1)
    return -np.mean(distances)  # more compact = higher fitness

# Crossover: average each atom's position between two parents
def crossover(p1, p2):
    return [(a + b) / 2 for a, b in zip(p1, p2)]

# Mutation: randomly jitter atom positions
def mutate(particle):
    return [
        pos + np.random.normal(0, 0.5, size=3) if random.random() < MUTATION_RATE else pos
        for pos in particle
    ]

# Selection: weighted by fitness
def selection(population):
    scores = [fitness(p) for p in population]
    scores = [s - min(scores) + 1e-3 for s in scores]  # shift to positive
    return random.choices(population, weights=scores, k=2)

# Run the GA
def run_ga():
    population = [random_particle() for _ in range(POP_SIZE)]

    for gen in range(GENERATIONS):
        population = sorted(population, key=fitness, reverse=True)
        best = population[0]
        best_score = fitness(best)

        print(f"Generation {gen}: Best fitness = {best_score:.4f}")

        # Early stopping
        if -best_score < 0.5:
            print("Structure is very compact. Stopping early.")
            break

        # Next generation
        next_gen = []
        while len(next_gen) < POP_SIZE:
            p1, p2 = selection(population)
            child = crossover(p1, p2)
            child = mutate(child)
            next_gen.append(child)

        population = next_gen

    return best

# Visualize the result (optional, needs matplotlib)
def plot_structure(particle):
    import matplotlib.pyplot as plt
    from mpl_toolkits.mplot3d import Axes3D

    coords = np.array(particle)
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.scatter(coords[:,0], coords[:,1], coords[:,2], c='r', s=50)
    ax.set_title("Optimized Nanoparticle Structure")
    plt.show()

if __name__ == "__main__":
    best_particle = run_ga()
    plot_structure(best_particle)
