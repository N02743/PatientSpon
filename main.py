import tkinter as tk
from tkinter import messagebox

from Var import Var

from File import Page


def onClosing():
    if messagebox.askokcancel(
        "Quit",
        "Do you really want to quit?",
    ):
        app.destroy()
    else:
        print("Close canceled")


app = tk.Tk()

app.title("Patient Spon form program")

app.attributes("-fullscreen", True)
app.bind("<Escape>", lambda e: onClosing())
app.protocol("WM_DELETE_WINDOW", onClosing)

app.update_idletasks()
Var.window_width = app.winfo_width()

PAGE = Page.Page(app)

app.grid_rowconfigure(0, weight=1)
app.grid_rowconfigure(1, weight=10)

app.grid_columnconfigure(0, weight=1)

app.mainloop()
