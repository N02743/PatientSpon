import tkinter as tk
import Page
import Var
import File.Frame as Frame


def graph_page(ID):
    for widget in app.winfo_children():
        widget.destroy()

    PAGE = Page.showGraph(
        app,
        ID,
        patient_page=patient_page,
    )


def patient_page():
    for widget in app.winfo_children():
        widget.destroy()

    PAGE = Page.patientList(
        app,
        graph_page=graph_page,
    )


app = tk.Tk()

app.title("Patient Spon form program")
app.state("zoomed")

app.update_idletasks()
Var.window_width = app.winfo_width()

# PAGE = Page.patientList(app, graph_page)

# for develop
PAGE = Page.showGraph(app, "0000000000", patient_page)

app.mainloop()
