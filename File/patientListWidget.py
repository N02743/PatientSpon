import tkinter as tk
from tkinter import messagebox

from File import Widget, Frame
from File import GlobalFunction as GLBFunc

from Var import Font, Var, Global
from Var.Color import Color

from Data import getData as get


def addNewPatient():
    # TODO:
    messagebox.showinfo(
        "Add new Patient",
        "text field for add new Patient",
    )
    print("Config Time Tick")


def resetButtonFunction():
    # TODO:

    print("Reset Button")


def confirmButtonFunction():
    # TODO:
    GLBFunc.reloadFunction()

    print("Confirm Button")


def update_listbox(*args):
    GLBFunc.PatientListReload()
    print("update\n")


class NavFrame(Frame.NavFrame):
    def __init__(
        self,
        parent,
        onClosing,
    ):
        super().__init__(parent)

        button = tk.Button(
            self,
            text="X",
            font=Font.backButtom,
            fg=Color.backButtomFontBG,
            background=Color.backButtomBG,
            width=Var.backButtomWidth,
            command=lambda: onClosing(),
        )
        # button.pack(
        #     side="left",
        #     fill=tk.Y,
        # )
        button.grid(
            row=0,
            column=0,
            sticky="nsew",
            padx=Var.miniPadding,
            pady=Var.miniPadding,
        )

        banner = Frame.BannerFrame(self)
        filter = FiltersFrame(self)

        self.grid_rowconfigure(0, weight=1)

        for i, w in enumerate(Var.navFrameWeight):
            self.grid_columnconfigure(
                i,
                weight=w,
                uniform="navGroup",
            )


# TODO: Remove duplicate PatientFrame
class FiltersFrame(tk.Frame):
    def __init__(self, parent):
        super().__init__(
            parent,
        )
        # self.pack(
        #     fill=tk.BOTH,
        #     expand=True,
        # )
        self.grid(
            row=0,
            column=2,
            sticky="nsew",
            padx=Var.miniPadding,
            pady=Var.miniPadding,
        )

        weightList = [15, 15, 1, 1, 15]

        pageInfo = tk.Frame(
            self,
            bg=Color.patientPageBG,
        )
        Frame.PageInfoFrame(pageInfo, text="Patient Info Page")
        pageInfo.pack(
            fill=tk.BOTH,
            expand=True,
        )

        frame = []
        frame.append(
            tk.Frame(
                self,
                bg=Color.patientInfoFirstRowBG,
            )
        )
        frame.append(
            tk.Frame(
                self,
                bg=Color.patientInfoSecondRowBG,
            )
        )
        frame[0].pack(
            fill=tk.BOTH,
            expand=True,
        )
        frame[1].pack(
            fill=tk.BOTH,
            expand=True,
        )

        labelList = Global.LabelList[:6]
        del labelList[4]  # remove sex label

        tf = []

        for i, label in enumerate(labelList):
            row = 0 if i < 2 else 1
            column = i if i < 2 else i - 2

            tf.append(
                Widget.Textfield(
                    frame[row],
                    label=label,
                    info=None,
                    row=0,
                    column=column,
                )
            )
            tf[i].onEnabled()
            tf[i].entryVar.trace_add("write", update_listbox)
            # tf[i].entry.trace_add('write', update_listbox)

        for i in range(len(weightList)):
            row = 0 if i < 2 else 1
            column = i if i < 2 else i - 2

            frame[row].grid_columnconfigure(
                column,
                weight=weightList[i],
            )

        pageInfo.grid_columnconfigure(0, weight=1)
        pageInfo.grid_rowconfigure(0, weight=1)

        frame[0].grid_rowconfigure(0, weight=1)
        frame[1].grid_rowconfigure(0, weight=1)


class ContentFrame(tk.Frame):
    def __init__(
        self,
        parent,
        graph_page,
    ):
        super().__init__(parent)
        # self.pack(
        #     fill=tk.BOTH,
        #     expand=True,
        #     padx=50,
        #     pady=30,
        # )
        self.grid(
            row=1,
            column=0,
            sticky="nsew",
            padx=Var.miniPadding,
            pady=Var.miniPadding,
        )

        header = HeaderFrame(self)
        self.patientList = ListFrame(self, graph_page)

        buttom = ButtomFrame(self)

        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=10)
        self.grid_rowconfigure(2, weight=1)

        self.grid_columnconfigure(0, weight=1)

    def unbindScroll(self):
        self.patientList.unbindScroll()


class HeaderFrame(tk.Frame):
    def __init__(
        self,
        parent,
    ):
        super().__init__(
            parent,
            background=Color.patientHeaderFrameBG,
        )
        self.grid(
            row=0,
            column=0,
            sticky="nsew",
            padx=Var.miniPadding,
            pady=Var.miniPadding,
        )

        weight = Var.patientListWeight

        labelList = Global.LabelList[:6]
        del labelList[4]

        for column, label in enumerate(labelList):
            cell = tk.Label(
                self,
                text=label,
                background=Color.patientHeaderBG,
            )
            cell.grid(
                row=0,
                column=column,
                sticky="nsew",
                padx=Var.miniPadding,
                pady=Var.miniPadding,
            )

        for column in range(5):
            self.grid_columnconfigure(
                column,
                weight=weight[column],
                uniform="group1",
            )

        self.grid_rowconfigure(0, weight=1)


