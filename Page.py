import tkinter as tk

import Data.getData as get
import File.Frame as Frame
import Var.Global as Global


class showGraph(tk.Tk):
    def __init__(
        self,
        parent,
        patient_id,
        patient_page,
    ):
        Global.showGrid = True
        Global.showLabTest = True
        Global.showMedUsage = True

        # Get data
        PATIENT_DATA = get.get_patient_data_by_HN(patient_id)

        # Nav Frame
        navFrame = Frame.GraphNavFrame(
            parent,
            PT=PATIENT_DATA,
            patient_page=patient_page,
        )

        # Content Frame
        contentFrame = Frame.ContentFrame(
            parent,
            patient_data=PATIENT_DATA,
        )


class patientList(tk.Tk):
    def __init__(
        self,
        parent,
        graph_page,
    ):

        # TODO: main Nav Frame
        navFrame = Frame.PatientListNavFrame(parent)

        # TODO: Patient list frame
        # patientList = Frame.PatientListFrame(parent, graph_page)
        patientContent = Frame.PatientContentFrame(parent, graph_page)
