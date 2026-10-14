places = ["Switzerland","Japan","America", "San Francisco", "Miami"]
print(f"Original list : {places}")

print(f"Sorted list : {sorted(places)}")
print(f"Original list : {places}")

print(f"Sorted reverse list : {sorted(places, reverse=True)}")
print(f"Original list : {places}")

places.reverse()
print(f"Reversed list : {places}")

places.sort()
print(f"Sorted list : {places}")

sorted(places, reverse = True)
print(f"Reversed Alphabetical list : {places}")