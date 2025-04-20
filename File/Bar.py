import tkinter as tk

import Var.GlobalVariable as Global
import Var.Variable as Var
import Var.Color as Color
import Var.Font as Font

import File.Widget as Widget
import File.Canvas as Canvas


def toggleGrid():
    Global.showGrid = not Global.showGrid
    print("toggle grid =", Global.showGrid)


def toggleLabTest():
    Global.showLabTest = not Global.showLabTest
    print("toggle Lab test =", Global.showLabTest)


def toggleMedUsage():
    Global.showMedUsage = not Global.showMedUsage
    print("toggle Medicine Usage =", Global.showMedUsage)


def addNewLabTest():
    # TODO:
    print("Add New Lab Test")


def addNewMedUsage():
    # TODO:
    print("Add New Medicine Usage")


def configTimeTick():
    # TODO:
    print("Config Time Tick")


def confirmButtonFunction():
    # Canvas.CanvasGraph.redraw()
    print("Confirm Button")


def resetButtonFunction():
    print("Reset Button")


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
        Label.pack(side="top", pady=10)

        SubLabel = tk.Label(
            self,
            text="Yommarat Hospital",
            bg=Color.subLabelBG,
            font=Font.subBanner,
        )
        SubLabel.pack(side="top")


class PatientFrame(tk.Frame):
    def __init__(self, parent, PT):
        super().__init__(parent)
        self.pack()

        InfoTextField = []

        for label in Global.LabelList:
            # print(label, getattr(PT, label))
            InfoTextField.append(
                Widget.TextfieldInput(
                    self,
                    label=label,
                    info=getattr(PT, label),
                ),
            )


class ConfigButtonFrame(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.pack(side="left")

        # TODO: Config Button
        showLabButton = Widget.ButtonInput(
            self,
            text="Show Lab test",
            command=lambda: toggleLabTest(),
        )
        showMedButton = Widget.ButtonInput(
            self,
            text="Show Medication",
            command=lambda: toggleMedUsage(),
        )

        addLabButton = Widget.ButtonInput(
            self,
            text="Add new Lab test",
            command=lambda: addNewLabTest(),
        )
        addMedButton = Widget.ButtonInput(
            self,
            text="Add new Medication",
            command=lambda: addNewMedUsage(),
        )

        timeTickButton = Widget.ButtonInput(
            self,
            text="Time tick",
            command=lambda: configTimeTick(),
        )
        showGridButton = Widget.ButtonInput(
            self,
            text="Show grid",
            command=lambda: toggleGrid(),
        )


class ConfirmFrame(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.pack(side="right")

        # TODO: Confirm and Reset
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


class LabTestFrame(tk.Frame):
    def __init__(
        self,
        parent,
        # date_range,
        patient_data,
    ):
        super().__init__(parent)
        self.pack()

        canvas = Canvas.CanvasGraph(
            self,
            # date_range=date_range,
            patient_data=patient_data,
        )
