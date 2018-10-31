from tkinter import *
import time


class FrameControlGraphs:
    frame_width_1 = 100
    background_color = "#232730"
    graphs_expanded = False

    def __init__(self, root, images):
        self.frame = Frame(root, background=self.background_color, width=self.frame_width_1)
        self.frame.pack(side=LEFT, fill=Y)
        self.frame.pack_propagate(0)

        self.label_graphs_image = images.label_graphs_PhotoImage

        self.label_graphs = Label(self.frame, image=self.label_graphs_image, bg=self.background_color, bd=0,
                               state="normal",
                               activebackground=self.background_color)
        self.label_graphs.pack(pady=10, padx=7)

        exact_solution_button = Button(text='Exact soltion', command=self.draw_exact_solution)

    def set_frame_graphs(self, frame_graphs):
        self.frame_graphs = frame_graphs

    def draw_exact_solution(self):
        points = []



