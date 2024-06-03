import tkinter as tk

# Define functions
def button_click(number):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, str(current) + str(number))

def button_clear():
    entry.delete(0, tk.END)

def button_equal():
    second_number = entry.get()
    entry.delete(0, tk.END)
    if math == "addition":
        entry.insert(0, first_number + float(second_number))
    elif math == "subtraction":
        entry.insert(0, first_number - float(second_number))
    elif math == "multiplication":
        entry.insert(0, first_number * float(second_number))
    elif math == "division":
        entry.insert(0, first_number / float(second_number))

def button_add():
    global math
    math = "addition"
    get_first_number()

def button_subtract():
    global math
    math = "subtraction"
    get_first_number()

def button_multiply():
    global math
    math = "multiplication"
    get_first_number()

def button_divide():
    global math
    math = "division"
    get_first_number()

def get_first_number():
    global first_number
    first_number = entry.get()
    entry.delete(0, tk.END)

# Set up the window
root = tk.Tk()
root.title("Simple Calculator")

# Create the entry widget
entry = tk.Entry(root, width=35, borderwidth=5)
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# Define buttons
buttons = [
    ("1", 3, 0), ("2", 3, 1), ("3", 3, 2),
    ("4", 2, 0), ("5", 2, 1), ("6", 2, 2),
    ("7", 1, 0), ("8", 1, 1), ("9", 1, 2),
    ("0", 4, 0)
]

for button_text, row, col in buttons:
    button = tk.Button(root, text=button_text, padx=40, pady=20, command=lambda button_text=button_text: button_click(button_text))
    button.grid(row=row, column=col)

# Define operation buttons
operation_buttons = [
    ("+", button_add, 5, 0), ("-", button_subtract, 6, 0),
    ("*", button_multiply, 6, 1), ("/", button_divide, 6, 2),
    ("=", button_equal, 5, 1), ("Clear", button_clear, 5, 2)
]

for button_text, command, row, col in operation_buttons:
    button = tk.Button(root, text=button_text, padx=40, pady=20, command=command)
    button.grid(row=row, column=col, columnspan=2 if button_text == "=" else 1)

root.mainloop()
