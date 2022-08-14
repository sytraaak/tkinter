from tkinter import *
from PIL import ImageTk, Image

def open():
    global image
    top = Toplevel()
    top.title("Horní vokno")
    top.minsize(width=300, height=300)
    image = ImageTk.PhotoImage(Image.open("images/cyberpunk.png"))
    Label(top, image=image).pack()


root = Tk()
root.title("Image viewer")
root.iconbitmap("images/favicon.ico")
root.minsize(width=300, height=300)

btn = Button(root, text="Open window", command=open).pack()






mainloop()
