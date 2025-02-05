# Sum of All Even Numbers in a List:
def sum_even(numbers):
    return sum(num for num in numbers if num % 2 == 0)
print(sum_even([1, 2, 3, 4, 5, 6]))
