from tkinter import *
from PIL import Image, ImageTk

class Images:
    def __init__(self, root):

        '''CONTROL GRAPHS'''

        graphs_label_width = 85
        graphs_label_height = 35

        label_graphs_image = Image.open("ProjectImages/button_graphs_pressed.png") #TODO Rename file, delete the rest
        label_graphs_image = label_graphs_image.resize((graphs_label_width, graphs_label_height),
                                                                 Image.ANTIALIAS)
        self.label_graphs_PhotoImage = ImageTk.PhotoImage(label_graphs_image)

        '''SETTINGS BUTTON'''

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


        '''SETTINGS BACKGROUND'''

        settings_background_image = Image.open("ProjectImages/ForDanya.png")
        settings_background_image = settings_background_image.resize((300, root.winfo_screenheight()),
                                                             Image.ANTIALIAS)
        self.settings_background_PhotoImage = ImageTk.PhotoImage(settings_background_image)
