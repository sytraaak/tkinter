from tkinter import *
from PIL import ImageTk, Image
#nutný import
from tkinter import messagebox


root = Tk()
root.title("Image viewer")
root.iconbitmap("images/favicon.ico")
root.minsize(width=300, height=300)

#typy pop up okne - "showinfo", "showwarning", "showerror", "askquestion", "askokcancel", "askyesno", "askyesnocancel", "askretrycancel"
#různé typy vrací různé popupu vrací různé informace
def popup():
    response = messagebox.askquestion(title="Upozornění", message="Něco jsi tam pojebal, chceš to zopakovat?")
    Label(root, text=response).pack()
    if response == 1:
        Label(root, text="Ano").pack()
    else:
        Label(root, text="Ne").pack()

Button(root, text="Popup", command=popup).pack()



mainloop()
