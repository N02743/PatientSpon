import tkinter as tk
from tkinter import messagebox

from Var import Global

from Data import getData as get

from File import patientListWidget as patientList
from File import showGraphWidget as showGraph


# class Page(tk.Tk):
class Page(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.grid(
            row=0,
            column=0,
            sticky="nsew",
            padx=5,
            pady=5,
        )
        self.parent = parent
        self.Page = self.patientListPage()

    def patientListPage(self):
        navFrame = patientList.NavFrame(
            self.parent,
            self.onClosing,
        )

        # configFrame = patientList.GraphConfigFrame(self.parent)

        self.patientContent = patientList.ContentFrame(
            self.parent,
            self.open_ShowGraphPage,
        )

    def showGraphPage(
        self,
        patient_id,
    ):
        Global.showGrid = True
        Global.showLabTest = True
        Global.showMedUsage = True

        PATIENT_DATA = get.get_patient_data_by_HN(patient_id)

        navFrame = showGraph.NavFrame(
            self.parent,
            PatientData=PATIENT_DATA,
            patient_page=self.open_PatientListPage,
        )

        # configFrame = showGraph.GraphConfigFrame(self.parent)

        contentFrame = showGraph.ContentFrame(
            self.parent,
            patient_data=PATIENT_DATA,
        )

    def clearPage(self):
        for widget in self.parent.winfo_children():
            widget.destroy()

    def open_PatientListPage(self):
        self.clearPage()

        self.Page = self.patientListPage()

    def open_ShowGraphPage(self, ID):
        self.patientContent.unbindScroll()
        self.clearPage()

        self.Page = self.showGraphPage(ID)

    def onClosing(self):
        if messagebox.askokcancel(
            "Quit",
            "Do you really want to quit?",
        ):
            self.parent.destroy()
        else:
            print("Close canceled")
