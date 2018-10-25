from tkinter import *
import time


class Graph:

    background_color = "#20232a"

    # def change_color(self, event, id, root):
    #     print(event)
    #     event.widget.itemconfig(id, fill="red")
    #     event.widget.config(height=int(root.winfo_width()//2))
    #     print(root.winfo_width())

    def __init__(self, root, dataList, linecolors):
        root.update()
        canvas = Canvas(root, height=int(root.winfo_width()//2), bg=self.background_color)
        canvas.pack(fill=X, padx=10, pady=70) #TODO change padding to add more graphs

        self.dataList = dataList
        self.linecolors = linecolors

        rect = canvas.create_rectangle(0, 0, 100, 100, fill='yellow')
        #canvas.tag_bind(rect, '<Enter>', lambda event, id=rect, rt=root: self.change_color(event, id, rt))
        #canvas.create_window(10, 10, window=root)

    def draw_piece(self, canvas, fromx, fromy, tox, toy):
        cw = canvas.winfo_width()
        ch = canvas.winfo_height()
