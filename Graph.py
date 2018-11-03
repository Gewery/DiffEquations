import tkinter


class Graph:
    points = []
    line_color = 'red'

    exact_solution = None  # for local errors

    h = 0.6
    x0 = 1
    y0 = 1
    tox = 10

    min_division = 1  # min split of graph (for global errors)
    max_division = 2  # max split of graph (for global errors)

    method = None
    plane = None

    def __init__(self, plane, method, line_color, exact_solution=None):
        self.exact_solution = exact_solution
        self.plane = plane
        self.method = method
        self.__calculate_points()
        self.line_color = line_color

    def draw_graph(self):
        self.plane.add_graph(self)

    def remove_graph(self):
        self.plane.remove_graph(self)

    def __calculate_points(self):
        self.points = self.method.calculate(self.x0, self.y0, self.tox, self.h, exact_solution=self.exact_solution,
                                            min_division=self.min_division, max_division=self.max_division)

    def change_graph_settings(self, kwargs):  # update planes after call this
        if 'exact_solution' in kwargs: self.exact_solution = kwargs['exact_solution']
        if 'min_division' in kwargs: self.min_division = kwargs['min_division']
        if 'max_division' in kwargs: self.max_division = kwargs['max_division']
        if 'x0' in kwargs: self.x0 = kwargs['x0']
        if 'y0' in kwargs: self.y0 = kwargs['y0']
        if 'h' in kwargs: self.h = kwargs['h']
        if 'tox' in kwargs: self.tox = kwargs['tox']
        self.__calculate_points()
