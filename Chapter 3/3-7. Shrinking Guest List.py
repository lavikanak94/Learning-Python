names = ['Lavi','Kanak','Priyanka','Kuldeep']
print(f"Hello, {names[0]}, how are you doing? You are invited to dinner")
print(f"Hello, {names[1]}, how are you doing? You are invited to dinner")
print(f"Hello, {names[2]}, how are you doing? You are invited to dinner")
print(f"Hello, {names[3]}, how are you doing? You are invited to dinner")
print()

print(f'''{names[3]} can't make it.
Sorry''')
print()
names.pop()
names.append('Deepak')
print(f"Hello, {names[0]}, how are you doing? You are still invited to the dinner")
print(f"Hello, {names[1]}, how are you doing? You are still invited to the dinner")
print(f"Hello, {names[2]}, how are you doing? You are still invited to the dinner")
print(f"Hello, {names[3]}, how are you doing? You are still invited to the dinner")
print()

print("Hello everyone, We found a bigger table.")
print()

names.insert(0, "Kuber")
names.insert(len(names)//2, "Rishabh")
names.append("Anuj")
print(f"Hello, {names[0]}, how are you doing? You are still invited to the dinner")
print(f"Hello, {names[1]}, how are you doing? You are still invited to the dinner")
print(f"Hello, {names[2]}, how are you doing? You are still invited to the dinner")
print(f"Hello, {names[3]}, how are you doing? You are still invited to the dinner")
print(f"Hello, {names[4]}, how are you doing? You are still invited to the dinner")
print(f"Hello, {names[5]}, how are you doing? You are still invited to the dinner")
print(f"Hello, {names[6]}, how are you doing? You are still invited to the dinner")
print()

print("Sorry, we have space for only 2 guests.")
guest = names.pop()
print(f"{guest} we are sorry. We can't invite you to the dinner.")
guest = names.pop()
print(f"{guest} we are sorry. We can't invite you to the dinner.")
guest = names.pop()
print(f"{guest} we are sorry. We can't invite you to the dinner.")
guest = names.pop()
print(f"{guest} we are sorry. We can't invite you to the dinner.")
guest = names.pop()
print(f"{guest} we are sorry. We can't invite you to the dinner.")
print()

print(f"Hello, {names[0]}, how are you doing? You are still invited to the dinner")
print(f"Hello, {names[1]}, how are you doing? You are still invited to the dinner")
print()

del names[0]
del names[0]

print(names)