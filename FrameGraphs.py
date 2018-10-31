from tkinter import *
#from Graph import Graph
import math
from Graph import Graph


class FrameGraphs:

    background_color = "#20232a"

    def __init__(self, root):
        topframe = Frame(root, background=self.background_color)
        topframe.pack(fill=BOTH, expand=1)

        self.canvas = Canvas(topframe, background=self.background_color, highlightthickness=0)
        self.frame = Frame(self.canvas, background=self.background_color)
        scrollbar = Scrollbar(topframe, orient='vertical', command=self.canvas.yview)
        self.canvas.config(yscrollcommand=scrollbar.set)

        scrollbar.pack(side=RIGHT, fill=Y)
        self.canvas.pack(side=LEFT, fill=BOTH, expand=1)
        self.canvas.update()

        self.frame.config(height=self.canvas.winfo_height(), width=self.canvas.winfo_width())
        self.window = self.canvas.create_window((0, 0), window=self.frame, anchor=NW, width=self.canvas.winfo_width())

        self.frame.bind('<Configure>', self.scroll)
        self.canvas.bind('<Configure>', self.change_window_size)
        self.canvas.bind_all('<MouseWheel>', self._on_mousewheel)

        self.graph_1 = Graph(self.frame)
        self.graph_2 = Graph(self.frame)
        self.graph_3 = Graph(self.frame)

        #b = Button(text="draw", command=self.draw)
        #b.pack()

    def _on_mousewheel(self, event):
        self.canvas.yview_scroll(int(-1 * (event.delta / 120)), "units")

    def scroll(self, event):
        self.canvas.configure(scrollregion=self.canvas.bbox('all'))

    def change_window_size(self, event):
        self.canvas.itemconfig(self.window, width=self.canvas.winfo_width())

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