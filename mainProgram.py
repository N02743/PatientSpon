import tkinter as tk
import pandas as pd

import Data.getData as get
import File.Bar as Bar
import Var.Variable as Var

app = tk.Tk()

app.title("Patient Spon form program")

app.state("zoomed")

# TODO: calculate window everytime that resize
app.update_idletasks()
Var.window_width = app.winfo_width()

patient_id = "0000000000"
# TODO: init start -> 01/present_month, end -> "" -> show max available
start_date = "01/03/2025"
end_date = "10/03/2025"

# Get data
PATIENT_DATA = get.get_patient_data_by_HN(patient_id)
DATERANGE_DATA = get.get_dateRange_data(
    start=start_date,
    end=end_date,
)
# LABRESULTS_DATA = get.get_labResults_data_by_HN()
# MEDICINEUSAGE_DATA = get.get_medicineUsage_data_by_HN()


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
    # date_range=DATERANGE_DATA,
    patient_data=PATIENT_DATA,
)


app.mainloop()
