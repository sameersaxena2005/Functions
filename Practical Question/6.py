# Generator for Powers of 2:
def power_of_2(n):
    for i in range(n + 1):
        yield 2 ** i

print(list(power_of_2(5)))
