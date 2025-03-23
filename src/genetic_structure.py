"""
What is the genotype in this context?

The data structure that best represents a nanoparticle design might include:

- Atom types
- Positions
- Size/Shape
- Surface Functionalization
- Crystallographic Features

"""

class NanoParticleGenotype:
    """
    TODO 
    """
    def __init__(self, elements, positions, radii, shape, surface_ligands):
        self.elements = elements
        self.positions = positions
        self.radii = radii
        self.shape = shape
        self.surface_ligands = surface_ligands

    def mutate(self):
        # add mutation logic here
        pass

    def crossover(self, other):
        # create new genotype from self and other
        pass

genotype = {
    "elements": ["Au", "Ag", "Pt"],
    "positions": [(0, 0, 0), (1, 1, 1), (2, 0, 2)],  # 3D positions
    "radii": [1.2, 1.5, 1.0],  # per-atom size
    "shape": "sphere",         # could also be 'cube', 'rod', etc.
    "surface_ligands": ["COOH", "NH2", None]
}
