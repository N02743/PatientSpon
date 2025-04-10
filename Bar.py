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
