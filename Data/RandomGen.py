import random
import pandas as pd

# import File.Class as Class

patientAmount = 10

patient_csv = pd.read_csv(
    "Data/Random/PatientData.csv",
    dtype={
        "HN": str,
        "AN": str,
        "PhoneNumber": str,
    },
)

print(len(patient_csv))
print(patient_csv.iloc[0])

# TODO: gen data


def genPatientData():
    for i in range(patientAmount):
        pass
