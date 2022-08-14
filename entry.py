from tkinter import *

root = Tk()

def myClick():
    myLabel = Label(root, text=f"Ahoj, jmenuju se {e.get()}")
    myLabel.pack()

#entry widget funguje jako input, má další parametry
e = Entry(root, width=50, bg="black", fg="yellow", borderwidth=20)
e.pack()
e.insert(0, "Vložte Vaše jméno")

myButton1 = Button(root, text="Odešli", command=myClick, fg="yellow", bg="black")
myButton1.pack()

root.mainloop()
