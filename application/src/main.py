import tkinter
# import cowsay
import gamelogic
import userinterface

field = gamelogic.Map(10, 20)
field.new_block(0, 4)
print("new block",field.return_map_str())
# cowsay.tux("TkT Inter")
window = tkinter.Tk()
window.title("TkInter example")
window.geometry("500x500")

userinterface = userinterface.UI(window, field)
userinterface.start()

window.mainloop()
