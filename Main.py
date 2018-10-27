from tkinter import *
from FrameControlGraphs import FrameControlGraphs
from FrameSettings import FrameSettings
from FrameGraphs import FrameGraphs
from Images import Images


root = Tk()
root.geometry("1000x600")
root.configure(background="#20232a")
root.title("Karachev_top")

images = Images(root)

frame_control_graphs = FrameControlGraphs(root, images)
frame_graphs = FrameGraphs(root)
frame_settings = FrameSettings(root, images)


# def f(x):
#     return x*x
#
# canvas = Canvas(gui, width=300, height=300)
# canvas.pack()
#
# for i in range(1000):
#     x = -100 + 0.2*i
#     line = canvas.create_line(150 + 10*(x-0.2), 300-f(x-0.2), 150 + 10*x, 300-f(x), fill="blue")

root.mainloop()
