from chemistry.rings import ring_information

smiles = input("Enter SMILES: ")

info = ring_information(smiles)

print(info)