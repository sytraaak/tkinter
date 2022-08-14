from tkinter import *

root = Tk()
root.title("Kalkulačka")

class Calculator():
    def __init__(self):
        self.numbers = ""

    def button_add(self):
        f_number = int(e.get())
        self.numbers += f"{f_number} + "
        e.delete(0, END)

    def button_equal(self):
        number = str(e.get())
        e.delete(0, END)
        self.numbers += number
        print(self.numbers)
        result = eval(self.numbers)
        e.insert(0, result)
        self.numbers = str(result)

    def button_click(self, number):
        current = e.get()
        e.delete(0, END)
        e.insert(0, str(current) + str(number))

    def button_clear(self):
        self.numbers = []
        e.delete(0, END)

    def button_subtrack(self):
        f_number = int(e.get())
        self.numbers += f"{f_number} - "
        e.delete(0, END)

    def button_divide(self):
        f_number = int(e.get())
        self.numbers += f"{f_number} / "
        e.delete(0, END)

    def button_multiply(self):
        f_number = int(e.get())
        self.numbers += f"{f_number} * "
        e.delete(0, END)




e = Entry(root, width=23, bg="black", fg="lime", borderwidth=5)
e.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

calc = Calculator()

#definování tlačítek

button_1 = Button(root, text="1", padx=20, pady=10, command=lambda: calc.button_click(1))
button_2 = Button(root, text="2", padx=20, pady=10, command=lambda: calc.button_click(2))
button_3 = Button(root, text="3", padx=20, pady=10, command=lambda: calc.button_click(3))
button_4 = Button(root, text="4", padx=20, pady=10, command=lambda: calc.button_click(4))
button_5 = Button(root, text="5", padx=20, pady=10, command=lambda: calc.button_click(5))
button_6 = Button(root, text="6", padx=20, pady=10, command=lambda: calc.button_click(6))
button_7 = Button(root, text="7", padx=20, pady=10, command=lambda: calc.button_click(7))
button_8 = Button(root, text="8", padx=20, pady=10, command=lambda: calc.button_click(8))
button_9 = Button(root, text="9", padx=20, pady=10, command=lambda: calc.button_click(9))
button_0 = Button(root, text="0", padx=20, pady=10, command=lambda: calc.button_click(0))
button_add = Button(root, text="+", padx=19, pady=10, command=calc.button_add)
button_sub = Button(root, text="-", padx=21, pady=10, command=calc.button_subtrack)
button_divide = Button(root, text="/", padx=20, pady=10, command=calc.button_divide)
button_multiply = Button(root, text="*", padx=21, pady=10, command=calc.button_multiply)
button_equal = Button(root, text="=", padx=47, pady=10, command=calc.button_equal)
button_clear = Button(root, text="Clear", padx=38, pady=10, command=calc.button_clear)

# vložení tlačítek na obrazovku

button_sub.grid(row=6, column=0)
button_divide.grid(row=6, column=1)
button_multiply.grid(row=6, column=2)

button_1.grid(row=3, column=0)
button_2.grid(row=3, column=1)
button_3.grid(row=3, column=2)

button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)

button_7.grid(row=1, column=0)
button_8.grid(row=1, column=1)
button_9.grid(row=1, column=2)

button_0.grid(row=4, column=0)
button_add.grid(row=5, column=0)
button_equal.grid(row=5, column=1, columnspan=2)
button_clear.grid(row=4, column=1, columnspan=2)

root.mainloop()