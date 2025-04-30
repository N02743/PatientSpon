import tkinter as tk

from Var import Font, Global, Var
from Var.Color import Color


class BannerFrame(tk.Frame):
    def __init__(self, parent):
        super().__init__(
            parent,
            bg=Color.bannerFrameBG,
            width=Var.bannerFrame_width,
        )

        self.pack(
            side="left",
            fill="both",
        )
        self.pack_propagate(False)

        Label = tk.Label(
            self,
            text="Spontaneous ADR Form",
            bg=Color.mainLabelBG,
            font=Font.banner,
        )
        Label.pack(
            side="top",
            pady=Var.bannerLabelPadding,
        )

        SubLabel = tk.Label(
            self,
            text="Yommarat Hospital",
            bg=Color.subLabelBG,
            font=Font.subBanner,
        )
        SubLabel.pack(side="top")


class PageInfoFrame(tk.Label):
    def __init__(self, parent, text):
        super().__init__(
            parent,
            text=text,
            padx=5,
            pady=5,
        )
        self.pack(side="left")


class NavFrame(tk.Frame):
    def __init__(
        self,
        parent,
    ):
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


class PatientRowFrame(tk.Frame):
    def __init__(
        self,
        parent,
        patient,
        row,
    ):
        super().__init__(
            parent,
            background=Color.patientRowFrameBG,
            # height=100,
        )

        self.grid(
            row=row,
            column=0,
            sticky="nsew",
            padx=Var.miniPadding,
            pady=Var.miniPadding,
        )

        weight = Var.patientListWeight

        self.grid_rowconfigure(0, weight=1)

        labelList = Global.LabelList[:6]
        del labelList[4]

        for column, label in enumerate(labelList):
            cell = tk.Label(
                self,
                text=getattr(patient, label),
                background=Color.patientRowBG,
                borderwidth=1,
                relief=Var.patientRowBorderType,
            )
            cell.grid(
                row=0,
                column=column,
                sticky="nsew",
                padx=Var.miniPadding,
                pady=Var.miniPadding,
            )
            cell.bind(
                "<Button-1>",
                lambda event: self.event_generate("<Button-1>"),
            )
            cell.bind(
                "<Enter>",
                lambda event: self.event_generate("<Enter>"),
            )
            cell.bind(
                "<Leave>",
                lambda event: self.event_generate("<Leave>"),
            )

        for column in range(5):
            self.grid_columnconfigure(
                column,
                weight=weight[column],
                uniform="group1",
            )
