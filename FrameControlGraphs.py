from tkinter import *
import time


class FrameControlGraphs:
    frame_width_1 = 100
    background_color = "#232730"
    graphs_expanded = False
    frame_graphs = None

    def __init__(self, root, images):
        self.frame = Frame(root, background=self.background_color, width=self.frame_width_1)
        self.frame.pack(side=LEFT, fill=Y)
        self.frame.pack_propagate(0)

        self.label_graphs_image = images.label_graphs_PhotoImage

        self.label_graphs = Label(self.frame, image=self.label_graphs_image, bg=self.background_color, bd=0,
                               state="normal",
                               activebackground=self.background_color)
        self.label_graphs.pack(pady=10, padx=7)

        exact_solution_button = Button(self.frame, text='Exact soltion', command=self.draw_exact_solution_graph)
        exact_solution_button.pack()

        euler_button = Button(self.frame, text='Euler', command=self.draw_euler_graphs)
        euler_button.pack()

        improved_euler_button = Button(self.frame, text='Improved Euler', command=self.draw_improved_euler_graphs)
        improved_euler_button.pack()

        runge_kutta_button = Button(self.frame, text='Runge-Kutta', command=self.draw_runge_kutta_graphs)
        runge_kutta_button.pack()

    def set_frame_graphs(self, frame_graphs):
        self.frame_graphs = frame_graphs

    def draw_exact_solution_graph(self):
        self.frame_graphs.draw_exact_solution_graph()

    def draw_euler_graphs(self):
        self.frame_graphs.draw_euler_graphs()

    def draw_improved_euler_graphs(self):
        self.frame_graphs.draw_improved_euler_graphs()

    def draw_runge_kutta_graphs(self):
        self.frame_graphs.draw_runge_kutta_graphs()


