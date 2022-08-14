from tkinter import *


root = Tk()

def myClick():
    myLabel = Label(root, text="Kliknul jsem na tlačítko")
    myLabel.grid(row=2, column=0)

#takto vzniká tlačítko, je možné jej nastavit na vypnuto = state
myButton = Button(root, text="Neklikneš na mě", state=DISABLED, padx=80, pady=80)
myButton.grid(row=0, column=0)

#bez state je možné na něj kliknout, padx říká jak velké má být tlačítko v ose X a pady v ose Y, do command se vkládá funkce, která se má spustit
#fg = foreground color, bg = background color, je možné použít hex colors #00000
myButton1 = Button(root, text="Klikneš na mě a mám rozměry jiný", padx=50, pady=80, command=myClick, fg="blue", bg="yellow")
myButton1.grid(row=1, column=0)

root.mainloop()
