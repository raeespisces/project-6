class Multiplier:
    def __init__(self, factor):
        self.factor = factor

    def __call__(self, value):
        return self.factor * value

# Usage
m = Multiplier(3)
print(callable(m))  # True
print(m(5))         # 15
    