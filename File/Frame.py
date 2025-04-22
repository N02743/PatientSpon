import tkinter as tk

import Var.GlobalVariable as Global
import Var.Variable as Var
import Var.Color as Color
import Var.Font as Font

import File.Widget as Widget
import File.Canvas as Canvas

import Data.getData as get

import File.GlobalFunction as GLBFunc


def buttonColor(variable, check):
    # TODO: Weird
    if variable:
        if variable == check:
            return Color.buttonTrueBG
        else:
            return Color.buttonWaitTrueBG
    else:
        if variable == check:
            return Color.buttonFalseBG
        else:
            return Color.buttonWaitFalseBG

    # return Color.buttonTrueBG if variable else Color.buttonFalseBG


def toggleGrid():
    # Global.showGrid = not Global.showGrid
    global showGrid
    showGrid = not showGrid
    showGridButton.config(
        bg=buttonColor(
            showGrid,
            Global.showGrid,
        ),
    )
    print("toggle grid =>", showGrid)


def toggleLabTest():
    # Global.showLabTest = not Global.showLabTest
    global showLab
    showLab = not showLab
    showLabButton.config(
        bg=buttonColor(
            showLab,
            Global.showLabTest,
        ),
    )
    print("toggle Lab test =>", showLab)


def toggleMedUsage():
    # Global.showMedUsage = not Global.showMedUsage
    global showMed
    showMed = not showMed
    showMedButton.config(
        bg=buttonColor(
            showMed,
            Global.showMedUsage,
        ),
    )
    print("toggle Medicine Usage =>", showMed)


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
    Global.showGrid = showGrid
    Global.showLabTest = showLab
    Global.showMedUsage = showMed

    showGridButton.config(
        bg=buttonColor(
            showGrid,
            Global.showGrid,
        ),
    )
    showLabButton.config(
        bg=buttonColor(
            showLab,
            Global.showLabTest,
        ),
    )
    showMedButton.config(
        bg=buttonColor(
            showMed,
            Global.showMedUsage,
        ),
    )

    GLBFunc.CanvasRedraw()

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

        weightList = [15, 15, 1, 1, 1, 15, 1, 4]

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
            row = 0 if i < 4 else 1
            column = i if i < 4 else i - 4

            textField[row].append(
                Widget.Textfield(
                    frame[row],
                    label=label,
                    info=getattr(PT, label),
                    row=row,
                    column=column,
                ),
            )

        for i in range(8):
            row = 0 if i < 4 else 1
            column = i if i < 4 else i - 4

            frame[row].grid_columnconfigure(
                column,
                weight=weightList[i],
            )

        frame[0].grid_rowconfigure(0, weight=1)
        frame[1].grid_rowconfigure(1, weight=1)


class ConfigButtonFrame(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.pack(side="left")

        # TODO: Config Button
        global showLabButton
        global showLab
        showLab = Global.showLabTest
        showLabButton = Widget.ButtonInput(
            self,
            text="Show Lab test",
            command=lambda: toggleLabTest(),
            bgColor=buttonColor(
                showLab,
                Global.showLabTest,
            ),
        )

        global showMedButton
        global showMed
        showMed = Global.showMedUsage
        showMedButton = Widget.ButtonInput(
            self,
            text="Show Medication",
            command=lambda: toggleMedUsage(),
            bgColor=buttonColor(
                showMed,
                Global.showMedUsage,
            ),
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

        global showGridButton
        global showGrid
        showGrid = Global.showGrid
        showGridButton = Widget.ButtonInput(
            self,
            text="Show grid",
            command=lambda: toggleGrid(),
            bgColor=buttonColor(
                showGrid,
                Global.showGrid,
            ),
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
            # command=lambda: confirmButtonFunction(),
            # TODO:
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

        GLBFunc.CanvasRedrawSet(canvas.redraw)


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
