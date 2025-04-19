import random
import pandas as pd
import File.Class as Class
import Var.Variable as Var

#         self.height = (self.total_rows * self.row_height) + (self.canvas_padding * 2)


def get_data():
    # TODO: get All data into one object Patient Class
    pass


# TODO: Duplicate at Canvas.py
def nextDay(date):
    return (pd.to_datetime(date, format="%d/%m/%Y") + pd.Timedelta(days=1)).strftime(
        "%d/%m/%Y"
    )


def get_patient_data_by_HN(HN):
    # TODO: send data from previous page

    # TODO: loading patient data
    patientCSV = pd.read_csv(
        "Data/Random/PatientData.csv",
        dtype={
            "HN": str,
            "AN": str,
            "PhoneNumber": str,
        },
    )

    # dummy data
    patient = patientCSV[patientCSV["HN"] == HN]
    # print(patient)
    PT = Class.Patient(patientPD=patient)

    return PT


def get_dateRange_data(start, end):
    # TODO: date range

    maxDays = (
        Var.window_width - Var.graphLabel_width - (Var.graphCanvas_padding * 2)
    ) // Var.graphDay_width

    date_range = []
    # TODO:
    for i in range(10):
        date_range.append(f"{i + 1} Apr")
    # for i in range():
    #     date_range.append(f"{i + 1} Apr")

    return date_range


def get_labResults_data_by_HN(HN, start, end):
    labResultCSV = pd.read_csv(
        "Data/mock_lab_results.csv",
        dtype={
            "HN": str,
            "Date": str,
        },
    )
    labResult = labResultCSV[labResultCSV["HN"] == HN]

    iterDate = start
    labName = labResult["LabName"].unique()

    labList = {}
    for name in labName:
        labList[name] = {}

    while iterDate != end:
        labInDate = labResult[labResult["Date"] == iterDate]
        for name in labName:
            labInName = labInDate[labInDate["LabName"] == name]

            if not labInName.empty:
                labList[name][iterDate] = float(labInName["Result"].values[0])

            else:
                labList[name][iterDate] = None

        iterDate = nextDay(iterDate)

    return labList


def get_medicineUsage_data_by_HN(HN, start, end):
    # TODO: medicine usage
    medicine_usage = [
        {"name": "Paracetamol", "start": 1, "end": 6},
        {"name": "Amoxicillin", "start": 2, "end": 4},
        {"name": "Iblutofel", "start": 2, "end": 9},
    ]

    return medicine_usage
