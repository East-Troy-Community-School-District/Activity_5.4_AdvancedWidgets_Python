'''
Draw Panel
Pawelski
5/19/2023
Python II

Instructions:
Consider the following questions as we dicuss the program. Make
sure you take notes on the program!
1. What is contained in the module named colors?
2. How many event handlers does this program have?
3. What event is "<ButtonRelease-1>"? What about "<B1-Motion>"?
4. How does the draw() event handler work?
5. What happens if you delete the end_draw() event handler? Don't forget
   to delete the bind statement as well!
6. What line of code allows the canvas to fill the window as it is resized?
7. What line of code clears the canvas?
8. What is a list box? How does this program use a listbox?
'''

import tkinter as tk
from colors import *

# -- Global Variables --
new_click = True
selected_color = "snow"


# -- Event Handlers --
def draw(event):
    '''
    Draws on the canvas when the left button is held.
    '''
    global previous_x, previous_y, new_click, selected_color
    if new_click:
        previous_x = event.x
        previous_y = event.y
        new_click = False
    canvas.create_line(previous_x, previous_y, event.x, event.y, fill=selected_color)
    previous_x = event.x
    previous_y = event.y

def end_draw(event):
    '''
    Checks if the user released their click.
    '''
    global new_click
    new_click = True
    
def select_color(event):
    '''
    Sets the color based on the selection.
    '''
    global selected_color
    selected_color = colors[colors_listbox.curselection()[0]]

def clear():
    '''
    Clears the canvas.
    '''
    canvas.delete("all")


# -- GUI --
window = tk.Tk()
window.title("Draw Panel")

# Left control frame
control_frame = tk.Frame(window)

colors_label = tk.Label(control_frame, text="Colors")
colors_label.pack()

colors_listbox = tk.Listbox(control_frame)
colors_listbox.bind("<ButtonRelease-1>", select_color)
for i in range(0, len(colors)):
    colors_listbox.insert("end", colors[i])
    colors_listbox.itemconfig(i, bg=colors[i])
colors_listbox.pack(fill=tk.Y, expand=True)

clear_button = tk.Button(control_frame, text="Clear", command=clear)
clear_button.pack(pady=3)

control_frame.pack(side=tk.LEFT, fill=tk.Y, padx=5, pady=5)

# Canvas
canvas = tk.Canvas(window, bg="white", cursor="spraycan", height=500, width=500)
canvas.bind("<B1-Motion>", draw)
canvas.bind("<ButtonRelease-1>", end_draw)
canvas.pack(side=tk.LEFT, padx=5, pady=5, fill=tk.BOTH, expand=True)

window.mainloop()