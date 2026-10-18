def calculate_total(price, tax):
    """Calculate the final price including tax."""
    return price + (price * tax)

print(calculate_total(100, 0.08))
print()


names = ['alice', 'bob', 'charlie']

for name in names:
    print(f"Hello, {name.title()}!")
print()


def check_number(num):
    """Check if a number is even or odd."""
    if num % 2 == 0:
        print('Even')
    else:
        print('Odd')


check_number(15)