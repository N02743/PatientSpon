import random
import pandas as pd
import Class


def generate_timeline_data():
    data = {}

    for i in range(5):
        x = random.randint(1, 30)
        # data.append([f"drug {i}": x, random.randint(1, 31 - x) + x])
        data[f"drug {i}"] = [x, random.randint(1, 31 - x) + x]

    return data


def get_timeline_data():
    # TODO: loading timeline data

    # dummy data by random gen
    return generate_timeline_data()


def get_patient_data():
    # TODO: send data from previous page

    # TODO: loading patient data
    patientCSV = pd.read_csv("PatientData.csv")

    # dummy data
    patient = patientCSV.iloc[0]
    PT = Class.Patient(patientPD=patient)

    return PT


def get_dateRange_data():
    # TODO: date range
    date_range = ["1 Apr", "2 Apr", "3 Apr", "4 Apr", "5 Apr"]

    return date_range


def get_labResults_data():
    # TODO: lab results
    lab_results = {
        "WBC": [5.5, None, 6.8, None, 6.7],
        "RBC": [4.7, 4.8, None, 5.0, 5.1],
    }

    return lab_results


def get_medicineUsage_data():
    # TODO: medicine usage
    medicine_usage = [
        {"name": "Paracetamol", "start": 1, "end": 3},
        {"name": "Amoxicillin", "start": 2, "end": 4},
        {"name": "Iblutofel", "start": 2, "end": 3},
    ]

    return medicine_usage
