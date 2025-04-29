import tkinter as tk
from tkinter import messagebox

from Var import Font, Var, Global
from Var.Color import Color

from File import Widget, Canvas, Frame


from File import GlobalFunction as GLBFunc


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


def toggleGrid():
    showGridButton.onClick()

    print("toggle grid")


def toggleLabTest():
    showLabButton.onClick()

    print("toggle Lab test")


def toggleMedUsage():
    showMedButton.onClick()

    print("toggle Medicine Usage")


class GraphNavFrame(Frame.NavFrame):
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

        banner = Widget.BannerFrame(self)
        patient = PatientFrame(self, PT=PatientData)


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
            bg=Color.patientPageBG,
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

        Widget.PageInfoFrame(pageInfo, text="Medication page")

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


class GraphConfigFrame(tk.Frame):
    def __init__(self, parent):
        super().__init__(
            parent,
            padx=Var.padding,
            pady=Var.padding,
            bg=Color.configFrameBG,
        )
        self.pack(side="top", fill="x")

        buttonFrame = ConfigButtonFrame(self)
        confirmFrame = ConfirmFrame(self)


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


class ConfigButtonFrame(tk.Frame):
    def __init__(self, parent):
        super().__init__(
            parent,
            background=Color.configFrameBG,
        )
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
        super().__init__(
            parent,
            background=Color.configFrameBG,
        )
        self.pack(side="right")

        resetButton = Widget.ResetButton(
            self,
            command=lambda: resetButtonFunction(),
        )
        confirmButton = Widget.ConfirmButton(
            self,
            command=lambda: confirmButtonFunction(),
        )
