from Calculations.CalculationMethod import CalculationMethod
import math


class RungeKuttaLocalError(CalculationMethod):
    def calculate(self, x0, y0, tox, h, **kwargs):
        if x0 >= tox: return []
        points = []
        x = x0
        y = y0
        i = 0
        while x <= tox:
            points.append((x, kwargs['exact_solution'][i][1] - y))
            k1 = self.__func(x, y)
            k2 = self.__func(x + h/2, y + h*k1/2)
            k3 = self.__func(x + h/2, y + h*k2/2)
            k4 = self.__func(x + h, y + h * k3)
            y = y + (k1 + 2 * k2 + 2 * k3 + k4) * h / 6
            x = x + h
            i += 1

        return points

    def __func(self, x, y):
        return math.cos(x) - y
