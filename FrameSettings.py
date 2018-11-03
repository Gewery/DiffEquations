from tkinter import *
import time


class FrameSettings:
    frame_width = 100
    background_color = "#232730"
    settings_expanded = False
    frame_graphs = None

    def __init__(self, root, images):
        self.frame = Frame(root, width=self.frame_width, borderwidth=0, highlightthickness=0, background=self.background_color)
        self.frame.pack(side=RIGHT, fill=Y)
        self.frame.pack_propagate(0)

        self.label_settings_image = images.label_settings_PhotoImage
        label_settings = Label(self.frame, image=self.label_settings_image, bg=self.background_color, bd=0,
                                 state="normal",
                                 activebackground=self.background_color)
        label_settings.pack(pady=10)

        string_x0 = StringVar()
        entry_x0 = Entry(self.frame, textvariable=string_x0)
        entry_x0.pack()
        string_x0.trace("w", lambda name, index, mode, s_x0=string_x0: self.change_graph_settings(x0=s_x0))

        string_y0 = StringVar()
        entry_y0 = Entry(self.frame, textvariable=string_y0)
        entry_y0.pack()
        string_y0.trace("w", lambda name, index, mode, s_y0=string_y0: self.change_graph_settings(y0=s_y0))

        string_h = StringVar()
        entry_h = Entry(self.frame, textvariable=string_h)
        entry_h.pack()
        string_h.trace("w", lambda name, index, mode, s_h=string_h: self.change_graph_settings(h=s_h))

        string_tox = StringVar()
        entry_tox = Entry(self.frame, textvariable=string_tox)
        entry_tox.pack()
        string_tox.trace("w", lambda name, index, mode, s_tox=string_tox: self.change_graph_settings(tox=s_tox))

    def change_graph_settings(self, **kwargs):
        for arg in kwargs:
            try:
                if arg=='h' and float(kwargs[arg].get()) == 0:
                    continue
                kwargs[arg] = float(kwargs[arg].get())
                self.frame_graphs.change_graphs_settings(kwargs)
                break
            except:
                pass

    def set_frame_graphs(self, frame_graphs):
        self.frame_graphs = frame_graphs
