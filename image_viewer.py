from tkinter import *
from PIL import ImageTk, Image
import os

def image_name():
    global current_name
    current_name.grid_forget()
    current_name = Label(text=f"{image_names[index]}", bd=1, relief=SUNKEN)
    current_name.grid(row=1, column=0, sticky=W, columnspan=3)

def image_index(index):
    global status_label
    status_label.grid_forget()
    status_label = Label(root, text=f"Image {index + 1} of {len(image_names)}", bd=1, relief=SUNKEN)
    status_label.grid(row=1, column=0, sticky=E, columnspan=3)

def next_image():
    global index
    global image_label
    index += 1
    image_label.grid_forget()
    image_label = Label(image=image_list[index])
    image_label.grid(row=0, column=0, columnspan=3)
    if index == len(image_list) - 1:
        button_next = Button(root, text=">>", command=next_image, state=DISABLED)
    else:
        button_next = Button(root, text=">>", command=next_image)
    if index != 0:
        button_back = Button(root, text="<<", command=previous_image)
        button_back.grid(row=2, column=0, sticky=W)
    button_next.grid(row=2, column=2, sticky=E)
    image_name()
    image_index(index)

def previous_image():
    global index
    global image_label
    index -= 1
    image_label.grid_forget()
    image_label = Label(image=image_list[index])
    image_label.grid(row=0, column=0, columnspan=3)
    if index == 0:
        button_back = Button(root, text="<<", state=DISABLED)
    else:
        button_back = Button(root, text="<<", command=previous_image)
    if index != len(image_list) - 1:
        button_next = Button(root, text=">>", command=next_image)
        button_next.grid(row=2, column=2, sticky=E)
    button_back.grid(row=2, column=0, sticky=W)
    image_name()
    image_index(index)

def directory_check():
    global directory
    if "\\" in directory_entry.get():
        directory = str(directory_entry.get()).replace("\\", "/") + "/"
        first_window.destroy()
    else:
        directory_entry.delete(0, END)
        directory_entry.insert(0, "Chybně vložená cesta")

#první okno
first_window = Tk()
first_window.title("Image viewer")
first_window.iconbitmap("images/favicon.ico")
first_window.minsize(width=403, height=50)
first_window.maxsize(width=403, height=50)

#dotaz na cestu k souborů
directory_entry = Entry(first_window, width=50)
directory_entry.insert(0, "Vložte cestu k souborům")
directory_entry.pack()
directory = ""

button_continue = Button(first_window, text="Load images", command=directory_check)
button_continue.pack()

first_window.mainloop()

#prohlížeč
root = Tk()
root.title("Image viewer")
root.iconbitmap("images/favicon.ico")
root.minsize(width=403, height=450)
root.maxsize(width=403, height=450)

files = os.listdir(directory)
image_names = []
image_list = []
index = 0

for i, image in enumerate(files):
    if image[-3:].lower() in ["jpg", "png", "bmp"]:
        path = f"{directory}{image}"
        image_list.append(ImageTk.PhotoImage(Image.open(path).resize((400, 400))))
        image_names.append(image)

current_name = Label(text=f"{image_names[index]}")
status_label = Label(text=f"Image {index + 1} of {len(image_names)}", bd=1, relief=SUNKEN)
image_label = Label(image=image_list[index])
button_quit = Button(root, text="EXIT", command=root.quit)
button_next = Button(root, text=">>", command=next_image)
button_back = Button(root, text="<<", command=previous_image, state=DISABLED)

image_label.grid(row=0, column=0, columnspan=3)
button_next.grid(row=2, column=2, sticky=E)
button_quit.grid(row=2, column=1)
button_back.grid(row=2, column=0, sticky=W)
image_index(index)
image_name()


root.mainloop()