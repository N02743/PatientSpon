import tkinter as tk

import Var.Color as Color
import Var.Variable as Var


class TextfieldInput(tk.Frame):
    def __init__(self, parent, label, info):
        super().__init__(parent)
        self.pack(side="left")

        tk.Label(self, text=label).pack(side="left")
        entry = tk.Entry(self)
        entry.insert(0, info)
        entry.config(state="disabled")
        entry.pack(side="left")


class ButtonInput(tk.Button):
    def __init__(self, parent, text, bgColor="white", command=None):
        super().__init__(
            parent,
            text=text,
            background=bgColor,
            command=command,
        )
        self.pack(
            side="left",
            padx=Var.button_padding,
        )


class ConfirmButton(ButtonInput):
    def __init__(self, parent, command=None):
        super().__init__(
            parent,
            text="Confirm",
            bgColor=Color.confirmBG,
            command=command,
        )
        self.pack(
            side="right",
            padx=Var.button_padding,
        )


class ResetButton(ButtonInput):
    def __init__(self, parent):
        super().__init__(
            parent,
            text="Reset",
            bgColor=Color.resetBG,
        )
        self.pack(
            side="right",
            padx=Var.button_padding,
        )
