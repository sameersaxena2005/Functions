    # Fibonacci Iterator Class:
class Fibonacci:
    def __init__(self, max_terms):
        self.a, self.b = 0, 1
        self.count = 0
        self.max_terms = max_terms

    def __iter__(self):
        return self

    def __next__(self):
        if self.count >= self.max_terms:
            raise StopIteration
        self.a, self.b = self.b, self.a + self.b
        self.count += 1
        return self.a

fib = Fibonacci(10)
print(list(fib))
