'''
Place Order
Pawelski
5/19/2023
Python II

Instructions:
Consider the following questions as we dicuss the program. Make
sure you take notes on the program!
1. What is the purpose of the tk.IntVar() variable called size? How do
   you get the value out of a tk.IntVar() variable?
2. What value is associated with the sixteen_radiobutton? What about
   the thirtytwo_radiobutton?
3. How did Mr. Pawelski add a border to the size_frame?
4. How did Mr. Pawelski add a border to the cost_label?
5. How does the grid() geometry manager add widgets to the window?
'''

import tkinter as tk

# -- Event Handlers --
def calculate_cost():
    '''
    Calculates the cost of the order.
    '''
    if size.get() == 16:
        cost = int(quantity_entry.get()) * 5.99
    else:
        cost = int(quantity_entry.get()) * 9.99
    cost = round(cost, 2)
    cost_label.config(text="$" + str(cost))


# -- GUI --
window = tk.Tk()
window.title("Place Order")

size = tk.IntVar()	# Used to track which radiobutton is selected

size_frame = tk.Frame(window, relief=tk.GROOVE, bd=1)
size_label = tk.Label(size_frame, text="USB Flash Drive Sizes")
size_label.pack(padx=3, pady=3)
sixteen_radiobutton = tk.Radiobutton(size_frame,
                                     text="16 GB",
                                     variable=size,
                                     value=16)
sixteen_radiobutton.select()
sixteen_radiobutton.pack(anchor=tk.W, padx=3, pady=3)
thirtytwo_radiobutton = tk.Radiobutton(size_frame,
                                       text="32 GB",
                                       variable=size,
                                       value=32)
thirtytwo_radiobutton.pack(anchor=tk.W, padx=3, pady=3)
size_frame.grid(row=0, column=0, padx=10, pady=10)

quantity_frame = tk.Frame(window)
quantity_label = tk.Label(quantity_frame, text="Quantity:")
quantity_label.pack(padx=3, pady=3)
quantity_entry = tk.Entry(quantity_frame)
quantity_entry.pack(padx=3, pady=3)
quantity_frame.grid(row=0, column=1, padx=10, pady=10)

calculate_cost_button = tk.Button(window,
                                  text="Calculate Cost",
                                  command=calculate_cost,
                                  height=2,
                                  width=20)
calculate_cost_button.grid(row=1, column=0, columnspan=2, padx=10, pady=10)

cost_frame = tk.Frame(window)
label1 = tk.Label(cost_frame, text="Cost:")
label1.pack(side=tk.LEFT, padx=3, pady=3)
cost_label = tk.Label(cost_frame,
                      relief=tk.GROOVE,
                      bd=2,
                      width=20,
                      anchor=tk.W)
cost_label.pack(side=tk.LEFT, padx=3, pady=3)
cost_frame.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

window.mainloop()