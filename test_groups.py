from chemistry.functional_groups import detect_functional_groups

smiles = input("Enter SMILES: ")

groups = detect_functional_groups(smiles)

print("\nDetected Functional Groups:\n")

if groups:
    for group in groups:
        print("-", group)
else:
    print("None")