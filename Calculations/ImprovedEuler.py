from Calculations.CalculationMethod import CalculationMethod
import math


class ImprovedEuler(CalculationMethod):
    def calculate(self, x0, y0, tox, h, **kwargs):
        if x0 >= tox: return []
        points = []
        x = x0
        y = y0
        while x <= tox:
            points.append((x, y))
            prev_y = y
            y = y + h * self.__func(x, y)
            y = prev_y + h * (self.__func(x, prev_y) + self.__func(x + h, y)) / 2
            x += h

        return points

    def __func(self, x, y):
        return math.cos(x) - y
