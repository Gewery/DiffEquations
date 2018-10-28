from tkinter import *
import time


class FrameSettings:
    frame_width = 100
    background_color = "#232730"
    settings_expanded = False

    def __init__(self, root, images):
        self.frame = Frame(root, width=self.frame_width, borderwidth=0, highlightthickness=0, background=self.background_color)
        self.frame.pack(side=RIGHT, fill=Y)
        self.frame.pack_propagate(0)

        self.label_settings_image = images.label_settings_PhotoImage
        button_settings = Label(self.frame, image=self.label_settings_image, bg=self.background_color, bd=0,
                                 state="normal",
                                 activebackground=self.background_color)
        button_settings.pack(pady=10)
