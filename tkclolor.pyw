from tkinter import Canvas, END, Entry, Label, Scale, Text, Tk , Button
import ttips

root = Tk()
root.title('TKcolor')


# Ensure the .ico file is in same dir
# as this source code is run from.

# Rename disk.ico to your own icon
root.iconbitmap('icon.ico')

def clkd_btn():
    import os
    os.system("start tkcolorchart.pyw")


st_bar = Label(root, text='                     Status: Ready                      ', bd=2, relief='sunken', anchor='w')
def slider_update(source):
    """Update sliders values."""
    red = red_slider.get()
    green = green_slider.get()
    blue = blue_slider.get()

    colour = '#%02x%02x%02x' % (red, green, blue)
    Canvas.config(bg=colour, cursor="crosshair")
    hex_text.delete(0, END)
    hex_text.insert(0, colour)

import time
text = Label(text="TKCOLOR")
red_slider = Scale(root, from_=0, to=255, command=slider_update)

green_slider = Scale(root, from_=0, to=255, command=slider_update)

blue_slider = Scale(root, from_=0, to=255, command=slider_update)

btn_one = Button(root, text='   Click me to open color chart    ',
                 command=clkd_btn)
time.sleep(0.5)
ttips.Create(red_slider, 'Red' , bgcol="red", fontsize=15)
ttips.Create(blue_slider, 'Blue', bgcol="blue", fontsize=15)
ttips.Create(green_slider, 'Green',bgcol="green", fontsize=15)



Canvas = Canvas(root, width=200, height=200)

hex_text = Entry(root)
btn_one.grid(row=1,column=1, columnspan=4)
red_slider.grid(row=2, column=1)
green_slider.grid(row=2, column=2)
blue_slider.grid(row=2, column=3)
Canvas.grid(row=3, column=1, columnspan=3)
hex_text.grid(row=4, column=1, columnspan=3)
st_bar.grid(row=5, column=1, columnspan=4)

root.mainloop()

"""Simple button.
   Stand-alone example from Tk Assistant.
   stevepython.wordpress.com
   pyshambles.blogspot.com
"""
from tkinter import Button, LabelFrame, Tk

root = Tk()
root.title('Button')

def clkd_btn():
    """Button was clicked."""
    print('Button was clicked')





