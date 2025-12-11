import gamelogic
import userinterface


def main():
    # Standard Tetris board: 20 rows x 10 columns
    rows = 20
    columns = 10
    field = gamelogic.Map(rows, columns)
    ui = userinterface.UI(cell_size=30)  # 30px per cell
    game = gamelogic.Game(field, ui)
    gameplay = gamelogic.Loop(field, ui,game)
    gameplay.start()


if __name__ == "__main__":
    main()