class ListFrame(tk.Frame):
    def __init__(
        self,
        parent,
        graph_page=None,
    ):
        super().__init__(
            parent,
            borderwidth=Var.patientListBorderWidth,
            relief=Var.patientListBorderType,
        )
        self.grid(
            row=1,
            column=0,
            sticky="nsew",
            padx=Var.miniPadding,
            pady=Var.miniPadding,
        )

        self.canvas = tk.Canvas(self)
        self.canvas.pack(
            side=tk.LEFT,
            fill=tk.BOTH,
            expand=True,
        )

        # TODO: scrollbar cannot scroll until the last item hit buttom and first item hit top
        scrollbar = tk.Scrollbar(
            self,
            orient="vertical",
            command=self.canvas.yview,
        )
        scrollbar.pack(
            side=tk.RIGHT,
            fill=tk.Y,
        )

        self.canvas.configure(yscrollcommand=scrollbar.set)

        self.inner_frame = tk.Frame(
            self.canvas,
            bg=Color.patientListInnerFrameBG,
        )
        window_id = self.canvas.create_window(
            (0, 0),
            window=self.inner_frame,
            anchor="nw",
        )

        self.inner_frame.grid_columnconfigure(0, weight=1)

        def resize_inner(event):
            self.canvas.itemconfig(window_id, width=event.width)

        self.canvas.bind("<Configure>", resize_inner)

        def _on_mousewheel(event):
            self.canvas.yview_scroll(int(-1 * (event.delta / 120)), "units")

        def on_frame_configure(event):
            self.canvas.update_idletasks()

            bbox = self.canvas.bbox("all")
            if bbox:
                self.canvas.configure(scrollregion=bbox)

                needs_scroll = bbox[3] > self.canvas.winfo_height()
                if needs_scroll:
                    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
                    self.canvas.bind_all("<MouseWheel>", _on_mousewheel)
                else:
                    scrollbar.pack_forget()
                    self.canvas.unbind_all("<MouseWheel>")

        self.inner_frame.bind("<Configure>", on_frame_configure)

        self.patientListData = get.get_patient_list()

        Global.patientAllAmount = len(self.patientListData)
        Global.patientFilterAmount = Global.patientAllAmount

        self.graph_page = graph_page

        self.patientRowList = []
        self.renderRow()
        GLBFunc.PatientListReloadSetting(self.renderRow)

    def renderRow(self):
        for row in self.patientRowList:
            row.destroy()

        self.patientRowList = []

        patientListData = self.patientListData.copy()

        for label, var in Global.filterVarDict.items():
            value = var.get().strip().lower()
            if value:
                patientListData = patientListData[
                    patientListData[label].astype(str).str.lower().str.contains(value)
                ]
                if label in patientListData.columns:
                    patientListData = patientListData[
                        patientListData[label]
                        .astype(str)
                        .str.lower()
                        .str.contains(value)
                    ]
        Global.patientFilterAmount = len(patientListData)

        for row, patient in enumerate(patientListData.itertuples()):
            # TODO:
            self.patientRowList.append(
                Frame.PatientRowFrame(
                    # self,
                    self.inner_frame,
                    patient=patient,
                    row=row,
                )
            )
            self.patientRowList[row].bind(
                "<Button-1>",
                lambda event, HN=patient.HN: self.graph_page(HN),
            )
            self.patientRowList[row].bind(
                "<Enter>",
                lambda event, ptR=self.patientRowList[row]: ptR.config(
                    bg=Color.patientRowOnHover
                ),
            )
            self.patientRowList[row].bind(
                "<Leave>",
                lambda event, ptR=self.patientRowList[row]: ptR.config(
                    bg=Color.patientRowFrameBG
                ),
            )

            self.grid_rowconfigure(row, weight=1)

        self.grid_columnconfigure(0, weight=1)

    def unbindScroll(self):
        self.canvas.unbind_all("<MouseWheel>")


class ButtomFrame(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.grid(
            row=2,
            column=0,
            sticky="nsew",
            padx=Var.miniPadding,
            pady=Var.miniPadding,
        )

        self.label = tk.Label(
            self,
            text=f"Founded {Global.patientFilterAmount} of {Global.patientAllAmount}",
        )
        self.label.pack(side="left")

        GLBFunc.PatientFilterFoundLabelSetting(self.onFilter)

        tk.Button(
            self,
            text="Add new Patient",
            command=lambda: addNewPatient(),
        ).pack(side="right")

    def onFilter(self):
        self.label.config(
            text=f"Founded {Global.patientFilterAmount} of {Global.patientAllAmount}"
        )


class GraphConfigFrame(tk.Frame):
    def __init__(self, parent):
        super().__init__(
            parent,
            padx=Var.padding,
            pady=Var.padding,
            bg=Color.configFrameBG,
        )
        self.pack(side="top", fill="x")

        # buttonFrame = ConfigButtonFrame(self)
        confirmFrame = ConfirmFrame(self)


# class ConfigButtonFrame(tk.Frame):
#     def __init__(self, parent):
#         super().__init__(
#             parent,
#             background=Color.configFrameBG,
#         )
#         self.pack(side="left")

#         global showLabButton
#         showLabButton = Widget.ToggleButton(
#             self,
#             text="Show Lab test",
#             var=Global.showLabTest,
#         )

#         global showMedButton
#         showMedButton = Widget.ToggleButton(
#             self,
#             text="Show Medication",
#             var=Global.showMedUsage,
#         )

#         global showGridButton
#         showGridButton = Widget.ToggleButton(
#             self,
#             text="Show grid",
#             var=Global.showGrid,
#         )


class ConfirmFrame(tk.Frame):
    def __init__(self, parent):
        super().__init__(
            parent,
            background=Color.configFrameBG,
        )
        self.pack(side="right")

        resetButton = Widget.ResetButton(
            self,
            command=lambda: resetButtonFunction(),
        )
        confirmButton = Widget.ConfirmButton(
            self,
            command=lambda: confirmButtonFunction(),
        )
