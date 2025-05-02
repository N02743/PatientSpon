import pandas as pd

from File import Class
from Var import Var as Var

from datetime import datetime
from pathlib import Path

import re

# patientDataFilePath = "Data/PatientData.csv"
patientDataFilePath = "Data/PatientData50.csv"
# labResultFilePath = "Data/mock_lab_results.csv"
# medicineUsageFilePath = "Data/mock_medicine_usage.csv"
labResultFilePath = "Data/LabResultData.csv"
medicineUsageFilePath = "Data/MedicineUsage.csv"


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


def get_patient_list():
    patientCSV = pd.read_csv(
        patientDataFilePath,
        dtype={
            "HN": str,
            "AN": str,
            "PhoneNumber": str,
        },
    )

    return patientCSV


def get_patient_data_by_HN(HN):
    patientCSV = pd.read_csv(
        patientDataFilePath,
        dtype={
            "HN": str,
            "AN": str,
            "PhoneNumber": str,
        },
    )

    patient = patientCSV[patientCSV["HN"] == HN]

    if patient is None:
        print("Patient None", HN)
        return None
    else:
        print("DEBUG PATIENT", patient)

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
        labResultFilePath,
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
        medicineUsageFilePath,
        dtype={
            "HN": str,
            "Date": str,
        },
    )

    medicineUsage = medicineUsageCSV[medicineUsageCSV["HN"] == HN]

    medicineDict = {}

    medName = medicineUsage["MedName"].unique()
    for med in medName:
        medUsageInName = medicineUsage[medicineUsage["MedName"] == med]
        startDate = medUsageInName["Start"].values[0]
        endDate = medUsageInName["End"].values[0]
        medicineDict[med] = {"start": startDate, "end": endDate}

    return medicineDict


def get_image_paths_by_HN_and_Date(HN, Date_str):
    # TODO: Try except?
    dateCheck = datetime.strptime(Date_str, r"%d/%m/%Y").date()

    path = "Data/Image/PatientImage"
    dirPath = Path(path) / str(HN)

    # print(dirPath.resolve())

    if not dirPath.exists():
        # print("Not exists")
        # TODO:
        return []

    imagePathList = []
    for file in dirPath.glob("*.jpg"):
        dateNow = datetime.strptime(file.stem, r"%Y-%m-%d_%H-%M-%S").date()
        if dateNow == dateCheck:
            imagePathList.append(file)

    imagePathList = sorted(imagePathList)

    # print("Can return:", imagePathList)
    return imagePathList


def if_no_image_for_button(HN, Date) -> bool:
    Date = datetime.strptime(Date, "%d/%m/%Y").date()
    date_str = Date.strftime("%Y-%m-%d")

    pattern = re.compile(rf"^{date_str}_\d{{2}}-\d{{2}}-\d{{2}}\.jpg$")

    path = "Data/Image/PatientImage"
    dirPath = Path(path) / str(HN)

    # print(HN, Date)

    if not dirPath.exists():
        # print("Not exists")
        return True

    for file in dirPath.glob("*.jpg"):
        # print(file.name)
        if pattern.match(file.name):
            # print("match", file.name)
            return False

    # print("No Image")
    return True
