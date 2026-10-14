# Create an initial list of cities
cities = ["tokyo", "paris", "cairo", "new york", "sydney"]
print(f"Original list: {cities}")

# 1. Accessing an element using an index
print(f"The first city in the list is: {cities[0].title()}")

# 2. Modifying an element in a list
cities[1] = "london"
print(f"Modified list (replaced 'paris' with 'london'): {cities}")

# 3. Adding an item to the end using append()
cities.append("rio de janeiro")
print(f"After append(): {cities}")

# 4. Inserting an item at a specific index using insert()
cities.insert(2, "mumbai")
print(f"After insert(): {cities}")

# 5. Removing an item using the del statement
del cities[0]
print(f"After del (removed index 0): {cities}")

# 6. Removing an item using pop() (and retaining its value)
popped_city = cities.pop()
print(f"After pop() (removed '{popped_city}'): {cities}")

# 7. Removing an item by value using remove()
cities.remove("cairo")
print(f"After remove('cairo'): {cities}")

# 8. Temporarily sorting a list using sorted()
print(f"Temporarily sorted list: {sorted(cities)}")
print(f"List is still in its original order: {cities}")

# 9. Temporarily sorting a list in reverse using sorted(reverse=True)
print(f"Temporarily reverse-sorted list: {sorted(cities, reverse=True)}")

# 10. Permanently reversing the order of the list using reverse()
cities.reverse()
print(f"After reverse() (permanently flipped): {cities}")

# 11. Permanently sorting the list alphabetically using sort()
cities.sort()
print(f"After sort() (permanently sorted alphabetically): {cities}")

# 12. Permanently sorting the list in reverse alphabetical order using sort(reverse=True)
cities.sort(reverse=True)
print(f"After sort(reverse=True): {cities}")

# 13. Finding the length of a list using len()
print(f"The final list has {len(cities)} cities remaining.")