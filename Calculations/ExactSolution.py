from Calculations.CalculationMethod import CalculationMethod
import math

class ExactSolution(CalculationMethod):

    const = 0.8402572149116814

    def calculate(self, fromx, tox, step):
        points = []
        x = fromx
        while x <= tox:
            points.append((x, 3 + self.__func(x)))
            x += step
        print(points)
        return points

    def __func(self, x):
        return self.const * math.exp(-x) + math.sin(x) / 2 + math.cos(x) / 2
