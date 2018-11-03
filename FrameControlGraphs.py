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
        self.label_graphs.place(relx=0, rely=0, x=9, y=10)

        # EXACT

        self.exact_solution_switcher = Canvas(self.frame, background=self.background_color, highlightthickness=0,
                                              width=81,
                                              height=46)
        self.exact_solution_switcher.place(relx=0, rely=0.2, x=9)
        self.exact_solution_switcher.create_polygon(self.round_rectangle(0, 0, 80, 45), smooth=True, outline='white',
                                                    fill=self.background_color)
        self.exact_solution_fill = self.exact_solution_switcher.create_polygon(self.round_rectangle(3, 3, 3, 42),
                                                                               fill=self.background_color, smooth=True)
        self.exact_solution_switcher.update()
        self.exact_solution_text = self.exact_solution_switcher.create_text(
            self.exact_solution_switcher.winfo_width() // 2, self.exact_solution_switcher.winfo_height() // 2,
            text='Exact', font=('comic sans ms', 14, 'bold'), fill='white')
        self.exact_solution_turned = False
        self.exact_solution_switcher.bind('<Button-1>', self.draw_exact_solution_graph)

        # EULER

        self.euler_switcher = Canvas(self.frame, background=self.background_color, highlightthickness=0,
                                              width=81,
                                              height=46)
        self.euler_switcher.place(relx=0, rely=0.2, x=9, y=80)
        self.euler_switcher.create_polygon(self.round_rectangle(0, 0, 80, 45), smooth=True, outline='white',
                                                    fill=self.background_color)
        self.euler_fill = self.euler_switcher.create_polygon(self.round_rectangle(3, 3, 3, 42),
                                                                               fill=self.background_color, smooth=True)
        self.euler_switcher.update()
        self.euler_text = self.euler_switcher.create_text(
            self.euler_switcher.winfo_width() // 2, self.euler_switcher.winfo_height() // 2,
            text='Euler', font=('comic sans ms', 14, 'bold'), fill='white')
        self.euler_turned = False
        self.euler_switcher.bind('<Button-1>', self.draw_euler_graphs)

        #IMPROVED EULER

        self.improved_euler_switcher = Canvas(self.frame, background=self.background_color, highlightthickness=0,
                                     width=81,
                                     height=46)
        self.improved_euler_switcher.place(relx=0, rely=0.2, x=9, y=160)
        self.improved_euler_switcher.create_polygon(self.round_rectangle(0, 0, 80, 45), smooth=True, outline='white',
                                           fill=self.background_color)
        self.improved_euler_fill = self.improved_euler_switcher.create_polygon(self.round_rectangle(3, 3, 3, 42),
                                                             fill=self.background_color, smooth=True)
        self.improved_euler_switcher.update()
        self.improved_euler_text = self.improved_euler_switcher.create_text(
            self.improved_euler_switcher.winfo_width() // 2, self.improved_euler_switcher.winfo_height() // 2,
            text='Impr. Euler', font=('comic sans ms', 10, 'bold'), fill='white')
        self.improved_euler_turned = False
        self.improved_euler_switcher.bind('<Button-1>', self.draw_improved_euler_graphs)

        # RUNGE KUTTA

        self.runge_kutta_switcher = Canvas(self.frame, background=self.background_color, highlightthickness=0,
                                              width=81,
                                              height=46)
        self.runge_kutta_switcher.place(relx=0, rely=0.2, x=9, y=240)
        self.runge_kutta_switcher.create_polygon(self.round_rectangle(0, 0, 80, 45), smooth=True, outline='white',
                                                    fill=self.background_color)
        self.runge_kutta_fill = self.runge_kutta_switcher.create_polygon(self.round_rectangle(3, 3, 3, 42),
                                                                               fill=self.background_color, smooth=True)
        self.runge_kutta_switcher.update()
        self.runge_kutta_text = self.runge_kutta_switcher.create_text(
            self.runge_kutta_switcher.winfo_width() // 2, self.runge_kutta_switcher.winfo_height() // 2,
            text='Runge Kutta', font=('comic sans ms', 10, 'bold'), fill='white')
        self.runge_kutta_turned = False
        self.runge_kutta_switcher.bind('<Button-1>', self.draw_runge_kutta_graphs)


    def set_frame_graphs(self, frame_graphs):
        self.frame_graphs = frame_graphs

    def draw_exact_solution_graph(self, event):
        if not self.exact_solution_turned:
            self.exact_solution_turned = True
            self.exact_solution_switcher.itemconfig(self.exact_solution_fill, fill='white')
            self.exact_solution_switcher.itemconfig(self.exact_solution_text, fill='black')
            for i in range(0, 82, 2):
                self.exact_solution_switcher.coords(self.exact_solution_fill, self.round_rectangle(0, 0, i, 45))
                self.exact_solution_switcher.update()
                time.sleep(0.2 / 80 / 2)
            self.frame_graphs.draw_exact_solution_graph()
        else:
            self.exact_solution_turned = False
            for i in range(82, 3, -2):
                self.exact_solution_switcher.coords(self.exact_solution_fill, self.round_rectangle(0, 0, i, 45))
                self.exact_solution_switcher.update()
                time.sleep(0.2 / 80 / 2)
            self.exact_solution_switcher.coords(self.exact_solution_fill, self.round_rectangle(3, 3, 3, 42))
            self.exact_solution_switcher.itemconfig(self.exact_solution_fill, fill=self.background_color)
            self.exact_solution_switcher.itemconfig(self.exact_solution_text, fill='white')
            self.frame_graphs.remove_exact_solution_graph()

    def draw_euler_graphs(self, event):
        if not self.euler_turned:
            self.euler_turned = True
            self.euler_switcher.itemconfig(self.euler_fill, fill='blue')
            self.euler_switcher.itemconfig(self.euler_text, fill='black')
            for i in range(3, 81, 2):
                self.euler_switcher.coords(self.euler_fill, self.round_rectangle(1, 1, i, 44))
                self.euler_switcher.update()
                time.sleep(0.2 / 80 / 2)
            self.frame_graphs.draw_euler_graphs()
        else:
            self.euler_turned = False
            for i in range(82, 3, -2):
                self.euler_switcher.coords(self.euler_fill, self.round_rectangle(0, 0, i, 45))
                self.euler_switcher.update()
                time.sleep(0.2 / 80 / 2)
            self.euler_switcher.coords(self.euler_fill, self.round_rectangle(3, 3, 3, 42))
            self.euler_switcher.itemconfig(self.euler_fill, fill=self.background_color)
            self.euler_switcher.itemconfig(self.euler_text, fill='white')
            self.frame_graphs.remove_euler_graphs()

    def draw_improved_euler_graphs(self, event):
        if not self.improved_euler_turned:
            self.improved_euler_turned = True
            self.improved_euler_switcher.itemconfig(self.improved_euler_fill, fill='yellow')
            self.improved_euler_switcher.itemconfig(self.improved_euler_text, fill='black')
            for i in range(3, 82, 2):
                self.improved_euler_switcher.coords(self.improved_euler_fill, self.round_rectangle(1, 1, i, 45))
                self.improved_euler_switcher.update()
                time.sleep(0.2 / 80 / 2)
            self.frame_graphs.draw_improved_euler_graphs()
        else:
            self.improved_euler_turned = False
            for i in range(82, 3, -2):
                self.improved_euler_switcher.coords(self.improved_euler_fill, self.round_rectangle(0, 0, i, 45))
                self.improved_euler_switcher.update()
                time.sleep(0.2 / 80 / 2)
            self.improved_euler_switcher.coords(self.improved_euler_fill, self.round_rectangle(3, 3, 3, 42))
            self.improved_euler_switcher.itemconfig(self.improved_euler_fill, fill=self.background_color)
            self.improved_euler_switcher.itemconfig(self.improved_euler_text, fill='white')
            self.frame_graphs.remove_improved_euler_graphs()

    def draw_runge_kutta_graphs(self, event):
        if not self.runge_kutta_turned:
            self.runge_kutta_turned = True
            self.runge_kutta_switcher.itemconfig(self.runge_kutta_fill, fill='red')
            self.runge_kutta_switcher.itemconfig(self.runge_kutta_text, fill='black')
            for i in range(3, 81, 2):
                self.runge_kutta_switcher.coords(self.runge_kutta_fill, self.round_rectangle(1, 1, i, 45))
                self.runge_kutta_switcher.update()
                time.sleep(0.2 / 80 / 2)
            self.frame_graphs.draw_runge_kutta_graphs()
        else:
            self.runge_kutta_turned = False
            for i in range(82, 3, -2):
                self.runge_kutta_switcher.coords(self.runge_kutta_fill, self.round_rectangle(0, 0, i, 45))
                self.runge_kutta_switcher.update()
                time.sleep(0.2 / 80 / 2)
            self.runge_kutta_switcher.coords(self.runge_kutta_fill, self.round_rectangle(3, 3, 3, 42))
            self.runge_kutta_switcher.itemconfig(self.runge_kutta_fill, fill=self.background_color)
            self.runge_kutta_switcher.itemconfig(self.runge_kutta_text, fill='white')
            self.frame_graphs.remove_runge_kutta_graphs()

    def round_rectangle(self, x1, y1, x2, y2, r=10):
        return (
            x1 + r, y1, x1 + r, y1, x2 - r, y1, x2 - r, y1, x2, y1, x2, y1 + r, x2, y1 + r, x2, y2 - r, x2, y2 - r, x2,
            y2,
            x2 - r, y2, x2 - r, y2, x1 + r, y2, x1 + r, y2, x1, y2, x1, y2 - r, x1, y2 - r, x1, y1 + r, x1, y1 + r, x1,
            y1)
