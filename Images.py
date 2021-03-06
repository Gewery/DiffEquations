from tkinter import *
from PIL import Image, ImageTk

class Images:
    def __init__(self, root):
        '''CONTROL GRAPHS'''

        graphs_label_width = 85
        graphs_label_height = 35

        label_graphs_image = Image.open("ProjectImages/control_graphs_label.png")
        label_graphs_image = label_graphs_image.resize((graphs_label_width, graphs_label_height),
                                                                 Image.ANTIALIAS)
        self.label_graphs_PhotoImage = ImageTk.PhotoImage(label_graphs_image)

        '''SETTINGS BUTTON'''

        settings_label_width = 85
        settings_label_height = 35

        settings_label_image = Image.open("ProjectImages/settings_label.png")
        settings_label_image = settings_label_image.resize((settings_label_width, settings_label_height),
                                                             Image.ANTIALIAS)
        self.label_settings_PhotoImage = ImageTk.PhotoImage(settings_label_image)

        '''SETTINGS N'''

        settings_N_width = 50
        settings_N_height = 250

        settings_N_image = Image.open("ProjectImages/settings_N.png")
        settings_N_image = settings_N_image.resize((settings_N_width, settings_N_height), Image.ANTIALIAS)

        self.settings_N_PhotoImage = ImageTk.PhotoImage(settings_N_image)
