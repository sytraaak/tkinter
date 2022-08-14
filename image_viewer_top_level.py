from tkinter import *
from PIL import ImageTk, Image
from tkinter import filedialog
import os

running = False
print(running)

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

def full_size(list_of_images, image_index):
    global my_img_full
    full = Toplevel()
    my_img_full_label = Label(full, image=list_of_images[image_index])
    my_img_full_label.grid(row=0, column=0)

def next_image():
    global index
    global image_label_button
    index += 1
    image_label_button.grid_forget()
    image_label_button = Button(root, image=image_list[index], borderwidth=0, command=lambda: full_size(image_list_full,
                                                                                                        index))
    image_label_button.grid(row=0, column=0, columnspan=3)
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
    global image_label_button
    index -= 1
    image_label_button.grid_forget()
    image_label_button = Button(root, image=image_list[index], borderwidth=0, command=lambda: full_size(image_list_full,
                                                                                                        index))
    image_label_button.grid(row=0, column=0, columnspan=3)
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

def browser():
    global status_label
    global current_name
    global image_label_button
    global root
    global image_names
    global image_list
    global image_list_full
    global index
    global running
    running = True
    print(running)
    # prohlížeč
    root = Tk()
    root.title("Image viewer")
    root.iconbitmap("images/favicon.ico")
    root.minsize(width=403, height=500)
    root.maxsize(width=403, height=500)

    files = os.listdir(directory)
    image_names = []
    image_list = []
    image_list_full = []
    index = 0

    for i, image in enumerate(files):
        if image[-3:].lower() in ["jpg", "png", "bmp"]:
            path = f"{directory}{image}"
            image_list.append(ImageTk.PhotoImage(Image.open(path).resize((400, 400))))
            image_list_full.append(ImageTk.PhotoImage(Image.open(path)))
            image_names.append(image)

    current_name = Label(text=f"{image_names[index]}")
    status_label = Label(text=f"Image {index + 1} of {len(image_names)}", bd=1, relief=SUNKEN)
    image_label_button = Button(root, image=image_list[index], borderwidth=0,
                                command=lambda: full_size(image_list_full, index))
    button_quit = Button(root, text="EXIT", command=root.quit)
    button_next = Button(root, text=">>", command=next_image)
    button_back = Button(root, text="<<", command=previous_image, state=DISABLED)
    button_open = Button(root, text="Open different folder", command=open_directory)

    image_label_button.grid(row=0, column=0, columnspan=3)
    button_next.grid(row=2, column=2, sticky=E)
    button_quit.grid(row=2, column=1)
    button_back.grid(row=2, column=0, sticky=W)
    button_open.grid(row=3, column=0, columnspan=3, pady=10)
    image_index(index)
    image_name()

    root.mainloop()

def open_directory():
    global running
    global directory_entry
    global first_window
    if running:
        print("Mělo by se vypnout")
        root.destroy()
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
    browser()

open_directory()


