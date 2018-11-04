from tkinter import *


class RoundEntry:
    background_color = "#232730"

    def __init__(self, canvas, x, y, w, h, textvariable):
        canvas.create_polygon(
            self.round_rectangle(x, y, x + w - 1, y + h - 1),
            smooth=True, fill=self.background_color, outline='white')

        frame = Frame(height=h, width=w, background=self.background_color)

        canvas.create_window(x + 2, y + 2, anchor=NW, window=frame, width=w - 4, height=h - 4)

        entry = Entry(frame, textvariable=textvariable, background=self.background_color, border=0, fg='white',
                      justify='center', insertbackground='white')
        entry.pack()

    def round_rectangle(self, x1, y1, x2, y2, r=10):
        return (
            x1 + r, y1, x1 + r, y1, x2 - r, y1, x2 - r, y1, x2, y1, x2, y1 + r, x2, y1 + r, x2, y2 - r, x2, y2 - r, x2,
            y2,
            x2 - r, y2, x2 - r, y2, x1 + r, y2, x1 + r, y2, x1, y2, x1, y2 - r, x1, y2 - r, x1, y1 + r, x1, y1 + r, x1,
            y1)
