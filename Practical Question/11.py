# Bookshop Accounting Routine:    

orders = [
    [34587, "Learning Python", 4, 40.95],
    [98762, "Python Cookbook", 5, 56.80],
    [77226, "Data Science", 3, 32.95],
    [88112, "Machine Learning", 3, 24.99]
]

result = [(order[0], order[2] * order[3] + (10 if order[2] * order[3] < 100 else 0)) for order in orders]
print(result)
