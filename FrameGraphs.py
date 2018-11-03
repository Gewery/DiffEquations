from tkinter import *
from Calculations.ExactSolution import ExactSolution

from Calculations.Euler import Euler
from Calculations.EulerLocalError import EulerLocalError
from Calculations.EulerGlobalError import EulerGlobalError

from Calculations.ImprovedEuler import ImprovedEuler
from Calculations.ImprovedEulerLocalError import ImprovedEulerLocalError
from Calculations.ImprovedEulerGlobalError import ImprovedEulerGlobalError

from Calculations.RungeKutta import RungeKutta
from Calculations.RungeKuttaLocalError import RungeKuttaLocalError
from Calculations.RungeKuttaGlobalError import RungeKuttaGlobalError


from Graph import Graph
import math
from Plane import Plane


class FrameGraphs:

    background_color = "#20232a"

    exact_solution_function_graph = None
    euler_function_graph = None
    euler_local_error_graph = None
    euler_global_error_graph = None
    improved_euler_function_graph = None
    improved_euler_local_error_graph = None
    improved_euler_global_error_graph = None
    runge_kutta_function_graph = None
    runge_kutta_local_error_graph = None
    runge_kutta_global_error_graph = None

    def __init__(self, root):
        topframe = Frame(root, background=self.background_color)
        topframe.pack(fill=BOTH, expand=1)

        self.canvas = Canvas(topframe, background=self.background_color, highlightthickness=0)
        self.frame = Frame(self.canvas, background=self.background_color)
        scrollbar = Scrollbar(topframe, orient='vertical', command=self.canvas.yview)
        self.canvas.config(yscrollcommand=scrollbar.set)

        #scrollbar.pack(side=RIGHT, fill=Y)  # Hided Scrollbar
        self.canvas.pack(side=LEFT, fill=BOTH, expand=1)
        self.canvas.update()

        self.frame.config(height=self.canvas.winfo_height(), width=self.canvas.winfo_width())
        self.window = self.canvas.create_window((0, 0), window=self.frame, anchor=NW, width=self.canvas.winfo_width())

        self.frame.bind('<Configure>', self.scroll)
        self.canvas.bind('<Configure>', self.change_window_size)
        self.canvas.bind_all('<MouseWheel>', self._on_mousewheel)

        self.function_plane = Plane(self.frame, 'Function')
        self.local_error_plane = Plane(self.frame, 'Local error')
        self.global_error_plane = Plane(self.frame, 'Total error')

        self.create_graphs()

    def _on_mousewheel(self, event):
        self.canvas.yview_scroll(int(-1 * (event.delta / 120)), "units")

    def scroll(self, event):
        self.canvas.configure(scrollregion=self.canvas.bbox('all'))

    def change_window_size(self, event):
        self.canvas.itemconfig(self.window, width=self.canvas.winfo_width())

    def draw_exact_solution_graph(self):
        self.exact_solution_function_graph.draw_graph()

    def remove_exact_solution_graph(self):
        self.exact_solution_function_graph.remove_graph()

    def draw_euler_graphs(self):
        self.euler_function_graph.draw_graph()
        self.euler_local_error_graph.draw_graph()
        self.euler_global_error_graph.draw_graph()

    def remove_euler_graphs(self):
        self.euler_function_graph.remove_graph()
        self.euler_local_error_graph.remove_graph()
        self.euler_global_error_graph.remove_graph()

    def draw_improved_euler_graphs(self):
        self.improved_euler_function_graph.draw_graph()
        self.improved_euler_local_error_graph.draw_graph()
        self.improved_euler_global_error_graph.draw_graph()

    def remove_improved_euler_graphs(self):
        self.improved_euler_function_graph.remove_graph()
        self.improved_euler_local_error_graph.remove_graph()
        self.improved_euler_global_error_graph.remove_graph()

    def draw_runge_kutta_graphs(self):
        self.runge_kutta_function_graph.draw_graph()
        self.runge_kutta_local_error_graph.draw_graph()
        self.runge_kutta_global_error_graph.draw_graph()

    def remove_runge_kutta_graphs(self):
        self.runge_kutta_function_graph.remove_graph()
        self.runge_kutta_local_error_graph.remove_graph()
        self.runge_kutta_global_error_graph.remove_graph()

    def change_graphs_settings(self, kwargs):
        self.exact_solution_function_graph.change_graph_settings(kwargs)
        kwargs['exact_solution'] = self.exact_solution_function_graph.points

        self.euler_function_graph.change_graph_settings(kwargs)
        self.euler_local_error_graph.change_graph_settings(kwargs)
        self.euler_global_error_graph.change_graph_settings(kwargs)
        self.improved_euler_function_graph.change_graph_settings(kwargs)
        self.improved_euler_local_error_graph.change_graph_settings(kwargs)
        self.improved_euler_global_error_graph.change_graph_settings(kwargs)
        self.runge_kutta_function_graph.change_graph_settings(kwargs)
        self.runge_kutta_local_error_graph.change_graph_settings(kwargs)
        self.runge_kutta_global_error_graph.change_graph_settings(kwargs)

        self.function_plane.update()
        self.local_error_plane.update()
        self.global_error_plane.update()

    def create_graphs(self):
        self.exact_solution_function_graph = Graph(self.function_plane, ExactSolution(), 'white')

        self.euler_function_graph = Graph(self.function_plane, Euler(), 'blue')
        self.euler_local_error_graph = Graph(self.local_error_plane, EulerLocalError(), 'blue', self.exact_solution_function_graph.points)
        self.euler_global_error_graph = Graph(self.global_error_plane, EulerGlobalError(), 'blue')

        self.improved_euler_function_graph = Graph(self.function_plane, ImprovedEuler(), 'yellow')
        self.improved_euler_local_error_graph = Graph(self.local_error_plane, ImprovedEulerLocalError(), 'yellow', self.exact_solution_function_graph.points)
        self.improved_euler_global_error_graph = Graph(self.global_error_plane, ImprovedEulerGlobalError(), 'yellow')

        self.runge_kutta_function_graph = Graph(self.function_plane, RungeKutta(), 'red')
        self.runge_kutta_local_error_graph = Graph(self.local_error_plane, RungeKuttaLocalError(), 'red', self.exact_solution_function_graph.points)
        self.runge_kutta_global_error_graph = Graph(self.global_error_plane, RungeKuttaGlobalError(), 'red')
