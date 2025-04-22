import tkinter as tk
import Var.Variable as Var

import Var.Font as Font
import File.Class as Class

from tkinter import messagebox

import Data.getData as get
import Var.Global as Global


def showImageModal(i):
    # TODO: show Image modal
    pictureDirectory = "Data/Image"
    messagebox.showinfo(
        "Image",
        f"Show image for {i}",
    )


class CanvasGraph(tk.Canvas):
    def __init__(
        self,
        parent,
        patient_data: Class.Patient,
    ):
        super().__init__(parent, bg="white")
        self.pack()

        self.patient_data = patient_data

        # TODO: auto set date
        self.startDate = "01/03/2025"
        self.endDate = "18/03/2025"

        self.redraw()

    # return x position at center for row = 0 at day = index
    def day_x(self, index):
        return self.label_width + index * self.day_width + self.day_width // 2

    # return y position for element in graph at row = row_idx
    def row_y(self, index):
        return self.canvas_padding + index * self.row_height

    def setVariableFromFile(self):
        self.label_width = Var.graphLabel_width
        self.day_width = Var.graphDay_width
        self.row_height = Var.graphRow_height
        self.canvas_padding = Var.padding

    def setVariableFromParameter(self):
        self.date_range = get.get_dateRange_data(
            start=self.startDate,
            end=self.endDate,
        )

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

        lab_test_rows = len(self.lab_results) + 1 if Global.showLabTest else 0
        medicine_usage_rows = len(self.medicine_usage) + 1 if Global.showMedUsage else 0

        self.total_rows = 1 + lab_test_rows + 1 + medicine_usage_rows

    def reconfig_WidthAndHeight(self):
        self.recalculate_WidthAndHeight()
        self.config(
            width=self.width,
            height=self.height,
        )

    def recalculate_WidthAndHeight(self):
        self.width = (
            self.label_width
            + (len(self.date_range) * self.day_width)
            + (self.canvas_padding * 2)
        )

        self.height = (self.total_rows * self.row_height) + (self.canvas_padding * 2)

    def createImageButton(self):
        iterDate = self.startDate
        for i in range(len(self.date_range)):
            x = self.day_x(i)
            y = self.row_y(self.row_idx)
            btn = tk.Button(
                self,
                text="📷",
                command=lambda d=iterDate: showImageModal(d),
                width=2,
            )
            self.create_window(x, y + 25, window=btn)
            iterDate = get.nextDay(iterDate)
        self.row_idx += 1

    def drawLabResults(self):
        labResults = self.lab_results

        y = self.row_y(self.row_idx) + 10
        self.create_text(
            5,
            y,
            anchor="w",
            text="Lab Test",
            font=Font.graphLabel,
        )
        self.row_idx += 1

        for labTest in labResults.keys():
            y = self.row_y(self.row_idx) + 10
            self.create_text(
                5,
                y,
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
                        y,
                        text=str(result),
                        font=Font.graph,
                    )
            self.row_idx += 1

    def drawDayRange(self):
        for i in range(len(self.date_range)):
            y = self.row_y(self.row_idx) + 10
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
            5,
            y,
            self.day_x(len(self.date_range) - 1) + Var.arrowGraph_padding,
            y,
            fill="black",
            width=6,
            arrow=tk.BOTH,
            arrowshape=(10, 12, 6),
        )
        self.row_idx += 1

    def DrawMedicine(self):
        y = self.row_y(self.row_idx) + 10
        self.create_text(
            5,
            y,
            anchor="w",
            text="Medicine Usage",
            font=Font.graphLabel,
        )
        self.row_idx += 1

        for medicine in self.medicine_usage.keys():
            y = self.row_y(self.row_idx) + 10
            self.create_text(
                5,
                y,
                anchor="w",
                text=medicine,
                font=Font.graph,
            )

            med = self.medicine_usage[medicine]
            timelinePositionY = y

            if get.findDays(self.endDate, med["start"]) > 0:
                pos = self.day_x(get.findDays(self.startDate, self.endDate))
                self.create_line(
                    pos,
                    timelinePositionY,
                    pos + Var.arrowGraph_padding,
                    timelinePositionY,
                    fill="black",
                    width=6,
                    arrow=tk.BOTH,
                )
                self.row_idx += 1
                continue

            if get.findDays(med["end"], self.startDate) > 0:
                pos = self.day_x(0)
                self.create_line(
                    pos - Var.arrowGraph_padding,
                    timelinePositionY,
                    pos,
                    timelinePositionY,
                    fill="black",
                    width=6,
                    arrow=tk.BOTH,
                )
                self.row_idx += 1
                continue

            start_idx = get.findDays(self.startDate, med["start"])
            end_idx = get.findDays(self.startDate, med["end"])

            start_diff = get.findDays(self.startDate, med["start"])
            end_diff = get.findDays(med["end"], self.endDate)

            # out of bound
            if start_diff < 0:
                x1 = -1
            else:
                x1 = self.day_x(start_idx)

            # out of bound
            if end_diff < 0:
                x2 = -1
            else:
                x2 = self.day_x(end_idx)

            self.drawTimeline(x1, x2, timelinePositionY)

            self.row_idx += 1

    def drawTimeline(self, x1, x2, timelinePosY):

        if x1 == -1:
            arrowStart = True
            x1 = self.day_x(0) - Var.arrowGraph_padding
        else:
            arrowStart = False

        if x2 == -1:
            arrowEnd = True
            x2 = (
                self.day_x(get.findDays(self.startDate, self.endDate))
                + Var.arrowGraph_padding
            )
        else:
            arrowEnd = False

        if arrowStart and arrowEnd:
            arrow = tk.BOTH
        elif arrowStart:
            arrow = tk.FIRST
        elif arrowEnd:
            arrow = tk.LAST
        else:
            arrow = tk.NONE

        self.create_line(
            x1,
            timelinePosY,
            x2,
            timelinePosY,
            fill="black",
            width=6,
            arrow=arrow,
        )

        if not arrowStart:
            self.create_oval(
                x1 - 5,
                timelinePosY - 5,
                x1 + 5,
                timelinePosY + 5,
                fill="yellow",
            )

        if not arrowEnd:
            self.create_oval(
                x2 - 5,
                timelinePosY - 5,
                x2 + 5,
                timelinePosY + 5,
                fill="red",
            )

    def redraw(self):
        self.delete("all")

        self.setVariableFromFile()
        self.setVariableFromParameter()

        self.reconfig_WidthAndHeight()

        # TODO: Make Canvas expand -> expand size calculate
        # self.height = (self.total_rows * self.row_height) + (self.canvas_padding * 2)

        self.row_idx = 0

        self.createImageButton()

        if Global.showLabTest:
            self.drawLabResults()

        self.drawDayRange()

        if Global.showMedUsage:
            self.DrawMedicine()

        if Global.showGrid:
            self.showGridLines()

    def showGridLines(self):
        grid_lines = []
        top = Var.padding
        bottom = self.height - Var.padding
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

        left = self.day_x(0) - 20
        right = self.day_x(len(self.date_range) - 1) + 20

        dayRange_idx = len(self.lab_results) + 2
        dontShowGridIndex = [0, 1, dayRange_idx, dayRange_idx + 1]

        for j in range(self.total_rows):
            if j not in dontShowGridIndex:
                pos_y = self.row_y(j) + 10
                line = self.create_line(
                    left,
                    pos_y,
                    right,
                    pos_y,
                    fill="#ccc",
                    dash=(2, 4),
                )
                grid_lines.append(line)

        for line in grid_lines:
            self.tag_lower(line)
