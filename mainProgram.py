import tkinter as tk
import pandas as pd

import File.getData as get
import File.Bar as Bar
import File.Variable as Var

app = tk.Tk()

app.title("Patient Spon form program")

app.state("zoomed")

# TODO: calculate window everytime that resize
app.update_idletasks()
Var.window_width = app.winfo_width()

# Get data
PATIENT_DATA = get.get_patient_data()
DATERANGE_DATA = get.get_dateRange_data()
LABRESULTS_DATA = get.get_labResults_data()
MEDICINEUSAGE_DATA = get.get_medicineUsage_data()


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


# Graph show
labTest = Bar.LabTestFrame(
    contentFrame,
    date_range=DATERANGE_DATA,
    lab_results=LABRESULTS_DATA,
    medicine_usage=MEDICINEUSAGE_DATA,
)


app.mainloop()
