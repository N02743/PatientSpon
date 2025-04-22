import tkinter as tk

import Var.Color as Color
import Var.Variable as Var
import Var.Font as Font
import Var.GlobalVariable as Global


def buttonColor(variable, isClick):
    if variable:
        if isClick:
            return Color.buttonWaitFalseBG
        else:
            return Color.buttonTrueBG
    else:
        if isClick:
            return Color.buttonWaitTrueBG
        else:
            return Color.buttonFalseBG


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
        var=None,
    ):
        if var is None:
            bgColor = "white"
        else:
            bgColor = buttonColor(var, False)

        super().__init__(
            parent,
            text=text,
            background=bgColor,
            command=self.onClick,
        )
        self.pack(
            side="left",
            padx=Var.padding,
        )

        self.variable = var
        self.isClick = False

    def configColor(self):
        self.config(
            bg=buttonColor(
                self.variable,
                self.isClick,
            ),
        )

    def onClick(self):
        self.isClick = not self.isClick
        self.configColor()

    def onConfirm(self):
        if self.isClick:
            self.variable = not self.variable

        self.isClick = False

        self.configColor()
        return self.variable

    def onReset(self):
        self.isClick = False
        self.configColor()


class ConfirmButton(tk.Button):
    def __init__(
        self,
        parent,
        command,
    ):
        super().__init__(
            parent,
            text="Confirm",
            background=Color.confirmBG,
            command=command,
        )

        self.pack(
            side="right",
            padx=Var.padding,
        )


class ResetButton(tk.Button):
    def __init__(
        self,
        parent,
        command,
    ):
        super().__init__(
            parent,
            text="Reset",
            background=Color.resetBG,
            command=command,
        )

        self.pack(
            side="right",
            padx=Var.padding,
        )
