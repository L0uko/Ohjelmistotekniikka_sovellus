import tk as tk # pyright: ignore[reportMissingImports]
import cowsay # pyright: ignore[reportMissingImports]
import gamelogic as gamelogic

field = gamelogic.Map(10,20)
cowsay.tux("TkT Inter")
root = tk()
frm = tk.ttk.Frame(root, padding=10)
frm.grid()
tk.ttk.Label(frm, text="Hello World!").grid(column=0, row=0)
tk.ttk.Button(frm, text="Quit", command=root.destroy).grid(column=1, row=0)
root.mainloop()
