names = ['Lavi','Kanak','Priyanka','Kuldeep']
print(f"Hello, {names[0]}, how are you doing? You are invited to dinner")
print(f"Hello, {names[1]}, how are you doing? You are invited to dinner")
print(f"Hello, {names[2]}, how are you doing? You are invited to dinner")
print(f"Hello, {names[3]}, how are you doing? You are invited to dinner")
print(f'''{names[3]} cant make it.
Sorry''')
names.pop()
names.append('Deepak')
print(f"Hello, {names[0]}, how are you doing? You are still invited to the dinner")
print(f"Hello, {names[1]}, how are you doing? You are still invited to the dinner")
print(f"Hello, {names[2]}, how are you doing? You are still invited to the dinner")
print(f"Hello, {names[3]}, how are you doing? You are still invited to the dinner")