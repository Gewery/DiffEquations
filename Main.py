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
frame_settings = FrameSettings(root, images)
frame_graphs = FrameGraphs(root)

frame_control_graphs.set_frame_graphs(frame_graphs)
frame_settings.set_frame_graphs(frame_graphs)

root.mainloop()
