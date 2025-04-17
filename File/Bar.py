import tkinter as tk

import File.Color as Color
import File.Variable as Var
import File.Widget as Widget
import File.Canvas as Canvas


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


class PatientFrame(tk.Frame):
    def __init__(self, parent, PT):
        super().__init__(parent)
        self.pack()

        LabelList = ["HN", "AN", "Ward", "Bed", "Sex", "Name", "Age", "PhoneNumber"]

        InfoTextField = []

        for label in LabelList:
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

        showLabButton = Widget.ButtonInput(self, text="Show Lab test")
        showMedButton = Widget.ButtonInput(self, text="Show Medication")
        addLabButton = Widget.ButtonInput(self, text="Add new Lab test")
        addMedButton = Widget.ButtonInput(self, text="Add new Medication")
        timeTickButton = Widget.ButtonInput(self, text="Time tick")


class ConfirmFrame(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.pack(side="right")

        confirmButton = Widget.ConfirmButton(self)
        resetButton = Widget.ResetButton(self)


class GraphConfigFrame(tk.Frame):
    def __init__(self, parent):
        super().__init__(
            parent,
            padx=Var.common_padding,
            pady=Var.common_padding,
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
    def __init__(self, parent, date_range, lab_results, medicine_usage):
        super().__init__(parent)
        self.pack()

        canvas = Canvas.CanvasGraph(
            self,
            date_range=date_range,
            lab_results=lab_results,
            medicine_usage=medicine_usage,
        )
