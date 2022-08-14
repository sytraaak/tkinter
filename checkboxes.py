from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("Checkboxes")
root.iconbitmap("images/favicon.ico")
root.geometry("400x400")

def show(var):
    global on_label
    global my_label

    on_label.forget()
    my_label.forget()

    on_label = Label(root, text="Je to zapnutý")
    my_label = Label(root, text=var.get())

    if var.get() == 1 and var == checkbox1:
        on_label.pack()
    my_label.pack()


checkbox1 = StringVar()
checkbox2 = IntVar()

var = IntVar()
c1 = Checkbutton(root, text="Check this box", variable=checkbox1, command=lambda: show(checkbox1), onvalue="On", offvalue="Off")
c2 = Checkbutton(root, text="Check this box 1", variable=checkbox2, command=lambda: show(checkbox2), onvalue="10", offvalue="20")

c1.pack(anchor=W)
c2.pack(anchor=W)
c1.deselect()
c2.deselect()
on_label = Label()
my_label = Label()

mainloop()
