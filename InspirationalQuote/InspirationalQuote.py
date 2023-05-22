'''
Inspiration Quote
Pawelski
5/21/2023
Python II

Instructions:
Consider the following questions as we dicuss the program. Make
sure you take notes on the program!
1. Try resizing the window while the application runs. You can't! Why?
   What line of code causes this to happen?
2. Does this program contain any event handlers?
3. What line of code adds the image to the canvas?
4. What line of code adds the text to the canvas?
5. What happens if you reverse the order of adding the image and text?
6. Change the canvas's bg property to a different color. What happens?
   What does this tell you about the picture?
7. Change the text's justify property to RIGHT. What happens?
'''

import tkinter as tk
import random

def select_quote():
    '''
    Selects a quote from the file of quotes.
    '''
    file = open("quotes.txt", "r")
    quotes = file.readlines()
    file.close()
    return random.choice(quotes).strip()


# -- GUI --
window = tk.Tk()
window.title("Inspirational Quote")
window.geometry("640x360")
window.resizable(False, False)

canvas = tk.Canvas(window, bg="light sky blue")
background_image = tk.PhotoImage(file="background.png")
canvas.create_image(0, 0,
                    anchor=tk.NW,
                    image=background_image)
canvas.create_text(320, 180,
                   text=select_quote(),
                   font=("Comic Sans", 24, "bold"),
                   width=600,
                   justify=tk.CENTER)
canvas.pack(fill=tk.BOTH, expand=True)

window.mainloop()