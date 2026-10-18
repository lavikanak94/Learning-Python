# 1. Create a list of numbers from one to one million
# (We use 1_000_001 because the upper bound in range() is exclusive)
numbers = list(range(1, 1000001))

# 2. Use min(), max() and sum()
print(f"Minimum value: {min(numbers)}")
print(f"Maximum value: {max(numbers)}")
print(f"Sum value: {sum(numbers)}")