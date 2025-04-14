import tkinter as tk

import Color
import Variable as Var


class TextfieldInput(tk.Frame):
    def __init__(self, parent, label):
        super().__init__(parent)
        self.pack(side="left")

        tk.Label(self, text=label).pack(side="left")
        tk.Entry(self).pack(side="left")


class ButtonInput(tk.Button):
    def __init__(self, parent, text, bgColor="white"):
        super().__init__(
            parent,
            text=text,
            background=bgColor,
        )
        self.pack(
            side="left",
            padx=Var.graphConfig_padding,
        )


class ConfirmButton(ButtonInput):
    def __init__(self, parent):
        super().__init__(
            parent,
            text="Confirm",
            bgColor="green2",
        )


class ResetButton(ButtonInput):
    def __init__(self, parent):
        super().__init__(
            parent,
            text="Reset",
            bgColor="gold",
        )
