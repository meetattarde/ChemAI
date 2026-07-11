from chemistry.properties import calculate_properties

properties = calculate_properties("c1ccccc1")

print("\n===== BENZENE PROPERTIES =====\n")

for key, value in properties.items():
    print(f"{key}: {value}")