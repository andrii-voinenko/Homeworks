non_unique = ["John Dow", "John Dow", "Marta Dow", "Victor Blood", "Marta Dow"]
unique = []

for name in non_unique:
    if name not in unique:
        unique.append(name)

print(unique)
