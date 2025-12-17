from logic.gameloop import Loop
from logic.game import Game
from logic.map import Map
import userinterface


def main():
    # Standard Tetris board: 20 rows x 10 columns
    rows = 20
    columns = 10
    field = Map(rows, columns)
    ui = userinterface.UI(cell_size=30)  # 30px per cell
    game =Game(field, ui)
    loop = Loop(game)
    loop.start()


if __name__ == "__main__":
    main()
