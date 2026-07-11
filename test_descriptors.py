from chemistry.descriptors import get_descriptors

smiles = input("Enter SMILES: ")

result = get_descriptors(smiles)

for key, value in result.items():
    print(f"{key}: {value}")