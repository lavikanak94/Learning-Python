my_foods = ['pizza', 'falafel', 'carrot cake', 'cannoli']

#both lists gets assigned the same list
friend_foods = my_foods[:]

print("My favorite foods are:")
for food in my_foods:
    print(food)

friend_foods.append('chicken')
print("\nMy friend's favorite foods are:")
for food in friend_foods:
    print(food)