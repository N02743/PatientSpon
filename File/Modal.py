import tkinter as tk
from tkinter import ttk, messagebox

from PIL import Image, ImageTk
from pathlib import Path
from datetime import datetime


class ImageModal:
    def __init__(self, parent, imagePaths):
        self.parent = parent

        self.imagePaths = imagePaths

        self.index = 0
        self.imageAmount = len(self.imagePaths)

        self.photos = []

        self.window = tk.Toplevel(parent)
        # TODO: Image on xx/xx/xxxx date
        self.window.title(f"Image Viewer")
        self.window.grab_set()

        self.indexLabel = ttk.Label(self.window, text="")
        # self.indexLabel.pack(pady=5)
        self.indexLabel.grid(
            row=0,
            column=1,
            sticky="nsew",
            padx=5,
            pady=5,
        )

        self.filenameLabel = ttk.Label(self.window, text="")
        # self.filenameLabel.pack(pady=5)
        self.filenameLabel.grid(
            row=1,
            column=1,
            sticky="nsew",
            padx=5,
            pady=5,
        )

        self.imageLabel = ttk.Label(self.window)
        # self.imageLabel.pack(pady=5)
        self.imageLabel.grid(
            row=2,
            column=1,
            sticky="nsew",
            padx=5,
            pady=5,
        )

        self.nextButton = ttk.Button(
            self.window,
            text=">",
            command=self.nextImage,
        )
        # self.nextButton.pack(pady=(0, 10))
        self.nextButton.grid(
            row=2,
            column=2,
            sticky="nsew",
            padx=5,
            pady=5,
        )

        self.backButton = ttk.Button(
            self.window,
            text="<",
            command=self.backImage,
        )
        # self.backButton.pack(pady=(0, 10))
        self.backButton.grid(
            row=2,
            column=0,
            sticky="nsew",
            padx=5,
            pady=5,
        )

        self.window.grid_rowconfigure(0, weight=1)
        self.window.grid_rowconfigure(1, weight=1)
        self.window.grid_rowconfigure(2, weight=1)

        self.window.grid_columnconfigure(0, weight=1)
        self.window.grid_columnconfigure(1, weight=10)
        self.window.grid_columnconfigure(2, weight=1)

        self.showImage()

    def showImage(self):
        imagePath = self.imagePaths[self.index]

        self.indexLabel.config(text=f"{self.index + 1} / {self.imageAmount}")
        self.filenameLabel.config(text=imagePath.name)

        image = Image.open(imagePath).resize((400, 400))
        photo = ImageTk.PhotoImage(image)

        self.photos.append(photo)

        self.imageLabel.config(image=photo)
        self.buttonConfig()

    def nextImage(self):
        self.index = (self.index + 1) % len(self.imagePaths)

        self.showImage()

    def backImage(self):
        self.index = self.index - 1 if self.index > 0 else self.imageAmount - 1

        self.showImage()

    def buttonConfig(self):
        nextState = "normal"
        backState = "normal"

        if self.index == 0:
            backState = "disabled"
        elif self.index == self.imageAmount - 1:
            nextState = "disabled"

        self.nextButton.config(state=nextState)
        self.backButton.config(state=backState)
