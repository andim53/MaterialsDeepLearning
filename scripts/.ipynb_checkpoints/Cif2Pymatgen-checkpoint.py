from pymatgen.io.cif import CifParser
from ase import Atoms
import numpy as np


def convert(df):
    import pandas as pd
    from pymatgen.io.cif import CifParser
    from ase import Atoms
    import numpy as np

    structures = []

    for n, cif in enumerate(np.array(df['structure'])):
        parser = CifParser.from_string(cif)
        structure = parser.get_structures()

        structures.append(structure)

    df['structures_convert'] = structures
    
    return df
