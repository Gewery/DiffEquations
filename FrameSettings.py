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

        label_x0 = Label(self.frame, text='x0')
        label_x0.pack()
        string_x0 = StringVar()
        entry_x0 = Entry(self.frame, textvariable=string_x0)
        entry_x0.pack()
        string_x0.trace("w", lambda name, index, mode, s_x0=string_x0: self.change_graph_settings(x0=s_x0))

        label_y0 = Label(self.frame, text='y0')
        label_y0.pack()
        string_y0 = StringVar()
        entry_y0 = Entry(self.frame, textvariable=string_y0)
        entry_y0.pack()
        string_y0.trace("w", lambda name, index, mode, s_y0=string_y0: self.change_graph_settings(y0=s_y0))

        label_h = Label(self.frame, text='h')
        label_h.pack()
        string_h = StringVar()
        entry_h = Entry(self.frame, textvariable=string_h)
        entry_h.pack()
        string_h.trace("w", lambda name, index, mode, s_h=string_h: self.change_graph_settings(h=s_h))

        label_tox = Label(self.frame, text='tox')
        label_tox.pack()
        string_tox = StringVar()
        entry_tox = Entry(self.frame, textvariable=string_tox)
        entry_tox.pack()
        string_tox.trace("w", lambda name, index, mode, s_tox=string_tox: self.change_graph_settings(tox=s_tox))

        label_min_div = Label(self.frame, text='min_div')
        label_min_div.pack()
        string_min_div = StringVar()
        entry_min_div = Entry(self.frame, textvariable=string_min_div)
        entry_min_div.pack()
        string_min_div.trace("w", lambda name, index, mode, s_min_div=string_min_div: self.change_graph_settings(min_division=s_min_div))

        label_max_div = Label(self.frame, text='max_div')
        label_max_div.pack()
        string_max_div = StringVar()
        entry_max_div = Entry(self.frame, textvariable=string_max_div)
        entry_max_div.pack()
        string_max_div.trace("w", lambda name, index, mode, s_max_div=string_max_div: self.change_graph_settings(
            max_division=s_max_div))

    def change_graph_settings(self, **kwargs):
        arg = ''
        for i in kwargs:
            arg = i
            break
        try:
            if arg != 'h' or float(kwargs[arg].get()) != 0:
                kwargs[arg] = float(kwargs[arg].get())
                self.frame_graphs.change_graphs_settings(kwargs)
        except:
            pass

    def set_frame_graphs(self, frame_graphs):
        self.frame_graphs = frame_graphs
