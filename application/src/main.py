import tkinter
import cowsay
import gamelogic
import userinterface 

field = gamelogic.Map(10, 20)
cowsay.tux("TkT Inter")
#root = tkinter.Tk()
#root.title("Tetris")
#root.geometry("500x500")
#root.mainloop()
window = tkinter.Tk()
window.title("TkInter example")
window.geometry("500x500")
userinterface = userinterface.UI(window)
userinterface.start()

window.mainloop()