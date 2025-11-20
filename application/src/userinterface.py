import tkinter
import gamelogic

class UI:
    def __init__(self, root):
        self._root = root

    def start(self):
        label = tkinter.Label(master=self._root, text="Tämä on Tetris", font=("Monocraft",10))

        label.grid()
        textbox = tkinter.Label(master=self._root, text="placeholder")
        textbox.grid()

