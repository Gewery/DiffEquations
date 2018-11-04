from tkinter import *
from SettingsExtras.RoundEntry import RoundEntry
import time


class FrameSettings:
    frame_width = 100
    background_color = "#232730"
    settings_expanded = False
    frame_graphs = None

    def __init__(self, root, images):
        self.frame = Frame(root, width=self.frame_width, borderwidth=0, highlightthickness=0,
                           background=self.background_color)
        self.frame.pack(side=RIGHT, fill=Y)
        self.frame.pack_propagate(0)

        self.label_settings_image = images.label_settings_PhotoImage
        label_settings = Label(self.frame, image=self.label_settings_image, bg=self.background_color, bd=0,
                               state="normal",
                               activebackground=self.background_color)
        label_settings.pack(pady=10)

        self.frame.update()
        top_frame_initial_settings = Frame(self.frame, height=80, width=self.frame.winfo_width(),
                                           background=self.background_color)
        top_frame_initial_settings.pack(pady=20, padx=5)
        top_frame_initial_settings.pack_propagate(0)

        canvas_initial_settings = Canvas(top_frame_initial_settings, background=self.background_color,
                                         highlightthickness=0)
        canvas_initial_settings.pack()
        frame_initial_settings = Frame(top_frame_initial_settings, background='blue')
        canvas_initial_settings.update()

        canvas_initial_settings.create_polygon(
            self.round_rectangle(0, 0, canvas_initial_settings.winfo_width() - 1,
                                 canvas_initial_settings.winfo_height() - 1),
            smooth=True, fill=self.background_color, outline='white')

        canvas_initial_settings.create_window(canvas_initial_settings.winfo_width() // 2,
                                              canvas_initial_settings.winfo_height() // 2,
                                              window=frame_initial_settings,
                                              width=canvas_initial_settings.winfo_width() - 5,
                                              height=canvas_initial_settings.winfo_height() - 5)

        down_canvas_initial_settings = Canvas(frame_initial_settings, background=self.background_color,
                                              highlightthickness=0)
        down_canvas_initial_settings.pack()

        down_canvas_initial_settings.create_text(20, 9, text='X0', fill='white', font=('Arial', 12))
        self.string_x0 = StringVar()
        self.string_x0.set('1')
        RoundEntry(down_canvas_initial_settings, 5, 20, 30, 20, self.string_x0)
        self.string_x0.trace("w", lambda name, index, mode, s_x0=self.string_x0: self.change_graph_settings(x0=s_x0))

        down_canvas_initial_settings.create_text(65, 9, text='Y0', fill='white', font=('Arial', 12))
        self.string_y0 = StringVar()
        self.string_y0.set('1')
        RoundEntry(down_canvas_initial_settings, 50, 20, 30, 20, self.string_y0)
        self.string_y0.trace("w", lambda name, index, mode, s_y0=self.string_y0: self.change_graph_settings(y0=s_y0))

        down_canvas_initial_settings.create_text(25, 60, text='Max X', fill='white', font=('Arial', 12))
        self.string_tox = StringVar()
        self.string_tox.set('9.5')
        RoundEntry(down_canvas_initial_settings, 50, 50, 30, 20, self.string_tox)
        self.string_tox.trace("w",
                              lambda name, index, mode, s_tox=self.string_tox: self.change_graph_settings(tox=s_tox))

        button_reset = Button(self.frame, text='Reset', font=('impact', 13), command=self.reset_settings,
                              background='blue')
        button_reset.pack()

        label_n = Label(self.frame, text='n')
        label_n.pack()
        string_n = StringVar()
        string_n.set('25')
        entry_n = Entry(self.frame, textvariable=string_n)
        entry_n.pack()
        string_n.trace("w", lambda name, index, mode, s_n=string_n: self.change_graph_settings(n=s_n))

        # GLOBAL ERROR SETTINGS

        top_frame_global_error_settings = Frame(self.frame, height=100, width=self.frame.winfo_width(),
                                                background=self.background_color)
        top_frame_global_error_settings.pack(pady=20, padx=5)
        top_frame_global_error_settings.pack_propagate(0)

        canvas_global_error_settings = Canvas(top_frame_global_error_settings, background=self.background_color,
                                              highlightthickness=0)
        canvas_global_error_settings.pack()
        frame_global_error_settings = Frame(top_frame_global_error_settings, background=self.background_color)
        canvas_global_error_settings.update()

        canvas_global_error_settings.create_polygon(
            self.round_rectangle(0, 0, canvas_global_error_settings.winfo_width() - 1,
                                 canvas_global_error_settings.winfo_height() - 1),
            smooth=True, fill=self.background_color, outline='white')

        canvas_global_error_settings.create_window(canvas_global_error_settings.winfo_width() // 2,
                                                   canvas_global_error_settings.winfo_height() // 2,
                                                   window=frame_global_error_settings,
                                                   width=canvas_global_error_settings.winfo_width() - 5,
                                                   height=canvas_global_error_settings.winfo_height() - 5)

        down_canvas_global_error_settings = Canvas(frame_global_error_settings, background=self.background_color,
                                                   highlightthickness=0)
        down_canvas_global_error_settings.pack()
        down_canvas_global_error_settings.create_text(1, 0, text='Global error', fill='white', anchor=NW,
                                                      font=('Arial', 12))
        down_canvas_global_error_settings.create_text(16, 17, text='division', fill='white', anchor=NW,
                                                      font=('Arial', 12))

        down_canvas_global_error_settings.create_text(0, 45, text='Minimal', fill='white', anchor=NW, font=('Arial, 11'))
        string_min_div = StringVar()
        string_min_div.set('2')
        RoundEntry(down_canvas_global_error_settings, 56, 44, 27, 20, string_min_div)
        string_min_div.trace("w", lambda name, index, mode, s_min_div=string_min_div: self.change_graph_settings(
            min_division=s_min_div))

        down_canvas_global_error_settings.create_text(0, 72, text='Maximal', fill='white', anchor=NW,
                                                      font=('Arial, 11'))
        string_max_div = StringVar()
        string_max_div.set('5')
        RoundEntry(down_canvas_global_error_settings, 56, 71, 27, 20, string_max_div)
        string_max_div.trace("w", lambda name, index, mode, s_max_div=string_max_div: self.change_graph_settings(
            max_division=s_max_div))

    def round_rectangle(self, x1, y1, x2, y2, r=10):
        return (
            x1 + r, y1, x1 + r, y1, x2 - r, y1, x2 - r, y1, x2, y1, x2, y1 + r, x2, y1 + r, x2, y2 - r, x2, y2 - r, x2,
            y2,
            x2 - r, y2, x2 - r, y2, x1 + r, y2, x1 + r, y2, x1, y2, x1, y2 - r, x1, y2 - r, x1, y1 + r, x1, y1 + r, x1,
            y1)

    def reset_settings(self):
        self.change_graph_settings(y0=1)
        self.change_graph_settings(x0=1)
        self.change_graph_settings(tox=9.5)
        self.string_x0.set('1')
        self.string_y0.set('1')
        self.string_tox.set('9.5')

    def change_graph_settings(self, **kwargs):
        arg = ''
        for i in kwargs:
            arg = i
            break
        try:
            if arg != 'n' or float(kwargs[arg].get()) != 0:
                kwargs[arg] = float(kwargs[arg].get())
                self.frame_graphs.change_graphs_settings(kwargs)
        except:
            pass

    def set_frame_graphs(self, frame_graphs):
        self.frame_graphs = frame_graphs
