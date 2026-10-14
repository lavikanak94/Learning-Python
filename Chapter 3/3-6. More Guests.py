names = ['Lavi','Kanak','Priyanka','Kuldeep']
print(f"Hello, {names[0]}, how are you doing? You are invited to dinner")
print(f"Hello, {names[1]}, how are you doing? You are invited to dinner")
print(f"Hello, {names[2]}, how are you doing? You are invited to dinner")
print(f"Hello, {names[3]}, how are you doing? You are invited to dinner")
print()

print(f'''{names[3]} cant make it.
Sorry''')
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
print()