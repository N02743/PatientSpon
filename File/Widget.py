import tkinter as tk

from Var import Var, Global
from Var.Color import Color


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

        self.label = label

        # TODO: Font size responsive => grid?
        label = tk.Label(
            self,
            text=label,
        )
        label.pack(side="left")

        self.entryVar = tk.StringVar()

        self.entry = tk.Entry(self, textvariable=self.entryVar)
        if info is not None:
            self.entry.insert(0, info)
        self.entry.config(state="readonly")
        self.entry.pack(
            side="right",
        )

    def onEnabled(self):
        self.entry.config(state="normal")
        Global.filterVarDict[self.label] = self.entryVar


class ToggleButton(tk.Button):
    def __init__(
        self,
        parent,
        text,
        var,
    ):

        bgColor = buttonColor(var, False)

        super().__init__(
            parent,
            text=text,
            background=bgColor,
            command=self.onClick,
        )
        self.pack(
            side="left",
            padx=20,
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


class ConfigButton(tk.Button):
    def __init__(
        self,
        parent,
        text,
        command,
    ):

        super().__init__(
            parent,
            text=text,
            command=command,
        )
        self.pack(
            side="left",
            padx=Var.padding,
        )
        # TODO:

        # self.isClick = False

    # def configColor(self):
    #     self.config(
    #         bg=buttonColor(
    #             self.variable,
    #             self.isClick,
    #         ),
    #     )

    # def onClick(self):
    #     self.isClick = not self.isClick
    #     self.configColor()

    # def onConfirm(self):
    #     if self.isClick:
    #         self.variable = not self.variable

    #     self.isClick = False

    #     self.configColor()
    #     return self.variable

    # def onReset(self):
    #     self.isClick = False
    #     self.configColor()


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
