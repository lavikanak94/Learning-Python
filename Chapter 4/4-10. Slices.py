# Original program list expanded to 7 items to have a clear middle
pizzas = ['pepperoni', 'hawaiian', 'veggie', 'margherita', 'bbq chicken', 'meat lovers', 'four cheese']

# Original program loop
print("My favorite pizzas are:")
for pizza in pizzas:
    print(f"- {pizza}")
print()

# --- NEW LINES ADDED FOR THE SLICES EXERCISE ---

# 1. Print the first three items
print("The first three items in the list are:")
print(pizzas[:3])

# 2. Print three items from the middle of the list
print("\nThree items from the middle of the list are:")
print(pizzas[2:5])

# 3. Print the last three items
print("\nThe last three items in the list are:")
print(pizzas[-3:])