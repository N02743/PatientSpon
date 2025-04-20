import tkinter as tk

import Data.getData as get
import File.Bar as Bar
import Var.GlobalVariable as Var


class showGraph(tk.Tk):
    def __init__(self, parent, patient_id):
        # TODO: show graph page class

        # Get data
        PATIENT_DATA = get.get_patient_data_by_HN(patient_id)

        # Nav Frame
        navFrame = Bar.NavFrame(parent)

        banner = Bar.BannerFrame(navFrame)
        patient = Bar.PatientFrame(navFrame, PT=PATIENT_DATA)

        # Content Frame
        contentFrame = Bar.ContentFrame(parent)

        config = Bar.GraphConfigFrame(contentFrame)

        # Graph show
        labTest = Bar.LabTestFrame(
            contentFrame,
            patient_data=PATIENT_DATA,
        )
