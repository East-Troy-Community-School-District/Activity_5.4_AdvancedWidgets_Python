'''
Draw Shapes
Pawelski
5/21/2023
Python II

Instructions:
Consider the following questions as we dicuss the program. Make
sure you take notes on the program!
1. What is the difference between radiobuttons and checkbuttons?
2. Which line draws a rectangle on the canvas? Circle?
3. What is the purpose of the tk.BooleanVar() variable called draw_rectangle?
4. Change the if before draw_circle.get() to an elif. How does this
   change the program?

Before moving on, add the missing code to this program.
'''

import tkinter as tk

# -- Event Handlers --
def draw():
    '''
    Draws the selected shapes on the canvas.
    '''
    canvas.delete("all")
    if draw_rectangle.get():
        canvas.create_rectangle(50, 50, 100, 200)
    if draw_circle.get():
        canvas.create_oval(300, 50, 400, 150)
    # Add the code to check is a square should be drawn and draw it


# -- GUI --
window = tk.Tk()
window.title("Draw Shapes")
window.geometry("600x300")

draw_rectangle = tk.BooleanVar()
draw_square = tk.BooleanVar()
draw_circle = tk.BooleanVar()

shapes_frame = tk.Frame(window)
shapes_label = tk.Label(shapes_frame, text="Shapes")
shapes_label.pack()
rectangle_checkbutton = tk.Checkbutton(shapes_frame,
                                       text="Rectangle",
                                       variable=draw_rectangle)
rectangle_checkbutton.pack(padx=3, pady=3, anchor=tk.W)
square_checkbutton = tk.Checkbutton(shapes_frame,
                                    text="Square",
                                    variable=draw_square)
square_checkbutton.pack(padx=3, pady=3, anchor=tk.W)
circle_checkbutton = tk.Checkbutton(shapes_frame,
                                    text="Circle",
                                    variable=draw_circle)
circle_checkbutton.pack(padx=3, pady=3, anchor=tk.W)
draw_button = tk.Button(shapes_frame, text="Draw", command=draw)
draw_button.pack(padx=3, pady=3)
shapes_frame.pack(side=tk.LEFT, padx=5, pady=5)

canvas = tk.Canvas(window, bg="white")
canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=5, pady=5)

window.mainloop()