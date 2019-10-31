def addition (a, b):
    return a + b


class Calculator:
    result = 0

    def add(self, a, b):
        self.result = addition(a, b)
        return self.result