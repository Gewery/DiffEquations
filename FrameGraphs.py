from tkinter import *


class FrameGraphs:

    def __int__(self, root):
        self.frame = Frame(root)
        self.frame.pack(fill=Y)
        self.frame.pack_propagate(0)
        print('created')