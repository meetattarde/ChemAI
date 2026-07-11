from chemistry.lipinski import lipinski_analysis

smiles = input("Enter SMILES: ")

result = lipinski_analysis(smiles)

print(result)