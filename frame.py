from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("Image viewer")
root.iconbitmap("images/favicon.ico")
root.maxsize(width=300, height=200)

#odsazení uvnitř rámečku
frame = LabelFrame(root, text="Frame", padx=5, pady=5)
#odsazení uvnitř rootu
frame.pack(padx=50, pady=10)

b = Button(frame, text="Dont click")
b2 = Button(frame, text="Dont click here")
#uvnitř framu je možné vytvořit grid
b.grid(row=0, column=0)
b2.grid(row=1, column=1)


root.mainloop()
