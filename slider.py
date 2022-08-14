from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("Image viewer")
root.iconbitmap("images/favicon.ico")
root.geometry("200x200")

def update_number(var):
    my_label = Label(root, text=horinzotal.get()).pack()
    root.geometry(f"{horinzotal.get()}x400")

#posuvník = Scale widget - defaultní je vertikální, from_ a to, vrací číslo
vertical = Scale(root, from_=0, to=200)
#musí být packnut na samostatném řádku
vertical.pack()

horinzotal = Scale(root, from_=0, to=200, orient=HORIZONTAL, command=update_number, height=400)
horinzotal.pack(anchor=W)

my_button = Button(root, text="Update", command=update_number).pack()






mainloop()
