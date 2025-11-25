import tkinter


class UI:
    def __init__(self, root, field):
        self._root = root
        self._field = field
        # self._root.geometry
        self._gamestate = tkinter.Variable()
        self._gamestate.set(self._field.return_map_str())

    def start(self):
        label = tkinter.Label(
            master=self._root, text="Tämä on Tetris", font=("Monocraft", 10))
        label.pack(padx=10, pady=10)
        tetrisbox = tkinter.Label(
            master=self._root, textvariable=self._gamestate)
        tetrisbox.pack(padx=10, pady=10)
