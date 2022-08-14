from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("Moje appka")
root.iconbitmap("images/favicon.ico")
root.maxsize(width=200, height=200)
root.minsize(width=200, height=200)
root.grid_rowconfigure(0, minsize=100)
root.grid_columnconfigure(0, minsize=100)

def full_size():
    global my_img_full
    full = Toplevel()
    my_img_full = ImageTk.PhotoImage(Image.open(path))
    my_img_full_label = Label(full, image=my_img_full)
    my_img_full_label.grid(row=0, column=0)

path = "images/cyberpunk.png"
my_img = ImageTk.PhotoImage(Image.open(path).resize((100,100)))
image_click = Button(root, image=my_img, command=full_size).grid(row=0, column=0)

button_quit = Button(root, text="EXIT", command=root.quit)
button_quit.grid(column=0, row=1)

root.mainloop()







