from tkinter import *

#všechno jsou widgety a potřebujeme window widget nazvaný root
root = Tk()
#label widget - label widgety se dávají do window widgetů
myLabel = Label(root, text="Hello world!")
# zobrazujeme na obrazovku
myLabel.pack()
#každý běžící program je běžící smyčka, takto se vytváří smyčka
root.mainloop()