import numpy as np
import logging


def compute_distances(a, b):
    return np.linalg.norm(np.array(a) - np.array(b))

def fitness_function(genotype, core_radius = 3.0, ideal_ligand_distance = 1.8):
    """
    This is just a sample fitness function I will be using to get
    an idea of how to implement this function generally - will be building on this function
    to create a true fitness function for a nanoparticle
    """
    core_atoms = [atom for atom in genotype if atom[0] == 'Au']
    ligand_atoms = [atom for atom in genotype if atom[0] =='S']

    if len(core_atoms) == 0:
        return 0.0


    core_positions = np.array([atom[1:] for atom in core_atoms])
    core_center = core_positions.mean(axis = 0)

    
    # ligand placement fitness

    ligand_scores = []
    for ligand in ligand_atoms:
        ligand_pos = np.array(ligand[1:])

        # find closest core atom
        distances = [compute_distances(ligand_pos, np.array(core[1:])) for core in core_atoms]
        min_dist = min(distances)


        # penalize if ligand is too close or too far
        distance_penalty = abs(min_dist - ideal_ligand_distance)

        # reward if ligand is pointing outward (radial vector from core center)

        radial_vector = ligand_pos - core_center
        norm_radial = np.linalg.norm(radial_vector)

        if norm_radial == 0:
            angle_score = 0
        else:
            direction = radial_vector / norm_radial
            angle_score = np.dot(direction, radial_vector / norm_radial)

        ligand_scores.append(np.exp(-distance_penalty) * angle_score)

    total_score = sum(ligand_scores)

    
    return total_score / max(1, len(ligand_atoms))
            
    
