from chemistry.reactions import reaction_sites

smiles = input("Enter SMILES: ")

atoms = reaction_sites(smiles)

for atom in atoms:
    print(atom)