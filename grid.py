from tkinter import *

#všechno jsou widgety a potřebujeme window widget nazvaný root
root = Tk()
#label widget - label widgety se dávají do window widgetů
myLabel1 = Label(root, text="Hello world!")
myLabel2 = Label(root, text="My name is Jan Burda")
myLabel3 = Label(root, text="                 ")
# umístění na obrazovku - grid je umístění namísto pack, pozice jsou relativní vůči ostatním
# pokud jsou řádky či sloupce prázdné, tak jsou z hlediska zobrazení ignorovány
myLabel1.grid(row=0, column=0)
myLabel2.grid(row=1, column=6)
myLabel3.grid(row=1, column=1)
#každý běžící program je běžící smyčka, takto se vytváří smyčka
root.mainloop()
#grid je prostě mřížka se sloupci a řádky