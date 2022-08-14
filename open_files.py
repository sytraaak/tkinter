from tkinter import *
from PIL import ImageTk, Image
from tkinter import filedialog

root = Tk()
root.title("Image viewer")
root.iconbitmap("images/favicon.ico")
root.minsize(width=300, height=300)

def open_file():
    # filetypes berou tuple - první je pojmenování a druhé je typ souboru - jako hlavní se bere první tuple, tedy zde nezobrazí all file
    # pokud by bylo potřeba otevřít pouze jeden, tuple musí být v listu [("png files, "*.png")] jinak nefunguje
    # vrací cestu k souboru
    global image_path
    global show_image
    global chosen_image
    show_image.pack_forget()
    image_path.pack_forget()

    root.filename = filedialog.askopenfilename(initialdir="/cyberpunk/", title="Select a file", filetypes=(("png files", "*.png"),("all files", "*.*")))
    image_path = Label(root, text=root.filename)
    image_path.pack()

    chosen_image = ImageTk.PhotoImage(Image.open(root.filename))
    show_image = Label(root, image=chosen_image)
    show_image.pack()

show_image = Label(root, text="Žádný zvolený obrázek")
show_image.pack()
image_path = Label(root, text="")
image_path.pack()
load_button = Button(root, text="Open file", command=open_file).pack()

mainloop()