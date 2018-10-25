from tkinter import *
import time


class FrameControlGraphs:
    frame_width_1 = 60
    frame_width_2 = 200
    background_color = "#232730"
    graphs_expanded = False

    def __init__(self, root, images):
        self.frame = Frame(root, background=self.background_color, width=self.frame_width_1)
        self.frame.pack(side=LEFT, fill=Y)
        self.frame.pack_propagate(0)

        self.button_graphs_image = images.button_graphs_PhotoImage
        self.button_graphs_hover_image = images.button_graphs_hover_PhotoImage
        self.button_graphs_pressed_image = images.button_graphs_pressed_PhotoImage

        self.button_graphs = Button(self.frame, image=self.button_graphs_image, bg=self.background_color, bd=0,
                               state="normal",
                               activebackground=self.background_color)
        self.button_graphs.pack(pady=10, padx=7)

        self.button_graphs.bind('<Enter>', lambda event, img=self.button_graphs_hover_image: self.change_img(event, img))
        self.button_graphs.bind('<Leave>', lambda event, img=self.button_graphs_image: self.change_img(event, img))
        self.button_graphs.bind('<Button-1>', self.expand_frame)

    def expand_frame(self, event):
        beg = self.frame_width_1
        end = self.frame_width_2
        if self.graphs_expanded:
            beg, end = end, beg
            event.widget.config(image=self.button_graphs_image)
            self.graphs_expanded = False
        else:
            event.widget.config(image=self.button_graphs_pressed_image)
            self.graphs_expanded = True

        N = 10  # steps
        for i in range(N):
            current = beg + (end - beg) * i / N
            self.frame.config(width=current)
            time.sleep(0.1 / N)
            self.frame.update()

    def change_img(self, event, img):
        if not self.graphs_expanded:
            event.widget.config(image=img)
