from tkinter import *
import time


class Graph:

    background_color = "#20232a"
    init_graphs = [] # list of lists of tuples (x_i, y_i)
    bounded_graphs = [] # only points which exists on rectangle (fromx, fromy)x(tox, toy)
    linecolors = [] # list of strings

    fromx, fromy = 0, 0
    tox, toy = 100, 100

    def __init__(self, root):
        self.root = root
        self.root.update()
        self.canvas = Canvas(root, height=int(root.winfo_width()//2), bg=self.background_color)
        self.canvas.pack(fill=X, padx=10, pady=70) #TODO change padding to see more graphs
        self.canvas.update()

        self.draw_axes()
        self.canvas.bind('<Configure>', self.update) # Redraw if size of window has changed

    def update(self, event):
        self.canvas.delete('all')
        self.canvas.config(height=self.root.winfo_width() // 2)
        self.draw_axes()
        #TODO: Draw all plots

    def draw_axes(self):
        self.canvas.create_line(20 - 1, self.convertY(20), self.canvas.winfo_width() - 5, self.convertY(20), width=3,
                                fill="white")# OX axis
        self.canvas.create_line(self.canvas.winfo_width() - 5, self.convertY(20 - 1), self.canvas.winfo_width() - 5 - 10,
                                self.convertY(20 + 7), width=2, fill="white")# arrow on OX
        self.canvas.create_line(self.canvas.winfo_width() - 5, self.convertY(20 + 1), self.canvas.winfo_width() - 5 - 10,
                                self.convertY(20 - 7), width=2, fill="white")

        self.canvas.create_line(20, self.convertY(20 - 1), 20, self.convertY(self.canvas.winfo_height() - 5), width=3,
                                fill="white")# OY axis
        self.canvas.create_line(20 + 1, self.convertY(self.canvas.winfo_height() - 5), 20 - 7,
                                self.convertY(self.canvas.winfo_height() - 5 - 10), width=2,
                                fill="white")# arrow on OY
        self.canvas.create_line(20 - 1, self.convertY(self.canvas.winfo_height() - 5), 20 + 7,
                                self.convertY(self.canvas.winfo_height() - 5 - 10), width=2,
                                fill="white")

        n = 15
        dx = (self.tox - self.fromx) / n
        if dx > 10:
            dx //= 10
            dx *= 10
        elif dx > 1:
            dx = int(dx)
        #TODO: write else

        first_mark = self.fromx
        if self.fromx > 1:
            first_mark = (first_mark + 9) // 10
            first_mark *= 10

        px = 20 + self.scaleX(first_mark - self.fromx)
        x = first_mark
        while px <= self.canvas.winfo_width() - 5:
            self.canvas.create_line(px, self.convertY(15), px, self.convertY(25), width=1, fill="white")
            self.canvas.create_text(px, self.convertY(10), text='%5.1f'%x, fill="yellow")
            x += dx
            px += self.scaleX(dx)

    def scaleX(self, x):
        return x * (self.canvas.winfo_width() - 5 - 10) / (self.tox - self.fromx)

    def rescale(self, fromx, fromy, tox, toy):
        self.bounded_graphs.clear()
        for plot in self.init_graphs:
            b_plot = list()
            added = False
            for i in range(len(plot)):
                if fromx <= plot[i][0] <= tox and fromy <= plot[i][1] <= toy:
                    b_plot.append(plot[i])
                    if not added and i != 0:
                        b_plot.append(plot[i - 1]) #add previous point if current added
                    added = True
                elif added:
                    b_plot.append(plot[i]) #add point if previous one was added
                    added = False

            self.bounded_graphs.append(b_plot)

    def draw_graph(self, graph_points, color):
        pass

    def convertY(self, y):
        return self.canvas.winfo_height() - y
