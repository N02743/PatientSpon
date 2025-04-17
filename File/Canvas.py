import tkinter as tk
import File.Variable as Var

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

        self.redraw(
            date_range=date_range,
            lab_results=lab_results,
            medicine_usage=medicine_usage,
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

    def setVariableFromParameter(self, date_range, lab_results, medicine_usage):
        self.date_range = date_range
        self.lab_results = lab_results
        self.medicine_usage = medicine_usage

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
        for test, values in self.lab_results.items():
            y = self.row_y()
            self.create_text(
                5,
                y + 10,
                anchor="w",
                text=test,
                font=Var.graph_font,
            )
            for i, val in enumerate(values):
                if val is not None:
                    x = self.day_x(i)
                    self.create_text(
                        x,
                        y + 10,
                        text=str(val),
                        font=Var.graph_font,
                    )
            self.row_idx += 1

    def drawDayRange(self):
        y = self.row_y()
        self.create_text(
            5,
            y + 10,
            anchor="w",
            text="Day",
            font=Var.graph_font,
        )
        for i in range(len(self.date_range)):
            x = self.day_x(i)
            self.create_text(x, y + 10, text=str(i + 1))
        self.row_idx += 1

    def DrawMedicine(self):
        for med in self.medicine_usage:
            y = self.row_y()
            self.create_text(
                5,
                y + 10,
                anchor="w",
                text=med["name"],
                font=Var.graph_font,
            )

            start_idx = med["start"] - 1
            end_idx = med["end"] - 1
            x1 = self.day_x(start_idx)
            x2 = self.day_x(end_idx)
            timelinePositionY = y + 10

            self.drawTimeline(x1, x2, timelinePositionY)

            self.row_idx += 1

    def drawTimeline(self, x1, x2, timelinePosY):
        self.create_line(
            x1,
            timelinePosY,
            x2,
            timelinePosY,
            fill="blue",
            width=6,
        )
        self.create_oval(
            x1 - 5,
            timelinePosY - 5,
            x1 + 5,
            timelinePosY + 5,
            fill="green",
        )
        self.create_oval(
            x2 - 5,
            timelinePosY - 5,
            x2 + 5,
            timelinePosY + 5,
            fill="red",
        )

    def redraw(self, date_range, lab_results, medicine_usage):
        self.delete("all")

        self.setVariableFromFile()
        self.setVariableFromParameter(date_range, lab_results, medicine_usage)

        self.reconfighWidthAndHeight()

        # TODO: expand size calculate

        self.row_idx = 0

        self.createImageButton()
        self.drawLabResults()
        self.drawDayRange()
        self.DrawMedicine()
