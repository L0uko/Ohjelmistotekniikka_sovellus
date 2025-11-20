import tkinter # pyright: ignore[reportMissingImports]
import cowsay # pyright: ignore[reportMissingImports]
import gamelogic # pyright: ignore[reportMissingImports]

field = gamelogic.Map(10,20)
cowsay.tux("TkT Inter")
root = tkinter.Tk()
root.title("Tetris")
root.geometry("500x500")
root.mainloop()
