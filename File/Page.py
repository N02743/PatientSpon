import tkinter as tk
from tkinter import messagebox

from Var import Global

from File import Frame

from Data import getData as get


class Page(tk.Tk):
    def __init__(self, parent):
        self.parent = parent
        self.Page = self.patientListPage()

    def patientListPage(self):
        # TODO: main Nav Frame
        navFrame = Frame.PatientListNavFrame(self.parent, self.onClosing)

        # TODO: Patient list frame
        patientContent = Frame.PatientContentFrame(self.parent, self.open_ShowGraphPage)

    def showGraphPage(
        self,
        patient_id,
    ):
        Global.showGrid = True
        Global.showLabTest = True
        Global.showMedUsage = True

        # Get data
        PATIENT_DATA = get.get_patient_data_by_HN(patient_id)

        # Nav Frame
        navFrame = Frame.GraphNavFrame(
            self.parent,
            PatientData=PATIENT_DATA,
            patient_page=self.open_PatientListPage,
        )

        # Content Frame
        contentFrame = Frame.ContentFrame(
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
        self.clearPage()

        self.Page = self.showGraphPage(ID)

    def onClosing(self):
        if messagebox.askokcancel("Quit", "Do you really want to quit?"):
            self.parent.destroy()
        else:
            print("Close canceled")
