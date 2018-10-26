from tkinter import *
#from Graph import Graph
import math
from Graph import Graph


class FrameGraphs:

    background_color = "#20232a"

    def __init__(self, root):
        frame = Frame(root, background=self.background_color)
        frame.pack(fill=BOTH, expand=1)
        frame.pack_propagate(0)

        dataList = []

        x = 0
        for i in range(100):
            dataList.append((x, math.sin(x) + 1))
            x += 0.5

        graph_1 = Graph(frame)
        #graph_1.draw_plots()
        #self.graph_2 = Graph(frame, dataList, "red")
        #self.graph_3 = Graph(frame, dataList, "red")

    def resize_graphs(self):
        pass
        #self.graph_1.draw_piece()
        #self.graph_2.draw_piece()