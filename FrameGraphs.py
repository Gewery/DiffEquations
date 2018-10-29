from tkinter import *
#from Graph import Graph
import math
from Graph import Graph


class FrameGraphs:

    background_color = "#20232a"

    def __init__(self, root):
        topframe = Frame(root, background=self.background_color)
        topframe.pack(fill=BOTH, expand=1)

        scrollbar = Scrollbar(topframe, orient='vertical')
        scrollbar.pack(side=RIGHT, fill=Y)

        self.canvas = Canvas(topframe, yscrollcommand=scrollbar.set, borderwidth=0, highlightthickness=0, background=self.background_color)
        self.canvas.pack(side=LEFT, fill=BOTH, expand=1)

        scrollbar.config(command=self.canvas.yview)

        self.canvas.xview_moveto(0)
        self.canvas.yview_moveto(0)

        self.frame = Frame(self.canvas, background=self.background_color)
        # self.frame.pack(fill=BOTH, expand=1)
        # self.frame.pack_propagate(0)

        self.canvas.update()
        self.window = self.canvas.create_window((0, 0), window=self.frame, anchor=NW, height=self.canvas.winfo_height(), width=self.canvas.winfo_width())
        self.canvas.bind('<Configure>', self.change_window_size)

        self.canvas.update()
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))

        self.graph_1 = Graph(self.frame)
        #self.graph_2 = Graph(self.frame)

        #b = Button(text="draw", command=self.draw)
        #b.pack()
        #self.graph_2 = Graph(frame, dataList, "red")
        #self.graph_3 = Graph(frame, dataList, "red")

    def change_window_size(self, event):
        self.canvas.itemconfig(self.window, height=self.canvas.winfo_height(), width=self.canvas.winfo_width())

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