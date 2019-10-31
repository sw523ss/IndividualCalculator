def addition (a, b):
    return a + b


class Calculator:
    result = 0

    def __init__(self):
        x = 3 + 3
        self.result = x;
        pass

    def add(self, a, b):
        self.result = addition(a, b)
        return self.result