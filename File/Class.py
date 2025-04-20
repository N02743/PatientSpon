import pandas as pd
import Data.getData as get


class Patient:
    def __init__(
        self,
        patientPD,
    ):
        print("Patient =>", patientPD)
        self.HN = patientPD.iloc[0]["HN"]
        self.AN = patientPD.iloc[0]["AN"]
        self.Ward = patientPD.iloc[0]["Ward"]
        self.Bed = patientPD.iloc[0]["Bed"]
        self.Sex = patientPD.iloc[0]["Sex"]
        self.Name = patientPD.iloc[0]["Name"]
        self.Age = patientPD.iloc[0]["Age"]
        self.PhoneNumber = patientPD.iloc[0]["PhoneNumber"]

        # self.LabResults = get.get_labResults_data_by_HN(self.HN)
        # self.MedicineUsage = get.get_medicineUsage_data_by_HN(self.HN)

    def __str__(self):
        # TODO: string
        return ""
