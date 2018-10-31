import tkinter


class Graph:
    points = []
    line_color = 'red'

    step = 1
    x0 = 1
    y0 = 1
    tox = 100

    method = None
    plane = None

    def __init__(self, plane, method, line_color):
        self.plane = plane
        self.method = method
        self.__calculate_points()
        self.line_color = line_color
        self.plane.add_graph(self)

    def __calculate_points(self):
        self.points = self.method.calculate(self.x0, self.y0, self.tox, self.step)

    def change_graph_settings(self, **kwargs):  # update planes after call this
        if 'x0' in kwargs: self.x0 = kwargs['x0']
        if 'y0' in kwargs: self.y0 = kwargs['y0']
        if 'step' in kwargs: self.step = kwargs['step']
        if 'tox' in kwargs: self.tox = kwargs['tox']
        self.__calculate_points()
