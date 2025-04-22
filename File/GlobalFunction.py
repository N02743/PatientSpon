canvas = None


def CanvasRedrawSet(redrawFunc):
    global redrawFunction
    redrawFunction = redrawFunc


def CanvasRedraw():

    redrawFunction()
