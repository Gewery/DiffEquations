import tkinter


class Graph:
    points = []
    line_color = 'red'

    exact_solution = None # for local errors

    step = 0.6
    x0 = 1
    y0 = 1
    tox = 9.5

    method = None
    plane = None

    def __init__(self, plane, method, line_color, exact_solution=None):
        self.exact_solution = exact_solution
        self.plane = plane
        self.method = method
        self.__calculate_points()
        self.line_color = line_color
        self.plane.add_graph(self)

    def __calculate_points(self):
        self.points = self.method.calculate(self.x0, self.y0, self.tox, self.step, exact_solution=self.exact_solution)

    def change_graph_settings(self, **kwargs):  # update planes after call this
        if 'x0' in kwargs: self.x0 = kwargs['x0']
        if 'y0' in kwargs: self.y0 = kwargs['y0']
        if 'step' in kwargs: self.step = kwargs['step']
        if 'tox' in kwargs: self.tox = kwargs['tox']
        self.__calculate_points()
