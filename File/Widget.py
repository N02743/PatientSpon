import tkinter as tk

import Var.Color as Color
import Var.Variable as Var
import Var.Font as Font


class Textfield(tk.Frame):
    def __init__(
        self,
        parent,
        label,
        info,
        row,
        column,
    ):
        super().__init__(parent)
        self.grid(
            row=row,
            column=column,
            sticky="nsew",
            padx=5,
            pady=5,
        )
        # self.pack_propagate(False)

        # TODO: Font size responsive => grid?
        label = tk.Label(
            self,
            text=label,
        )
        label.pack(side="left")

        entry = tk.Entry(self)
        entry.insert(0, info)
        entry.config(state="disabled")
        entry.pack(
            side="right",
        )


class ButtonInput(tk.Button):
    def __init__(
        self,
        parent,
        text,
        bgColor="white",
        command=None,
    ):
        super().__init__(
            parent,
            text=text,
            background=bgColor,
            command=command,
        )
        self.pack(
            side="left",
            padx=Var.padding,
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
            padx=Var.padding,
        )


class ResetButton(ButtonInput):
    def __init__(self, parent, command=None):
        super().__init__(
            parent,
            text="Reset",
            bgColor=Color.resetBG,
            command=command,
        )
        self.pack(
            side="right",
            padx=Var.padding,
        )
