class fibonacci_sequence:
    def __init__(self, n):
        self.length = n
        self.i = 0
        self.fib_l = [1, 1]

    def __next__(self):
        if self.i < self.length:
            if self.i in [0, 1]:
                self.i += 1
                return 1
            else:
                a = self.fib_l[self.i-2] + self.fib_l[self.i-1]
                self.fib_l.append(a)
                self.i += 1
                return a
        else:
            raise StopIteration

    def __iter__(self):
        return self

fib = fibonacci_sequence(9)

for i in fib:
    print(i)
