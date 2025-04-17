import tkinter as tk
import Variable as Var

from tkinter import messagebox


def showImageModal(i):
    # TODO: show Image modal
    messagebox.showinfo("Image", f"Show image for {i}")


# def toggle_grid():
#     global show_grid
#     show_grid = not show_grid
#     grid_btn.config(text=f"Grid: {'ON' if show_grid else 'OFF'}")
#     redraw()


def showGridLines():
    # TODO: togle grid line button function
    # if show_grid:
    #     top = canvas_padding
    #     bottom = canvas_height - canvas_padding
    #     for i in range(len(date_range) + 1):
    #         x = day_x(i) + 40
    #         line = canvas.create_line(x, top, x, bottom, fill="#ccc", dash=(2, 4))
    #         grid_lines.append(line)
    pass


class CanvasGraph(tk.Canvas):
    def __init__(
        self,
        parent,
        date_range,
        lab_results,
        medicine_usage,
    ):
        super().__init__(parent, bg="white")
        self.pack()

        self.setVariableFromFile()
        self.setVariableFromParameter(date_range, lab_results, medicine_usage)

        self.reconfighWidthAndHeight()

        # TODO: expand size calculate

        row_idx = 0

        # Image row
        row_idx = self.createImageButton(row_idx)

        # Lab results
        row_idx = self.drawLabResults(lab_results, row_idx)

        # Day Range
        row_idx = self.drawDayRange(row_idx)

        # Medicine
        self.DrawMedicine(medicine_usage, row_idx)

    def setVariableFromParameter(self, date_range, lab_results, medicine_usage):
        self.date_range = date_range
        self.lab_results = lab_results
        self.medicine_usage = medicine_usage

        lab_test_rows = len(self.lab_results)
        medicine_usage_rows = len(self.medicine_usage)
        self.total_rows = 1 + lab_test_rows + 1 + medicine_usage_rows

    def setVariableFromFile(self):
        self.label_width = Var.graphLabel_width
        self.day_width = Var.graphDay_width
        self.row_height = Var.graphRow_height
        self.canvas_padding = Var.graphCanvas_padding

    def DrawMedicine(self, medicine_usage, row_idx):
        for med in medicine_usage:
            y = self.row_y(row_idx)
            self.create_text(
                5,
                y + 10,
                anchor="w",
                text=med["name"],
                font=Var.graph_font,
            )

            start_idx = med["start"] - 1
            end_idx = med["end"] - 1
            x1 = self.day_x(start_idx) + self.day_width // 2
            x2 = self.day_x(end_idx) + self.day_width // 2
            timelinePositionY = y + 10

            self.drawTimeline(x1, x2, timelinePositionY)

            row_idx += 1

    def drawTimeline(self, x1, x2, timelinePositionY):
        self.create_line(
            x1, timelinePositionY, x2, timelinePositionY, fill="blue", width=6
        )
        self.create_oval(
            x1 - 5, timelinePositionY - 5, x1 + 5, timelinePositionY + 5, fill="green"
        )
        self.create_oval(
            x2 - 5, timelinePositionY - 5, x2 + 5, timelinePositionY + 5, fill="red"
        )

    def drawDayRange(self, row_idx):
        y = self.row_y(row_idx)
        self.create_text(
            5,
            y + 10,
            anchor="w",
            text="Day",
            font=Var.graph_font,
        )
        for i in range(len(self.date_range)):
            x = self.day_x(i) + self.day_width // 2
            self.create_text(x, y + 10, text=str(i + 1))
        row_idx += 1
        return row_idx

    def drawLabResults(self, lab_results, row_idx):
        for test, values in lab_results.items():
            y = self.row_y(row_idx)
            self.create_text(
                5,
                y + 10,
                anchor="w",
                text=test,
                font=Var.graph_font,
            )
            for i, val in enumerate(values):
                if val is not None:
                    x = self.day_x(i) + self.day_width // 2
                    self.create_text(
                        x,
                        y + 10,
                        text=str(val),
                        font=Var.graph_font,
                    )
            row_idx += 1
        return row_idx

    def createImageButton(self, row_idx):
        for i in range(len(self.date_range)):
            x = self.day_x(i) + self.day_width // 2
            y = self.row_y(row_idx)
            btn = tk.Button(
                self,
                text="📷",
                command=lambda d=i: showImageModal(d),
                width=2,
            )
            self.create_window(x, y + 25, window=btn)
        row_idx += 1

        return row_idx

    def day_x(self, index):
        return self.label_width + index * self.day_width

    def row_y(self, index):
        return self.canvas_padding + index * self.row_height

    def recalWidthAndHeight(self):
        # TODO: Calculate width and height
        self.width = (
            self.label_width
            + (len(self.date_range) * self.day_width)
            + (self.canvas_padding * 2)
        )
        self.height = (self.total_rows * self.row_height) + (self.canvas_padding * 2)

    def reconfighWidthAndHeight(self):
        self.recalWidthAndHeight()
        self.config(
            width=self.width,
            height=self.height,
        )

    def redraw(self):
        self.delete("all")
        self.reconfighWidthAndHeight()

        # TODO: Image Button

        # TODO: Lab test

        # TODO: Day Range Line

        # TODO: Medicine Usage
