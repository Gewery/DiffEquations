import tkinter


class Graph:
    points = []
    step = 0
    fromx = 0
    tox = 100

    function_plane = None
    local_error_plane = None
    global_error_plane = None

    def __init__(self, function_plane, local_error_plane, global_error_plane, method):
        self.function_plane = function_plane
        self.local_error_plane = local_error_plane
        self.global_error_plane = global_error_plane

    def calculate_points(self, method):
        points = method.calculate()