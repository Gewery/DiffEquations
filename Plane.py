from tkinter import *
import time


class Plane:
    background_color = "#20232a"
    init_graphs = [] # list of lists of tuples (x_i, y_i)
    bounded_graphs = [] # only points which exists on rectangle (fromx, fromy)x(tox, toy)
    linecolors = [] # list of strings

    fromx, fromy = 0, 0
    tox, toy = 290, 100

    def __init__(self, root):
        self.root = root
        self.root.update()
        self.canvas = Canvas(root, height=root.winfo_width()//2, bg=self.background_color, highlightthickness=0.5)
        self.canvas.pack(fill=X, padx=10, pady=50)
        self.canvas.pack_propagate(0)
        self.canvas.update()

        self.shift_OX_up = 30
        self.shift_OX_right = 30
        self.shift_OY_up = self.shift_OX_up
        self.shift_OY_right = self.shift_OX_right

        self.accuracy = 3 #TODO: deal with it

        self.draw_axes()
        self.canvas.bind('<Configure>', self.update) # Redraw if size of window has changed

    def add_graph(self, points, color):
        self.init_graphs.append(points)
        self.linecolors.append(color)
        self.bounded_graphs.append(self.bound_graph(points))
        self.draw_graph(self.bounded_graphs[-1], self.linecolors[-1], True)

    def change_boundaries(self, fromx, fromy, tox, toy):
        self.fromx = fromx
        self.fromy = fromy
        self.tox = tox
        self.toy = toy

        self.canvas.delete('all')
        self.draw_axes()
        self.bounded_graphs.clear()
        for i in range(len(self.init_graphs)):
            self.bounded_graphs.append(self.bound_graph(self.init_graphs[i]))
            self.draw_graph(self.bounded_graphs[i], self.linecolors[i])

    def update(self, event):
        self.canvas.delete('all')
        self.canvas.config(height=self.root.winfo_width() // 2)
        self.draw_axes()
        for i in range(len(self.bounded_graphs)):
            self.draw_graph(self.bounded_graphs[i], self.linecolors[i])

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
        dx_rounded_to_5 = False
        if dx >= 5:
            dx //= 5
            dx *= 5
            dx_rounded_to_5 = True
        elif dx >= 1:
            dx = int(dx)
        else:
            integer = False

        first_mark_ox = self.fromx
        if self.fromx >= 1 and (4 + first_mark_ox) // 5 < self.tox and integer and dx_rounded_to_5:
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
            px = self.scaleX(x)


        # Mark OY:

        dist_text_from_OY = 15

        integer = True
        n = 10
        dy = (self.toy - self.fromy) / n
        dy_rounded_to_5 = False
        if dy >= 5:
            dy //= 5
            dy *= 5
            dy_rounded_to_5
        elif dy >= 1:
            dy = int(dy)
        else:
            integer = False

        first_mark_oy = self.fromy
        if self.fromy >= 1 and (4 + first_mark_oy) // 5 < self.toy and integer and dy_rounded_to_5:
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
            py = self.scaleY(y)

    def scaleX(self, x):
        return (x - self.fromx) * (self.canvas.winfo_width() - 5 - self.shift_OX_right) / (self.tox - self.fromx)

    def scaleY(self, y):
        return (y - self.fromy) * (self.canvas.winfo_height() - 5 - self.shift_OY_up) / (self.toy - self.fromy)

    def bound_graph(self, plot):
        b_plot = list()
        added = False
        for i in range(len(plot)):
            if self.fromx <= plot[i][0] <= self.tox and self.fromy <= plot[i][1] <= self.toy:
                b_plot.append(plot[i])
                if not added and i != 0:
                    b_plot.append(plot[i - 1]) #add previous point if current added
                added = True
            elif added:
                b_plot.append(plot[i]) #add point if previous one was added
                added = False

        return b_plot

    def draw_graph(self, graph_points, color, animated=False):
        self.canvas.update()
        for i in range(1, len(graph_points)):
            self.canvas.create_line(self.scaleX(graph_points[i - 1][0]) + self.shift_OX_right,
                                    self.convertY(self.scaleY(graph_points[i - 1][1]) + self.shift_OX_up), self.scaleX(graph_points[i][0]) + self.shift_OX_right,
                                    self.convertY(self.scaleY(graph_points[i][1]) + self.shift_OX_up), fill=color, width=2)
            if animated:
                time.sleep(1.5 / len(graph_points))
                self.canvas.update()

    def convertY(self, y):
        return self.canvas.winfo_height() - y
