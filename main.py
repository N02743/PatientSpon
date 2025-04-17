import tkinter as tk
import Variable
import pandas as pd
import Class
import getData as get

global PATIENT_DATA

global TEST

import Bar


def plot_timeline():
    print()


# Get data
TIMELINE_DATA = get.get_timeline_data()
PATIENT_DATA = get.get_patient_data()
DATERANGE_DATA = get.get_dateRange_data()
LABRESULTS_DATA = get.get_labResults_data()
MEDICINEUSAGE_DATA = get.get_medicineUsage_data()

app = tk.Tk()

app.title("Patient Spon form program")

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


# Nav Frame
navFrame = Bar.NavFrame(app)

banner = Bar.BannerFrame(navFrame)
patient = Bar.PatientFrame(navFrame, PT=PATIENT_DATA)

# Content Frame
contentFrame = Bar.ContentFrame(app)

config = Bar.GraphConfigFrame(contentFrame)


# TODO: graph show
labTest = Bar.LabTestFrame(
    contentFrame,
    drugsTL=TIMELINE_DATA,
    date_range=DATERANGE_DATA,
    lab_results=LABRESULTS_DATA,
    medicine_usage=MEDICINEUSAGE_DATA,
)

app.mainloop()
