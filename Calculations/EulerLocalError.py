from Calculations.CalculationMethod import CalculationMethod
import math


class EulerLocalError(CalculationMethod):
    def calculate(self, x0, y0, tox, h, **kwargs):
        if x0 > tox: return []
        points = []
        x = x0
        y = y0
        i = 0
        while x <= tox:
            points.append((x, kwargs['exact_solution'][i][1] - y))
            y = y + h * self.__func(x, y)
            x += h
            i += 1

        return points

    def __func(self, x, y):
        return math.cos(x) - y