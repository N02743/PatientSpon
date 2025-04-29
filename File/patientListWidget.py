import tkinter as tk
from tkinter import messagebox

from File import Widget, Frame

from Var import Font, Var, Global
from Var.Color import Color

from Data import getData as get


def addNewPatient():
    # TODO:
    messagebox.showinfo(
        "Add new Patient",
        "text field for add new Patient",
    )
    print("Config Time Tick")


class NavFrame(Frame.NavFrame):
    def __init__(
        self,
        parent,
        onClosing,
    ):
        super().__init__(parent)

        tk.Button(
            self,
            text="X",
            font=Font.backButtom,
            fg=Color.backButtomFontBG,
            background=Color.backButtomBG,
            width=Var.backButtomWidth,
            command=lambda: onClosing(),
        ).pack(
            side="left",
            fill=tk.Y,
        )

        banner = Frame.BannerFrame(self)
        filter = FiltersFrame(self)


# TODO: Remove duplicate PatientFrame
class FiltersFrame(tk.Frame):
    def __init__(self, parent):
        super().__init__(
            parent,
        )
        self.pack(
            fill=tk.BOTH,
            expand=True,
        )

        info = tk.Frame(
            self,
            bg=Color.patientPageBG,
        )
        Frame.PageInfoFrame(info, text="Patient Info Page")
        info.pack(
            fill=tk.BOTH,
            expand=True,
        )

        # TODO:
        frame = tk.Frame(
            self,
            bg=Color.patientInfoSecondRowBG,
        )
        frame.pack(
            fill=tk.BOTH,
            expand=True,
        )

        info.grid_columnconfigure(0, weight=1)
        frame.grid_columnconfigure(0, weight=1)

        info.grid_rowconfigure(0, weight=1)
        frame.grid_rowconfigure(0, weight=3)


class ContentFrame(tk.Frame):
    def __init__(
        self,
        parent,
        graph_page,
    ):
        super().__init__(parent)
        self.pack(
            fill=tk.BOTH,
            expand=True,
            padx=50,
            pady=30,
        )

        header = HeaderFrame(self)
        patientList = ListFrame(self, graph_page)

        buttom = ButtomFrame(self)

        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=10)
        self.grid_rowconfigure(2, weight=1)

        self.grid_columnconfigure(0, weight=1)


class HeaderFrame(tk.Frame):
    def __init__(
        self,
        parent,
    ):
        super().__init__(
            parent,
            background=Color.patientHeaderFrameBG,
        )
        self.grid(
            row=0,
            column=0,
            sticky="nsew",
            padx=Var.miniPadding,
            pady=Var.miniPadding,
        )

        weight = Var.patientListWeight

        labelList = Global.LabelList[:6]
        del labelList[4]

        for column, label in enumerate(labelList):
            cell = tk.Label(
                self,
                text=label,
                background=Color.patientHeaderBG,
            )
            cell.grid(
                row=0,
                column=column,
                sticky="nsew",
                padx=Var.miniPadding,
                pady=Var.miniPadding,
            )

        for column in range(5):
            self.grid_columnconfigure(
                column,
                weight=weight[column],
                uniform="group1",
            )

        self.grid_rowconfigure(0, weight=1)


class ListFrame(tk.Frame):
    def __init__(
        self,
        parent,
        graph_page=None,
    ):
        super().__init__(
            parent,
            borderwidth=Var.patientListBorderWidth,
            relief=Var.patientListBorderType,
        )
        self.grid(
            row=1,
            column=0,
            sticky="nsew",
            padx=Var.miniPadding,
            pady=Var.miniPadding,
        )

        patientList = get.get_patient_list()

        for row, patient in enumerate(patientList.itertuples()):
            # TODO:
            patientRow = Frame.PatientRowFrame(
                self,
                patient=patient,
                row=row,
            )
            patientRow.bind(
                "<Button-1>",
                lambda event, HN=patient.HN: graph_page(HN),
            )
            patientRow.bind(
                "<Enter>",
                lambda event, ptR=patientRow: ptR.config(bg=Color.patientRowOnHover),
            )
            patientRow.bind(
                "<Leave>",
                lambda event, ptR=patientRow: ptR.config(bg=Color.patientRowFrameBG),
            )

            self.grid_rowconfigure(row, weight=1)

        self.grid_columnconfigure(0, weight=1)


class ButtomFrame(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.grid(
            row=2,
            column=0,
            sticky="nsew",
            padx=Var.miniPadding,
            pady=Var.miniPadding,
        )

        filterAmount = Global.patientFilterAmount
        allAmount = Global.patientAllAmount

        tk.Label(self, text=f"Founded {filterAmount} of {allAmount}").pack(side="left")

        tk.Button(
            self,
            text="Add new Patient",
            command=lambda: addNewPatient(),
        ).pack(side="right")
