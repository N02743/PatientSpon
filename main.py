import tkinter as tk
import random
import Variable
import pandas as pd
import Class

global PATIENT_DATA

global TEST

import Bar


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


def plot_timeline():
    print()


def get_patient_data():
    # TODO: send data from previous page

    # TODO: loading patient data
    patientCSV = pd.read_csv("PatientData.csv")

    # dummy data
    patient = patientCSV.iloc[0]
    PT = Class.Patient(patientPD=patient)

    return PT


# def print_something(text):
#     print(text)

TL = get_timeline_data()

app = tk.Tk()

app.title("Patient Spon form program")

# print(PATIENT_DATA)

app.state("zoomed")


# # ฟังก์ชันเปลี่ยนหน้า
# def show_page(page_name):
#     for widget in contentFrame.winfo_children():
#         widget.destroy()

#     label = tk.Label(
#         contentFrame,
#         text=f"คุณอยู่ที่หน้า {page_name}",
#         font=("Arial", 20),
#     )
#     label.pack(expand=True)

# TODO: patient data
PT = get_patient_data()

# Nav Frame
navFrame = Bar.NavFrame(app)

banner = Bar.BannerFrame(navFrame)
patient = Bar.PatientFrame(navFrame, PT=PT)

# Content Frame
contentFrame = Bar.ContentFrame(app)

config = Bar.GraphConfigFrame(contentFrame)


# TODO: graph show
labTest = Bar.LabTestFrame(contentFrame, TL)

app.mainloop()
