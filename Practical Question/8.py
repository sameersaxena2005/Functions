# Sort List of Tuples by Second Element Using Lambda:
data = [(1, 5), (2, 3), (3, 8)]
sorted_data = sorted(data, key=lambda x: x[1])
print(sorted_data)
