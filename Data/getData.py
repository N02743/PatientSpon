import random
import pandas as pd
import File.Class as Class
import Var.Variable as Var

#         self.height = (self.total_rows * self.row_height) + (self.canvas_padding * 2)


def get_data():
    # TODO: get All data into one object Patient Class
    pass


def get_patient_data():
    # TODO: send data from previous page

    # TODO: loading patient data
    patientCSV = pd.read_csv("Data/PatientData.csv")

    # dummy data
    patient = patientCSV.iloc[0]
    PT = Class.Patient(patientPD=patient)

    return PT


def get_dateRange_data():
    # TODO: date range

    # TODO: Calculate max day fit in frame

    maxDays = (
        Var.window_width - Var.graphLabel_width - (Var.graphCanvas_padding * 2)
    ) // Var.graphDay_width

    date_range = []
    for i in range(maxDays):
        date_range.append(f"{i + 1} Apr")

    return date_range


def get_labResults_data_by_HN():
    # TODO: lab results
    lab_results = {
        "WBC": [5.5, None, 6.8, None, 6.7],
        "RBC": [4.7, 4.8, None, 5.0, 5.1],
    }

    return lab_results


def get_medicineUsage_data_by_HN():
    # TODO: medicine usage
    medicine_usage = [
        {"name": "Paracetamol", "start": 1, "end": 6},
        {"name": "Amoxicillin", "start": 2, "end": 4},
        {"name": "Iblutofel", "start": 2, "end": 9},
    ]

    return medicine_usage
