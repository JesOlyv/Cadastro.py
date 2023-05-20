import tkinter as tk

class Calculadora:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Calculadora")

        self.entry = tk.Entry(self.window)
        self.entry.grid(row=0, column=0, columnspan=4)

        self.create_buttons()

        self.window.mainloop()

    def create_buttons(self):
        buttons = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            '0', '.', '=', '+'
        ]

        row = 1
        col = 0

        for button in buttons:
            tk.Button(self.window, text=button, width=5, command=lambda value=button: self.button_click(value)).grid(row=row, column=col)
            col += 1
            if col > 3:
                col = 0
                row += 1

    def button_click(self, value):
        if value == '=':
            result = eval(self.entry.get())
            self.entry.delete(0, tk.END)
            self.entry.insert(tk.END, str(result))
        else:
            self.entry.insert(tk.END, value)

Calculadora()
