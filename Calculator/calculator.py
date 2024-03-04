from tkinter import Tk, Entry, Button

class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculator")

        # Create Entry widget to display input and output
        self.entry = Entry(root, width=20, font=('Arial', 20), bd=5, justify='right')
        self.entry.grid(row=0, column=0, columnspan=4)

        # Create buttons for digits and operations
        buttons = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            'C', '0', '=', '+'
        ]

        row = 1
        col = 0
        for button in buttons:
            Button(root, text=button, width=5, height=2, font=('Arial', 15),
                   command=lambda b=button: self.click(b)).grid(row=row, column=col, padx=5, pady=5)
            col += 1
            if col > 3:
                col = 0
                row += 1

    def click(self, button):
        if button == '=':
            try:
                result = eval(self.entry.get())
                self.entry.delete(0, 'end')
                self.entry.insert('end', str(result))
            except:
                self.entry.delete(0, 'end')
                self.entry.insert('end', 'Error')
        elif button == 'C':
            self.entry.delete(0, 'end')
        else:
            self.entry.insert('end', button)

if __name__ == "__main__":
    root = Tk()
    calculator = Calculator(root)
    root.mainloop()
