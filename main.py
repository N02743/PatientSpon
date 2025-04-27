import tkinter as tk
import Page
import Var
import File.Frame as Frame
from tkinter import messagebox


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
        onClosing=onClosing,
    )


def onClosing():
    if messagebox.askokcancel("Quit", "Do you really want to quit?"):
        app.destroy()  # ปิดจริง
    else:
        print("Close canceled")


app = tk.Tk()

app.title("Patient Spon form program")
app.attributes("-fullscreen", True)
app.bind("<Escape>", lambda e: onClosing())

app.protocol("WM_DELETE_WINDOW", onClosing)

app.update_idletasks()
Var.window_width = app.winfo_width()

PAGE = Page.patientList(
    app,
    graph_page=graph_page,
    onClosing=onClosing,
)

# for develop
# PAGE = Page.showGraph(app, "0000000000", patient_page)

app.mainloop()
