import pandas as pd
import Data.getData as get


class Patient:
    def __init__(
        self,
        patientPD,
    ):
        self.HN = patientPD.loc[0, "HN"]
        self.AN = patientPD.loc[0, "AN"]
        self.Ward = patientPD.loc[0, "Ward"]
        self.Bed = patientPD.loc[0, "Bed"]
        self.Sex = patientPD.loc[0, "Sex"]
        self.Name = patientPD.loc[0, "Name"]
        self.Age = patientPD.loc[0, "Age"]
        self.PhoneNumber = patientPD.loc[0, "PhoneNumber"]

        # self.LabResults = get.get_labResults_data_by_HN(self.HN)
        # self.MedicineUsage = get.get_medicineUsage_data_by_HN(self.HN)

    def __str__(self):
        # TODO: string
        return ""
