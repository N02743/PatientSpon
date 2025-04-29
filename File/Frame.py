import tkinter as tk
from tkinter import messagebox

from Var import Font, Global, Var
from Var.Color import Color

from File import Widget, Canvas
from File import GlobalFunction as GLBFunc

from Data import getData as get


def toggleGrid():
    showGridButton.onClick()

    print("toggle grid")


def toggleLabTest():
    showLabButton.onClick()

    print("toggle Lab test")


def toggleMedUsage():
    showMedButton.onClick()

    print("toggle Medicine Usage")


def addNewLabTest():
    # TODO:
    messagebox.showinfo(
        "Add new Lab Test",
        "text field for add new Lab Test",
    )
    print("Add New Lab Test")


def addNewMedUsage():
    # TODO:
    messagebox.showinfo(
        "Add new Medicine Usage",
        "text field for add new Medicine Usage",
    )
    print("Add New Medicine Usage")


def configTimeTick():
    # TODO:
    messagebox.showinfo(
        "Add new Time Tick",
        "text field for add new Time Tick",
    )
    print("Config Time Tick")


def confirmButtonFunction():
    Global.showGrid = showGridButton.onConfirm()
    Global.showLabTest = showLabButton.onConfirm()
    Global.showMedUsage = showMedButton.onConfirm()

    GLBFunc.CanvasRedraw()

    print("Confirm Button")


def resetButtonFunction():
    showGridButton.onReset()
    showLabButton.onReset()
    showMedButton.onReset()

    print("Reset Button")


def addNewPatient():
    # TODO:
    messagebox.showinfo(
        "Add new Patient",
        "text field for add new Patient",
    )
    print("Config Time Tick")


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


class PatientFrame(tk.Frame):
    def __init__(self, parent, PT):
        super().__init__(
            parent,
            bg="green",
        )
        self.pack(
            fill=tk.BOTH,
            expand=True,
        )

        weightList = [15, 15, 1, 1, 1, 15, 1, 4]

        pageInfo = tk.Frame(
            self,
            bg="purple",
        )

        frame = []
        frame.append(
            tk.Frame(
                self,
                bg=Color.patientInfoFirstRowBG,
            )
        )
        frame.append(
            tk.Frame(
                self,
                bg=Color.patientInfoSecondRowBG,
            )
        )

        pageInfo.pack(
            fill=tk.BOTH,
            expand=True,
        )

        frame[0].pack(
            fill=tk.BOTH,
            expand=True,
        )
        frame[1].pack(
            fill=tk.BOTH,
            expand=True,
        )

        PageInfoFrame(pageInfo, text="Medication page")

        for i, label in enumerate(Global.LabelList):
            row = 0 if i < 4 else 1
            column = i if i < 4 else i - 4

            Widget.Textfield(
                frame[row],
                label=label,
                info=getattr(PT, label),
                row=0,
                column=column,
            ),

        for i in range(8):
            row = 0 if i < 4 else 1
            column = i if i < 4 else i - 4

            frame[row].grid_columnconfigure(
                column,
                weight=weightList[i],
            )

        pageInfo.grid_columnconfigure(0, weight=1)
        pageInfo.grid_rowconfigure(0, weight=1)

        frame[0].grid_rowconfigure(0, weight=1)
        frame[1].grid_rowconfigure(0, weight=1)


class ConfigButtonFrame(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.pack(side="left")

        # TODO: Add choose date to show

        global showLabButton
        showLabButton = Widget.ToggleButton(
            self,
            text="Show Lab test",
            var=Global.showLabTest,
        )

        global showMedButton
        showMedButton = Widget.ToggleButton(
            self,
            text="Show Medication",
            var=Global.showMedUsage,
        )

        addLabButton = Widget.AddButton(
            self,
            text="Add new Lab test",
            command=lambda: addNewLabTest(),
        )
        addMedButton = Widget.AddButton(
            self,
            text="Add new Medication",
            command=lambda: addNewMedUsage(),
        )

        timeTickButton = Widget.AddButton(
            self,
            text="Time tick",
            command=lambda: configTimeTick(),
        )

        global showGridButton
        showGridButton = Widget.ToggleButton(
            self,
            text="Show grid",
            var=Global.showGrid,
        )


class ConfirmFrame(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.pack(side="right")

        resetButton = Widget.ResetButton(
            self,
            command=lambda: resetButtonFunction(),
        )
        confirmButton = Widget.ConfirmButton(
            self,
            command=lambda: confirmButtonFunction(),
        )


class GraphConfigFrame(tk.Frame):
    def __init__(self, parent):
        super().__init__(
            parent,
            padx=Var.padding,
            pady=Var.padding,
        )
        self.pack(side="top", fill="x")

        buttonFrame = ConfigButtonFrame(self)
        confirmFrame = ConfirmFrame(self)


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


class GraphNavFrame(NavFrame):
    def __init__(
        self,
        parent,
        PatientData,
        patient_page,
    ):
        super().__init__(parent)

        tk.Button(
            self,
            text="↶",
            font=Font.backButtom,
            fg=Color.backButtomFontBG,
            background=Color.backButtomBG,
            width=Var.backButtomWidth,
            command=lambda: patient_page(),
        ).pack(
            side="left",
            fill=tk.Y,
        )

        banner = BannerFrame(self)
        patient = PatientFrame(self, PT=PatientData)


# TODO: Remove duplicate PatientFrame
class PatientFiltersFrame(tk.Frame):
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
            bg=Color.patientInfoFirstRowBG,
        )
        PageInfoFrame(info, text="Patient Info Page")
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


class PatientContentFrame(tk.Frame):
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

        header = PatientHeaderFrame(self)
        patientList = PatientListFrame(self, graph_page)

        buttom = PatientButtomFrame(self)

        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=10)
        self.grid_rowconfigure(2, weight=1)

        self.grid_columnconfigure(0, weight=1)


class PatientButtomFrame(tk.Frame):
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


class PatientListNavFrame(NavFrame):
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

        banner = BannerFrame(self)
        filter = PatientFiltersFrame(self)


class ContentFrame(tk.Frame):
    def __init__(
        self,
        parent,
        patient_data,
    ):
        super().__init__(
            parent,
            bg=Color.contentFrameBG,
        )
        self.pack(
            side="top",
            expand=True,
            fill="both",
        )

        configFrame = GraphConfigFrame(self)

        canvasFrame = CanvasFrame(
            self,
            patient_data=patient_data,
        )


class CanvasFrame(tk.Frame):
    def __init__(
        self,
        parent,
        patient_data,
    ):
        super().__init__(parent)
        self.pack()

        canvas = Canvas.CanvasGraph(
            self,
            patient_data=patient_data,
        )

        GLBFunc.CanvasRedrawSetting(canvas.redraw)


class PatientHeaderFrame(tk.Frame):
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


class PatientListFrame(tk.Frame):
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
            patientRow = PatientRowFrame(
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
