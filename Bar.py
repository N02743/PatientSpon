import tkinter as tk

import Color
import Variable as Var


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


class TextfieldInput(tk.Frame):
    def __init__(self, parent, label):
        super().__init__(parent)
        self.pack(side="left")

        tk.Label(self, text=label).pack(side="left")
        tk.Entry(self).pack(side="left")


class PatientFrame(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.pack()

        InfoList = ["HN", "AN", "Ward", "Bed", "Sex", "Name", "Age", "Phone Number"]

        InfoTextField = []

        for info in InfoList:
            InfoTextField.append(
                TextfieldInput(
                    self,
                    label=info,
                ),
            )


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
