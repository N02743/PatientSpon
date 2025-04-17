import pandas as pd


class Patient:
    def __init__(
        self,
        patientPD,
        # HN,
        # AN,
        # Ward,
        # Bed,
        # Sex,
        # Name,
        # Age,
        # PhoneNumber,
    ):
        # self.HN = HN
        # self.AN = AN
        # self.Ward = Ward
        # self.Bed = Bed
        # self.Sex = Sex
        # self.Name = Name
        # self.Age = Age
        # self.PhoneNumber = PhoneNumber
        self.HN = patientPD["HN"]
        self.AN = patientPD["AN"]
        self.Ward = patientPD["Ward"]
        self.Bed = patientPD["Bed"]
        self.Sex = patientPD["Sex"]
        self.Name = patientPD["Name"]
        self.Age = patientPD["Age"]
        self.PhoneNumber = patientPD["PhoneNumber"]

    def __str__(self):
        # TODO: string
        return ""

    def get(self, label):
        if label == "HN":
            return self.HN
