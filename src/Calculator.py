def addition (a, b):
    return a + b

def subtraction(a, b):
    return a - b

def multiplication(a, b):
    return a * b

def division (a, b):
    return a / b

def square (a):
    return a ** 2

def squareroot(a):
    return a ** 0.5


class Calculator:
    result = 0

    def __init__(self):
        x = 3 + 3
        self.result = x;
        pass

    def add(self, a, b):
        a = float(a)
        b = float(b)
        self.result = addition(a, b)
        return self.result

    def subtract(self, a, b):
        a = float(a)
        b = float(b)
        self.result = subtraction(a, b)
        return self.result

    def multipy(self, a, b):
        a = float(a)
        b = float(b)
        self.result = multiplication(a, b)
        return self.result

    def divide(self, a, b):
        self.result = division(a, b)
        return self.result

    def square(self, a, ):
        self.result = square(a)
        return self.result

    def squareroot(self, a, ):
        self.result = squareroot(a)
        return self.result

