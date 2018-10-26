from tkinter import *
import time


class Graph:

    background_color = "#20232a"
    init_graphs = [] # list of lists of tuples (x_i, y_i)
    bounded_graphs = [] # only points which exists on rectangle (fromx, fromy)x(tox, toy)
    linecolors = [] # list of strings

    fromx, fromy = 2.32, 4
    tox, toy = 2.5, 10

    def __init__(self, root):
        self.root = root
        self.root.update()
        self.canvas = Canvas(root, height=int(root.winfo_width()//2), bg=self.background_color)
        self.canvas.pack(fill=X, padx=10, pady=70) #TODO change padding to see more graphs
        self.canvas.update()

        self.shift_OX_up = 30
        self.shift_OX_right = 30
        self.shift_OY_up = 30
        self.shift_OY_right = 30

        self.accuracy = 3 #TODO: deal with it

        self.draw_axes()
        self.canvas.bind('<Configure>', self.update) # Redraw if size of window has changed

    def update(self, event):
        self.canvas.delete('all')
        self.canvas.config(height=self.root.winfo_width() // 2)
        self.draw_axes()
        #TODO: Draw all plots

    def draw_axes(self):
        self.canvas.create_line(self.shift_OX_right - 1, self.convertY(self.shift_OX_up), self.canvas.winfo_width() - 5, self.convertY(self.shift_OX_up), width=3,
                                fill="white")# OX axis
        self.canvas.create_line(self.canvas.winfo_width() - 5, self.convertY(self.shift_OX_up - 1), self.canvas.winfo_width() - 5 - 10,
                                self.convertY(self.shift_OX_up + 7), width=2, fill="white")# arrow on OX
        self.canvas.create_line(self.canvas.winfo_width() - 5, self.convertY(self.shift_OX_up + 1), self.canvas.winfo_width() - 5 - 10,
                                self.convertY(self.shift_OX_up - 7), width=2, fill="white")

        self.canvas.create_line(self.shift_OY_right, self.convertY(self.shift_OY_up - 1), self.shift_OY_right, self.convertY(self.canvas.winfo_height() - 5), width=3,
                                fill="white")# OY axis
        self.canvas.create_line(self.shift_OY_right + 1, self.convertY(self.canvas.winfo_height() - 5), self.shift_OY_right - 7,
                                self.convertY(self.canvas.winfo_height() - 5 - 10), width=2,
                                fill="white")# arrow on OY
        self.canvas.create_line(self.shift_OY_right - 1, self.convertY(self.canvas.winfo_height() - 5), self.shift_OY_right + 7,
                                self.convertY(self.canvas.winfo_height() - 5 - 10), width=2,
                                fill="white")

        #Mark OX:
        dist_text_from_OX = 12

        integer = True
        n = 15
        dx = (self.tox - self.fromx) / n
        if dx >= 5:
            dx //= 5
            dx *= 5
        elif dx >= 1:
            dx = int(dx)
        else:
            integer = False

        first_mark_ox = self.fromx
        if self.fromx >= 1 and (4 + first_mark_ox) // 5 < self.tox and integer:
            first_mark_ox = (4 + first_mark_ox) // 5
            first_mark_ox *= 5
        else:
            integer = False

        self.accuracy = 3 # to 3rd number after .

        px = self.shift_OX_right + self.scaleX(first_mark_ox - self.fromx) # calculate x in pixels
        x = first_mark_ox
        while px < self.canvas.winfo_width() - 5:
            self.canvas.create_line(px, self.convertY(self.shift_OX_up - 5), px, self.convertY(self.shift_OX_up + 5), width=1, fill="white")
            self.canvas.create_text(px, self.convertY(self.shift_OX_up - dist_text_from_OX), text=int(x) if integer else int(x*(10**self.accuracy))/(10**self.accuracy), fill="white")
            x += dx
            px += self.scaleX(dx)


        # Mark OY:

        dist_text_from_OY = 15

        integer = True
        n = 10
        dy = (self.toy - self.fromy) / n
        if dy >= 5:
            dy //= 5
            dy *= 5
        elif dy >= 1:
            dy = int(dy)
        else:
            integer = False

        first_mark_oy = self.fromy
        if self.fromy >= 1 and (4 + first_mark_oy) // 5 < self.toy and integer:
            first_mark_oy = (4 + first_mark_oy) // 5
            first_mark_oy *= 5
        else:
            integer = False

        self.accuracy = 3  # to 3rd number after .

        py = self.shift_OY_up + self.scaleY(first_mark_oy - self.fromy) # calculate y in pixels
        y = first_mark_oy
        while py < self.canvas.winfo_width() - 5:
            self.canvas.create_line(self.shift_OY_right - 5, self.convertY(py), self.shift_OX_right + 5, self.convertY(py), width=1, fill="white")
            self.canvas.create_text(self.shift_OY_right - dist_text_from_OY, self.convertY(py),
                                    text=int(y) if integer else int(y * (10 ** self.accuracy)) / (10 ** self.accuracy),# rounding
                                    fill="white")
            y += dy
            py += self.scaleY(dy)

    def scaleX(self, x):
        return x * (self.canvas.winfo_width() - 5 - 10) / (self.tox - self.fromx)

    def scaleY(self, y):
        return y * (self.canvas.winfo_height() - 5 - 10) / (self.toy - self.fromy)

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
