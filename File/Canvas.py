import tkinter as tk
import Var.Variable as Var

import Var.Font as Font
import File.Class as Class

from tkinter import messagebox

import Data.getData as get
import pandas as pd


def showImageModal(i):
    # TODO: show Image modal
    pictureDirectory = "Data/Image"
    messagebox.showinfo("Image", f"Show image for {i}")


# TODO: Duplicate at getData.py
def nextDay(date):
    return (pd.to_datetime(date, format="%d/%m/%Y") + pd.Timedelta(days=1)).strftime(
        "%d/%m/%Y"
    )


# def toggle_grid():
#     global show_grid
#     show_grid = not show_grid
#     grid_btn.config(text=f"Grid: {'ON' if show_grid else 'OFF'}")
#     redraw()


class CanvasGraph(tk.Canvas):
    def __init__(
        self,
        parent,
        date_range,
        patient_data: Class.Patient,
    ):
        super().__init__(parent, bg="white")
        self.pack()

        self.showGrid = True
        self.patient_data = patient_data

        # TODO: check if valid (end is after start)
        self.startDate = "01/03/2025"
        self.endDate = "07/03/2025"

        self.redraw(
            date_range=date_range,
        )

    # return x position at center for row = 0 at day = index
    def day_x(self, index):
        return self.label_width + index * self.day_width + self.day_width // 2

    # return y position for element in graph at row = row_idx
    def row_y(self):
        return self.canvas_padding + self.row_idx * self.row_height

    def setVariableFromFile(self):
        self.label_width = Var.graphLabel_width
        self.day_width = Var.graphDay_width
        self.row_height = Var.graphRow_height
        self.canvas_padding = Var.graphCanvas_padding

    def setVariableFromParameter(
        self,
        date_range,
        # lab_results,
        # medicine_usage,
    ):
        self.date_range = date_range
        # TODO: get at another position
        self.lab_results = get.get_labResults_data_by_HN(
            HN=self.patient_data.HN,
            start=self.startDate,
            end=self.endDate,
        )
        self.medicine_usage = get.get_medicineUsage_data_by_HN(
            HN=self.patient_data.HN,
            start=self.startDate,
            end=self.endDate,
        )

        lab_test_rows = len(self.lab_results)
        medicine_usage_rows = len(self.medicine_usage)
        self.total_rows = 1 + lab_test_rows + 1 + medicine_usage_rows

    def reconfighWidthAndHeight(self):
        self.recalWidthAndHeight()
        self.config(
            width=self.width,
            height=self.height,
        )

    def recalWidthAndHeight(self):
        self.width = (
            self.label_width
            + (len(self.date_range) * self.day_width)
            + (self.canvas_padding * 2)
        )

        self.height = (self.total_rows * self.row_height) + (self.canvas_padding * 2)

    def createImageButton(self):
        for i in range(len(self.date_range)):
            x = self.day_x(i)
            y = self.row_y()
            btn = tk.Button(
                self,
                text="📷",
                command=lambda d=i: showImageModal(d),
                width=2,
            )
            self.create_window(x, y + 25, window=btn)
        self.row_idx += 1

    def drawLabResults(self):
        labResults = self.lab_results

        for labTest in labResults.keys():
            y = self.row_y()
            self.create_text(
                5,
                y + 10,
                anchor="w",
                text=labTest,
                font=Font.graph,
            )

            labResultsOnName = labResults[labTest]

            for i, date in enumerate(labResultsOnName.keys()):
                result = labResultsOnName[date]

                if result is not None:
                    x = self.day_x(i)
                    self.create_text(
                        x,
                        y + 10,
                        text=str(result),
                        font=Font.graph,
                    )
            self.row_idx += 1

    def drawDayRange(self):
        y = self.row_y()
        self.create_text(
            5,
            y + 10,
            anchor="w",
            text="Day",
            font=Font.dayRangeLabel,
        )
        for i in range(len(self.date_range)):
            x = self.day_x(i)
            self.create_line(
                x,
                y - 10,
                x,
                y + 10,
                fill="black",
                width=3,
            )
            self.create_text(
                x,
                y + 20,
                text=str(self.date_range[i]),
                font=Font.dayRange,
            )

        self.create_line(
            self.day_x(0) - Var.dayRange_padding,
            y,
            self.day_x(len(self.date_range) - 1) + Var.dayRange_padding,
            y,
            fill="black",
            width=6,
            arrow=tk.BOTH,
            arrowshape=(10, 12, 6),
        )
        self.row_idx += 1

    def DrawMedicine(self):
        for med in self.medicine_usage:
            y = self.row_y()
            self.create_text(
                5,
                y + 10,
                anchor="w",
                text=med["name"],
                font=Font.graph,
            )

            start_idx = med["start"] - 1
            end_idx = med["end"] - 1
            x1 = self.day_x(start_idx)
            x2 = self.day_x(end_idx)
            timelinePositionY = y + 10

            # TODO: draw timeline add arrow if out of bound
            self.drawTimeline(x1, x2, timelinePositionY)

            self.row_idx += 1

    def drawTimeline(self, x1, x2, timelinePosY):
        self.create_line(
            x1,
            timelinePosY,
            x2,
            timelinePosY,
            fill="black",
            width=6,
        )
        self.create_oval(
            x1 - 5,
            timelinePosY - 5,
            x1 + 5,
            timelinePosY + 5,
            fill="yellow",
        )
        self.create_oval(
            x2 - 5,
            timelinePosY - 5,
            x2 + 5,
            timelinePosY + 5,
            fill="red",
        )

    def redraw(
        self,
        date_range,
    ):
        self.delete("all")

        self.setVariableFromFile()
        self.setVariableFromParameter(date_range)

        self.reconfighWidthAndHeight()

        # TODO: expand size calculate

        self.row_idx = 0

        self.createImageButton()
        self.drawLabResults()
        self.drawDayRange()
        self.DrawMedicine()

        if self.showGrid:
            self.showGridLines()

    def showGridLines(self):
        # TODO: togle grid line button function

        grid_lines = []
        top = Var.graphCanvas_padding
        bottom = self.height - Var.graphCanvas_padding
        for i in range(len(self.date_range) + 1):
            x = self.day_x(i)
            line = self.create_line(
                x,
                top,
                x,
                bottom,
                fill="#ccc",
                dash=(2, 4),
            )
            grid_lines.append(line)

        left = self.day_x(0)
        right = self.day_x(len(self.date_range) - 1)
        # TODO: Weird
        self.row_idx = 1
        for j in range(self.total_rows - 1):

            line = self.create_line(
                left,
                self.row_y(),
                right,
                self.row_y(),
                fill="#ccc",
                dash=(2, 4),
            )
            self.row_idx += 1
            grid_lines.append(line)

        for line in grid_lines:
            self.tag_lower(line)
