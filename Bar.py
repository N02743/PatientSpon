import tkinter as tk

import Color
import Variable as Var
import Widget


class BannerFrame(tk.Frame):
    def __init__(self, parent):
        super().__init__(
            parent,
            bg=Color.bannerFrameBG,
            width=Var.bannerFrame_height,
        )

        self.pack(
            side="left",
            fill="both",
        )
        self.pack_propagate(False)

        Label = tk.Label(
            self,
            text="Spontaneous ADR Form",
            bg="green",
        )
        Label.pack()

        SubLabel = tk.Label(
            self,
            text="Yommarat Hospital",
            bg="gray",
        )
        SubLabel.pack()


class PatientFrame(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.pack()

        InfoList = ["HN", "AN", "Ward", "Bed", "Sex", "Name", "Age", "Phone Number"]

        InfoTextField = []

        for info in InfoList:
            InfoTextField.append(
                Widget.TextfieldInput(
                    self,
                    label=info,
                ),
            )


class ConfigButtonFrame(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.pack(side="left")

        showLabButton = Widget.ButtonInput(self, text="Show Lab test")
        showMedButton = Widget.ButtonInput(self, text="Show Medication")
        addLabButton = Widget.ButtonInput(self, text="Add new Lab test")
        addMedButton = Widget.ButtonInput(self, text="Add new Medication")
        timeTickButton = Widget.ButtonInput(self, text="Time tick")


class ConfirmFrame(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.pack(side="right")

        confirmButton = Widget.ConfirmButton(self)
        resetButton = Widget.ResetButton(self)


class GraphConfigFrame(tk.Frame):
    def __init__(self, parent):
        super().__init__(
            parent,
            padx=Var.graphConfig_padding,
            pady=Var.graphConfig_padding,
        )
        self.pack(side="top", fill="x")

        buttonFrame = ConfigButtonFrame(self)
        confirmFrame = ConfirmFrame(self)


class NavFrame(tk.Frame):
    def __init__(self, parent):
        super().__init__(
            parent,
            bg=Color.navFrameBG,
            height=Var.navFrame_height,
        )
        self.pack(
            side="top",
            fill="x",
        )
        self.pack_propagate(False)


class ContentFrame(tk.Frame):
    def __init__(self, parent):
        super().__init__(
            parent,
            bg=Color.contentFrameBG,
        )
        self.pack(
            side="top",
            expand=True,
            fill="both",
        )
