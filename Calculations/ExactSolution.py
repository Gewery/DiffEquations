from Calculations.CalculationMethod import CalculationMethod
import math


class ExactSolution(CalculationMethod):
    const = 1

    def calculate(self, x0, y0, tox, h, **kwargs):
        if x0 >= tox: return []
        self.const = self.__calculate_const(x0, y0) # const = 0.8402572149116814
        points = []
        x = x0
        while x <= tox:
            points.append((x, self.__func(x)))
            x += h
        return points

    def __calculate_const(self, x0, y0):
        return -(-y0 + math.sin(x0) / 2 + math.cos(x0) / 2) / math.exp(-x0)

    def __func(self, x):
        return self.const * math.exp(-x) + math.sin(x) / 2 + math.cos(x) / 2
