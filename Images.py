from tkinter import *
from PIL import Image, ImageTk

class Images:
    def __init__(self):

        '''CONTROL GRAPHS'''

        graphs_button_width_1 = 45
        graphs_button_height_1 = 35
        graphs_button_width_2 = 85
        graphs_button_height_2 = 35

        button_graphs_image = Image.open("ProjectImages/button_graphs.png")
        button_graphs_image = button_graphs_image.resize((graphs_button_width_1, graphs_button_height_1),
                                                                 Image.ANTIALIAS)
        self.button_graphs_PhotoImage = ImageTk.PhotoImage(button_graphs_image)

        button_graphs_hover_image = Image.open("ProjectImages/button_graphs_hover.png")
        button_graphs_hover_image = button_graphs_hover_image.resize(
            (graphs_button_width_1, graphs_button_height_1),
            Image.ANTIALIAS)
        self.button_graphs_hover_PhotoImage = ImageTk.PhotoImage(button_graphs_hover_image)

        button_graphs_pressed_image = Image.open("ProjectImages/button_graphs_pressed.png")
        button_graphs_pressed_image = button_graphs_pressed_image.resize(
            (graphs_button_width_2, graphs_button_height_2),
            Image.ANTIALIAS)
        self.button_graphs_pressed_PhotoImage = ImageTk.PhotoImage(button_graphs_pressed_image)


        '''SETTINGS'''

        settings_button_width_1 = 45
        settings_button_height_1 = 35
        settings_button_width_2 = 85
        settings_button_height_2 = 35

        button_settings_image = Image.open("ProjectImages/button_settings.png")
        button_settings_image = button_settings_image.resize((settings_button_width_1, settings_button_height_1),
                                                             Image.ANTIALIAS)
        self.button_settings_PhotoImage = ImageTk.PhotoImage(button_settings_image)

        button_settings_hover_image = Image.open("ProjectImages/button_settings_hover.png")
        button_settings_hover_image = button_settings_hover_image.resize(
            (settings_button_width_1, settings_button_height_1),
            Image.ANTIALIAS)
        self.button_settings_hover_PhotoImage = ImageTk.PhotoImage(button_settings_hover_image)

        button_settings_pressed_image = Image.open("ProjectImages/button_settings_pressed.png")
        button_settings_pressed_image = button_settings_pressed_image.resize(
            (settings_button_width_2, settings_button_height_2),
            Image.ANTIALIAS)
        self.button_settings_pressed_PhotoImage = ImageTk.PhotoImage(button_settings_pressed_image)
