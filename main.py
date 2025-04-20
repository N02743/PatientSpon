import tkinter as tk
import Page
import Var
import File.Bar as Bar


def graph_page(ID):
    for widget in app.winfo_children():
        widget.destroy()

    PAGE = Page.showGraph(app, ID)


def patient_page():
    PAGE = Bar.NavFrame(app)


patient_id = ["0000000000", "1111111111"]

app = tk.Tk()

app.title("Patient Spon form program")
app.state("zoomed")

app.update_idletasks()
Var.window_width = app.winfo_width()

# graph_page()
# patient_page()
bt = tk.Button(app, text="patient 0", command=lambda: graph_page(patient_id[0])).pack()
bt2 = tk.Button(app, text="patient 1", command=lambda: graph_page(patient_id[1])).pack()

app.mainloop()

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
