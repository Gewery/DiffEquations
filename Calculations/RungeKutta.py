from Calculations.CalculationMethod import CalculationMethod
import math


class RungeKutta(CalculationMethod):
    def calculate(self, x0, y0, tox, step, **kwargs):
        points = []
        points.append((x0, y0))
        x = x0
        y = y0
        while x <= tox:
            k1 = self.__func(x, y)
            k2 = self.__func(x + step/2, y + step*k1/2)
            k3 = self.__func(x + step/2, y + step*k2/2)
            k4 = self.__func(x + step, y + step * k3)
            y = y + (k1 + 2 * k2 + 2 * k3 + k4) * step / 6
            x = x + step
            points.append((x, y))

        return points

    def __func(self, x, y):
        return math.cos(x) - y
