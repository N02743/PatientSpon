canvas = None


def CanvasRedrawSetting(redrawFunc):
    global redrawFunction
    redrawFunction = redrawFunc


def CanvasRedraw():

    redrawFunction()
