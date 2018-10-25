from tkinter import *
import time


class FrameSettings:
    frame_width_1 = 60
    frame_width_2 = 300
    background_color = "#232730"
    settings_expanded = False

    def __init__(self, root, images):
        self.frame = Frame(root, background=self.background_color, width=self.frame_width_1)
        self.frame.pack(side=RIGHT, fill=Y)
        self.frame.pack_propagate(0)

        self.button_settings_image = images.button_settings_PhotoImage
        self.button_settings_hover_image = images.button_settings_hover_PhotoImage
        self.button_settings_pressed_image = images.button_settings_pressed_PhotoImage

        button_settings = Button(self.frame, image=self.button_settings_image, bg=self.background_color, bd=0,
                                 state="normal",
                                 activebackground=self.background_color)
        button_settings.pack(pady=10, padx=7)
        button_settings.bind('<Enter>', lambda event, img=self.button_settings_hover_image: self.change_img(event, img))
        button_settings.bind('<Leave>', lambda event, img=self.button_settings_image: self.change_img(event, img))
        button_settings.bind('<Button-1>', self.expand_settings)

    def expand_settings(self, event):
        beg = self.frame_width_1
        end = self.frame_width_2

        if self.settings_expanded:
            beg, end = end, beg
            event.widget.config(image=self.button_settings_image)
            self.settings_expanded = False
        else:
            event.widget.config(image=self.button_settings_pressed_image)
            self.settings_expanded = True

        N = 10  # steps
        for i in range(N):
            current = beg + (end - beg) * i / N
            self.frame.config(width=current)
            time.sleep(0.1 / N)
            self.frame.update()

    def change_img(self, event, img):
        if not self.settings_expanded:
            event.widget.config(image=img)
