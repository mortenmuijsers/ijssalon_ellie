from tkinter import Tk, Entry, Button, Grid, N, S, E, W
import math

class ScientificCalculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Scientific Calculator")
        Grid.rowconfigure(root, 0, weight=1)
        Grid.columnconfigure(root, 0, weight=1)

        # Create Entry widget to display input and output
        self.entry = Entry(root, font=('Arial', 20), bd=5, justify='right')
        self.entry.grid(row=0, column=0, columnspan=6, sticky=N+S+E+W)

        # Create buttons for digits, operations, and scientific functions
        buttons = [
            '7', '8', '9', '/', 'C', 'AC',
            '4', '5', '6', '*', 'sqrt', '^',
            '1', '2', '3', '-', 'log10', 'ln',
            '0', '.', '=', '+', 'sin', 'cos', 'tan'
        ]

        row = 1
        col = 0
        for button in buttons:
            Button(root, text=button, font=('Arial', 15),
                   command=lambda b=button: self.click(b)).grid(row=row, column=col, sticky=N+S+E+W)
            col += 1
            if col > 5:
                col = 0
                row += 1

    def click(self, button):
        if button == '=':
            try:
                expression = self.entry.get()
                expression = expression.replace('^', '**')
                result = eval(expression)
                self.entry.delete(0, 'end')
                self.entry.insert('end', str(result))
            except:
                self.entry.delete(0, 'end')
                self.entry.insert('end', 'Error')
        elif button == 'C':
            current_expression = self.entry.get()
            new_expression = current_expression[:-1]
            self.entry.delete(0, 'end')
            self.entry.insert('end', new_expression)
        elif button == 'AC':
            self.entry.delete(0, 'end')
        elif button in ('sin', 'cos', 'tan', 'sqrt', 'log10', 'ln'):
            try:
                expression = self.entry.get()
                if button == 'sin':
                    result = math.sin(eval(expression))
                elif button == 'cos':
                    result = math.cos(eval(expression))
                elif button == 'tan':
                    result = math.tan(eval(expression))
                elif button == 'sqrt':
                    result = math.sqrt(eval(expression))
                elif button == 'log10':
                    result = math.log10(eval(expression))
                elif button == 'ln':
                    result = math.log(eval(expression))
                self.entry.delete(0, 'end')
                self.entry.insert('end', str(result))
            except:
                self.entry.delete(0, 'end')
                self.entry.insert('end', 'Error')
        else:
            current_expression = self.entry.get()
            new_expression = current_expression + button
            self.entry.delete(0, 'end')
            self.entry.insert('end', new_expression)

if __name__ == "__main__":
    root = Tk()
    calculator = ScientificCalculator(root)
    root.mainloop()
