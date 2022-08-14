from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("Image viewer")
root.iconbitmap("images/favicon.ico")
root.geometry("400x400")

def show(i):
    my_label = Label(root, text=globals()[f"variable{i}"].get()).pack()

for i in range(10):
    globals()[f"variable{i}"] = IntVar()
    c = Checkbutton(root, text=globals()[f"variable{i}"], variable=globals()[f"variable{i}"], command=lambda: show(i))
    c.pack()



mainloop()