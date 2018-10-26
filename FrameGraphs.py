from tkinter import *
#from Graph import Graph
import math
from Graph import Graph


class FrameGraphs:

    background_color = "#20232a"

    def __init__(self, root):
        self.frame = Frame(root, background=self.background_color)
        self.frame.pack(fill=BOTH, expand=1)
        self.frame.pack_propagate(0)

        self.graph_1 = Graph(self.frame)

        b = Button(text="draw", command=self.draw)
        b.pack()
        #self.graph_2 = Graph(frame, dataList, "red")
        #self.graph_3 = Graph(frame, dataList, "red")

    def draw(self):
        dataList = []
        x = 0
        for i in range(100):
            dataList.append((x, 1 + math.sin(x)))
            x += 0.1

        self.graph_1.change_boundaries(0, 0, 10, 2.5)
        self.graph_1.add_graph(dataList, "blue")

    def resize_graphs(self):
        pass
        #self.graph_1.draw_piece()
        #self.graph_2.draw_piece()