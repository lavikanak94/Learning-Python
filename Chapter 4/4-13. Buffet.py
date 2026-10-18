# Store five basic foods in a tuple
buffet_foods = ("rice", "pasta", "chicken", "fries", "salad")

# Use a for loop to print each food on the original menu
print("Original menu:")
for food in buffet_foods:
  print(food)

# Try to modify one of the items (this raises a TypeError because tuples are immutable)
# buffet_foods[0] = "burger"

# The restaurant changes its menu, replacing two of the items with different foods
buffet_foods = ("rice", "pasta", "burger", "fish", "salad")

# Use a for loop to print each item on the revised menu
print("\nRevised menu:")
for food in buffet_foods:
  print(food)