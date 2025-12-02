import gamelogic
import userinterface
# Muistiinpanot
# - merkitse ykkösellä liikkuvia paloja
# - merkitse kakkosella paikallaan olevia paloja


def main():
    # Standard Tetris board: 20 rows x 10 columns
    rows = 20
    columns = 10
    field = gamelogic.Map(rows, columns)
    ui = userinterface.UI(cell_size=30)  # 30px per cell
    game = gamelogic.Gameloop(field, ui)
    game.start()


if __name__ == "__main__":
    main()


# window.mainloop()
