# 1. Initialize an empty list to store the cubes
cubes = []

# 2. Use a for loop to calculate the cube for integers 1 through 10
for number in range(1, 11):
    cube = number ** 3
    cubes.append(cube)

# 3. Use another for loop to print out each value
for cube in cubes:
    print(cube)
