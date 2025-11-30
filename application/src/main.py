import tkinter
import gamelogic
import userinterface

#Muistiinpanot
# - merkitse ykkösellä liikkuvia paloja
# - merkitse kakkosella paikallaan olevia paloja
# 


field = gamelogic.Map(10, 20)
field.new_block(0, 0, field.return_block_list()[0])
print("new block",field.return_map_str())
window = tkinter.Tk()
window.title("TkInter example")
window.geometry("500x500")

userinterface = userinterface.UI(window, field)
userinterface.start()

window.mainloop()
