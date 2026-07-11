from chemistry.similarity import similarity

smiles1 = input("First SMILES: ")
smiles2 = input("Second SMILES: ")

print("\nSimilarity:", similarity(smiles1, smiles2))