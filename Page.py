import tkinter as tk

from Var import Global

from File import Frame

from Data import getData as get


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
            PatientData=PATIENT_DATA,
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
        onClosing,
    ):

        # TODO: main Nav Frame
        navFrame = Frame.PatientListNavFrame(parent, onClosing)

        # TODO: Patient list frame
        patientContent = Frame.PatientContentFrame(parent, graph_page)
