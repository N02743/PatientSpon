import random
import pandas as pd
import File.Class as Class
import Var.Variable as Var


# TODO: Duplicate at Canvas.py
def nextDay(date):
    return (pd.to_datetime(date, format="%d/%m/%Y") + pd.Timedelta(days=1)).strftime(
        "%d/%m/%Y"
    )


def findDays(start, end):
    return (
        pd.to_datetime(end, format="%d/%m/%Y")
        - pd.to_datetime(start, format="%d/%m/%Y")
    ).days


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

    days = findDays(start, end)

    # print(days)

    # maxDays = (
    #     Var.window_width - Var.graphLabel_width - (Var.graphCanvas_padding * 2)
    # ) // Var.graphDay_width

    date_range = []
    # TODO:
    iterDate = start
    for i in range(days + 1):
        # TODO: Show Year?
        date = pd.to_datetime(iterDate, format="%d/%m/%Y").strftime("%d %b").lstrip("0")
        date_range.append(date)
        iterDate = nextDay(iterDate)

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

    # To iterate till end date
    end = nextDay(end)

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
    medicineUsageCSV = pd.read_csv(
        "Data/mock_medicine_usage.csv",
        dtype={
            "HN": str,
            "Date": str,
        },
    )

    medicineUsage = medicineUsageCSV[medicineUsageCSV["HN"] == HN]

    # print(medicineUsage)

    medicineDict = {}

    medName = medicineUsage["MedName"].unique()
    for med in medName:
        medUsageInName = medicineUsage[medicineUsage["MedName"] == med]
        startDate = medUsageInName["Start"].values[0]
        endDate = medUsageInName["End"].values[0]
        medicineDict[med] = {"start": startDate, "end": endDate}

    # # TODO: medicine usage
    # medicine_usage = [
    #     {"name": "Paracetamol", "start": "01/03/2025", "end": "06/03/2025"},
    #     {"name": "Amoxicillin", "start": "02/03/2025", "end": "04/03/2025"},
    #     {"name": "Iblutofel", "start": "02/03/2025", "end": "07/03/2025"},
    # ]

    # return medicine_usage
    return medicineDict
