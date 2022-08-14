from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("Moje appka")
root.iconbitmap("images/favicon.ico")
root.maxsize(width=400, height=800)
root.minsize(width=400, height=800)
root.grid_rowconfigure(0, minsize=100)
root.grid_columnconfigure(0, minsize=100)

my_img = ImageTk.PhotoImage(Image.open("images/cyberpunk.png").resize((100,100)))
image_label = Label(image=my_img)
image_label.grid(row=0, column=0)


button_quit = Button(root, text="EXIT", command=root.quit)
button_quit.grid(column=0, row=1)

root.mainloop()







