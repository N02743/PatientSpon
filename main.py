import tkinter as tk
import random
import Variable

global PATIENT_DATA

global TEST

import Bar


def generate_timeline_data():
    data = []

    for i in range(20):
        x = random.randint(1, 30)
        data.append([f"drug {i}", x, random.randint(1, 31 - x) + x])

    return data


def get_timeline_data():
    # TODO: loading timeline data

    # dummy data by random gen
    return generate_timeline_data()


def plot_timeline():
    print()


def get_patient_data():
    # TODO: loading patient data
    pass


# def print_something(text):
#     print(text)

PATIENT_DATA = get_timeline_data()

app = tk.Tk()

app.title("Patient Spon form program")

print(PATIENT_DATA)

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
patient = Bar.PatientFrame(navFrame)

# Content Frame
contentFrame = Bar.ContentFrame(app)
config = Bar.GraphConfigFrame(contentFrame)

app.mainloop()
