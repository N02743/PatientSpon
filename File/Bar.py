import tkinter as tk

import Var.Variable as Var
import Var.Color as Color
import Var.Font as Font

import File.Widget as Widget
import File.Canvas as Canvas


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

        for label in Var.LabelList:
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
        showLabButton = Widget.ButtonInput(self, text="Show Lab test")
        showMedButton = Widget.ButtonInput(self, text="Show Medication")
        addLabButton = Widget.ButtonInput(self, text="Add new Lab test")
        addMedButton = Widget.ButtonInput(self, text="Add new Medication")
        timeTickButton = Widget.ButtonInput(self, text="Time tick")


class ConfirmFrame(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.pack(side="right")

        # TODO: Confirm and Reset
        confirmButton = Widget.ConfirmButton(self)
        resetButton = Widget.ResetButton(self)


class GraphConfigFrame(tk.Frame):
    def __init__(self, parent):
        super().__init__(
            parent,
            padx=Var.configFrame_padding,
            pady=Var.configFrame_padding,
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
        date_range,
        patient_data,
    ):
        super().__init__(parent)
        self.pack()

        canvas = Canvas.CanvasGraph(
            self,
            date_range=date_range,
            patient_data=patient_data,
        )
