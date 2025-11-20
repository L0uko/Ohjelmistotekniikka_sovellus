import tkinter  # pyright: ignore[reportMissingImports]
import cowsay # pyright: ignore[reportMissingImports]
import gamelogic as gamelogic

field = gamelogic.Map(10,20)
cowsay.tux("TkT Inter")
root = tkinter.Tk()
root.geometry("500x500")