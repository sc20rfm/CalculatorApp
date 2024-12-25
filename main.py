import tkinter as tk

# A global variable to hold the current calculation string
calculation = ""

# Function to add a symbol (number/operator) to the calculation string
def add_to_calculation(symbol):
    global calculation
    calculation += str(symbol)
    text_result.delete(1.0, "end")
    text_result.insert(1.0, calculation)

# Function to evaluate the calculation
def evaluate_calculation():
    global calculation
    try:
        calculation = str(eval(calculation))
        text_result.delete(1.0, "end")
        text_result.insert(1.0, calculation)
    except:
        clear_field()
        text_result.insert(1.0, "Error")

# Function to clear the calculation field
def clear_field():
    global calculation
    calculation = ""
    text_result.delete(1.0, "end")

# Initialise the main Tkinter window
root = tk.Tk()
root.geometry("300x275")

# Text box to display the current calculation or result
text_result = tk.Text(root, height=2, width=16, font=("Arial", 24))
text_result.grid(columnspan=5)

# Create number buttons (0-9) and operators (+,-,*,/)
btn_1 = tk.Button(root, text="1", command=lambda: add_to_calculation(1), width=5, font=("Arial", 14))
btn_1.grid(row=2, column=1)
btn_2 = tk.Button(root, text="2", command=lambda: add_to_calculation(2), width=5, font=("Arial", 14))
btn_2.grid(row=2, column=2)
btn_3 = tk.Button(root, text="3", command=lambda: add_to_calculation(3), width=5, font=("Arial", 14))
btn_3.grid(row=2, column=3)
btn_4 = tk.Button(root, text="4", command=lambda: add_to_calculation(4), width=5, font=("Arial", 14))
btn_4.grid(row=3, column=1)
btn_5 = tk.Button(root, text="5", command=lambda: add_to_calculation(5), width=5, font=("Arial", 14))
btn_5.grid(row=3, column=2)
btn_6 = tk.Button(root, text="6", command=lambda: add_to_calculation(6), width=5, font=("Arial", 14))
btn_6.grid(row=3, column=3)
btn_7 = tk.Button(root, text="7", command=lambda: add_to_calculation(7), width=5, font=("Arial", 14))
btn_7.grid(row=4, column=1)
btn_8 = tk.Button(root, text="8", command=lambda: add_to_calculation(8), width=5, font=("Arial", 14))
btn_8.grid(row=4, column=2)
btn_9 = tk.Button(root, text="9", command=lambda: add_to_calculation(9), width=5, font=("Arial", 14))
btn_9.grid(row=4, column=3)
btn_0 = tk.Button(root, text="0", command=lambda: add_to_calculation(0), width=5, font=("Arial", 14))
btn_0.grid(row=5, column=2)
btn_plus = tk.Button(root, text="+", command=lambda: add_to_calculation("+"), width=5, font=("Arial", 14))
btn_plus.grid(row=2, column=4)
btn_minus = tk.Button(root, text="-", command=lambda: add_to_calculation("-"), width=5, font=("Arial", 14))
btn_minus.grid(row=3, column=4)
btn_multiply = tk.Button(root, text="*", command=lambda: add_to_calculation("*"), width=5, font=("Arial", 14))
btn_multiply.grid(row=4, column=4)
btn_divide = tk.Button(root, text="/", command=lambda: add_to_calculation("/"), width=5, font=("Arial", 14))
btn_divide.grid(row=5, column=4)
btn_open = tk.Button(root, text="(", command=lambda: add_to_calculation("("), width=5, font=("Arial", 14))
btn_open.grid(row=5, column=1)
btn_close = tk.Button(root, text=")", command=lambda: add_to_calculation(")"), width=5, font=("Arial", 14))
btn_close.grid(row=5, column=3)

# Create clear and equals buttons
btn_clear = tk.Button(root, text="C", command=clear_field, width=5, font=("Arial", 14))
btn_clear.grid(row=6, column=3, columnspan=2)
btn_equals = tk.Button(root, text="=", command=evaluate_calculation, width=5, font=("Arial", 14))
btn_equals.grid(row=6, column=1, columnspan=2)

# Start the Tkinter main loop to run the application
root.mainloop()

