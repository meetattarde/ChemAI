from chemistry.atom_counter import count_atoms

smiles = input("Enter SMILES: ")

atoms = count_atoms(smiles)

print("\nAtoms Present\n")

for atom, count in atoms.items():
    print(f"{atom} : {count}")