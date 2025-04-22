import tkinter as tk

import Var.GlobalVariable as Global
import Var.Variable as Var
import Var.Color as Color
import Var.Font as Font

import File.Widget as Widget
import File.Canvas as Canvas

import Data.getData as get


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
        super().__init__(
            parent,
            bg="green",
        )
        self.pack(
            fill=tk.BOTH,
            expand=True,
        )

        rowList = [0, 0, 0, 0, 1, 1, 1, 1]
        columnList = [0, 1, 2, 3, 0, 1, 2, 3]
        weightList = [4, 4, 1, 1, 1, 6, 1, 4]

        frame = []
        frame.append(
            tk.Frame(
                self,
                bg="yellow",
            )
        )
        frame.append(
            tk.Frame(
                self,
                bg="gold",
            )
        )

        frame[0].pack(
            fill=tk.BOTH,
            expand=True,
        )
        frame[1].pack(
            fill=tk.BOTH,
            expand=True,
        )

        textField = [[], []]

        for i, label in enumerate(Global.LabelList):
            print(rowList[i], columnList[i], label)
            textField[rowList[i]].append(
                Widget.Textfield(
                    frame[rowList[i]],
                    label=label,
                    info=getattr(PT, label),
                    row=rowList[i],
                    column=columnList[i],
                ),
            )
        w = [1, 2, 1, 3]
        for i in range(8):
            frame[rowList[i]].grid_columnconfigure(
                rowList[i],
                weight=weightList[i],
            )

        frame[0].grid_rowconfigure(0, weight=1)
        frame[1].grid_rowconfigure(1, weight=1)


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
    def __init__(self, parent, PT, patient_page):
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

        tk.Button(
            self,
            text="↶",
            font=("Arial", 30, "bold"),
            fg="white",
            background="red",
            width=2,
            command=lambda: patient_page(),
        ).pack(
            side="left",
            fill=tk.Y,
        )

        banner = BannerFrame(self)
        patient = PatientFrame(self, PT=PT)


class ContentFrame(tk.Frame):
    def __init__(self, parent, patient_data):
        super().__init__(
            parent,
            bg=Color.contentFrameBG,
        )
        self.pack(
            side="top",
            expand=True,
            fill="both",
        )

        config = GraphConfigFrame(self)

        labTest = LabTestFrame(
            self,
            patient_data=patient_data,
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


class PatientListButton(tk.Frame):
    def __init__(self, parent, command=None):
        super().__init__(parent)
        self.pack()

        patientList = get.get_patient_list()

        for patient in patientList.itertuples():
            buttonText = f'[HN:{patient.HN}]    [AN:{patient.AN}] Ward: {patient.Ward}, Bed: {patient.Bed} "{patient.Name}"'
            tk.Button(
                self,
                text=buttonText,
                command=lambda HN=patient.HN: command(HN),
            ).pack()
