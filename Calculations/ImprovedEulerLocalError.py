from Calculations.CalculationMethod import CalculationMethod
import math


class ImprovedEulerLocalError(CalculationMethod):
    def calculate(self, x0, y0, tox, step, **kwargs):
        points = []
        points.append((x0, 0))
        x = x0
        y = y0
        i = 1
        while x <= tox:
            prev_y = y
            y = y + step * self.__func(x, y)
            y = prev_y + step * (self.__func(x, prev_y) + self.__func(x + step, y)) / 2
            x += step
            points.append((x, kwargs['exact_solution'][i][1] - y))
            i += 1

        return points

    def __func(self, x, y):
        return math.cos(x) - y
