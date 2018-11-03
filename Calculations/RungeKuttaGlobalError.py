from Calculations.CalculationMethod import CalculationMethod
from Calculations.RungeKuttaLocalError import RungeKuttaLocalError
from Calculations.ExactSolution import ExactSolution


class RungeKuttaGlobalError(CalculationMethod):
    def calculate(self, x0, y0, tox, h, **kwargs):
        if x0 >= tox: return []
        print(kwargs['max_division'])
        points = []

        div = kwargs['min_division']
        while div <= kwargs['max_division']:
            cur_h = (tox - x0) / div
            exact_solution_points = ExactSolution().calculate(x0, y0, tox, cur_h)
            local_error_points = RungeKuttaLocalError().calculate(x0, y0, tox, cur_h, exact_solution=exact_solution_points)
            max_local_error = 0
            for pnt in local_error_points:
                max_local_error = max(max_local_error, abs(pnt[1]))

            points.append((div, max_local_error))

            div += 1

        return points
