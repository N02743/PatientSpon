import pandas as pd
import Data.getData as get


class Patient:
    def __init__(
        self,
        patientPD,
    ):
        self.HN = patientPD["HN"]
        self.AN = patientPD["AN"]
        self.Ward = patientPD["Ward"]
        self.Bed = patientPD["Bed"]
        self.Sex = patientPD["Sex"]
        self.Name = patientPD["Name"]
        self.Age = patientPD["Age"]
        self.PhoneNumber = patientPD["PhoneNumber"]

        self.LabResults = get.get_labResults_data_by_HN()
        self.MedicineUsage = get.get_medicineUsage_data_by_HN()

    def __str__(self):
        # TODO: string
        return ""
