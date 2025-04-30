canvas = None


def CanvasRedrawSetting(redrawFunc):
    global redrawFunction
    redrawFunction = redrawFunc


def CanvasRedraw():
    redrawFunction()


def PatientListReloadSetting(reloadFunc):
    global reloadFunction
    reloadFunction = reloadFunc


def PatientListReload():
    reloadFunction()
