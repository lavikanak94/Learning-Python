# Start with your list of pizzas from Exercise 4-1
pizzas = ["pepperoni", "margherita", "BBQ chicken"]

# Make a copy of the list and call it friend_pizzas
friend_pizzas = pizzas.copy()

# Add a new pizza to the original list
pizzas.append("hawaiian")

# Add a different pizza to the friend_pizzas list
friend_pizzas.append("four cheese")

# Print the first list
print("My favorite pizzas are:")
for pizza in pizzas:
    print(pizza.title())

print()

# Print the second list
print("My friend’s favorite pizzas are:")
for friend_pizza in friend_pizzas:
    print(friend_pizza.title())