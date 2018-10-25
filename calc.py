import numpy as np

class calculator:

    def __init__(self):
        self.name = "calculator"

    def add(self, a, b):
        return np.add(a, b)

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return np.multiply(a, b)

    def division(self, a, b):
        if b != 0: 
            return a / b
        else:
            raise ValueError("division by 0!")