from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("Image viewer")
root.iconbitmap("images/favicon.ico")
root.minsize(width=300, height=300)

# def show_message(r):
#     #pokud chci dostat hodnotu, dává var.get()
#     message = Label(text=f"Hello {r.get()}")
#     message.grid_forget()
#     message.grid(row=2, column=0)


# tkinter používá proměnné IntVAr a StringVar
# r = IntVar()
# nastavení defaultní volby na 1
# r.set(1)

#vytvoření tlačítek z listu tuplů = první hodnota v tuplu je "text" a druhá je "variable" z radiobutton class
MODES = [
    ("Papričky", "Papričky"),
    ("Sýr", "Sýr"),
    ("Houby", "Houby"),
    ("Cibule", "Cibule"),
]

pizza = StringVar()
pizza.set("Papričky")

for text, mode in MODES:
    Radiobutton(root, text=text,  variable=pizza, value=mode).pack(anchor=W)

#nastavení radiobuttonu
# Radiobutton(root, text="První možnost", variable=r, value=1, command=lambda: show_message(r)).grid(row=0, column=0)
# Radiobutton(root, text="Druhá možnost", variable=r, value=2, command=lambda: show_message(r)).grid(row=1, column=0)
# show_message(r)



root.mainloop()