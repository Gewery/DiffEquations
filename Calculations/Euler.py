from Calculations.CalculationMethod import CalculationMethod
import math


class Euler(CalculationMethod):
    def calculate(self, x0, y0, tox, h, **kwargs):
        points = []
        x = x0
        y = y0
        while x <= tox:
            points.append((x, y))
            y = y + h * self.__func(x, y)
            x += h

        return points

    def __func(self, x, y):
        return math.cos(x) - y