from tkinter import *
import time
import sys

window = Tk()
window.title("Python Dijital Saat")
window.geometry("490x180")
window.resizable(1, 1)

text = ("Roboto", 80, 'bold')
background = "yellow"
foreground = "red"
border = 30

label = Label(window, font=text, bg=background, fg=foreground, bd=border)
label.grid(row=0, column=1)


def digitalClock():
    time_live = time.strftime("%H:%M:%S")
    label.config(text=time_live)
    label.after(200, digitalClock)


digitalClock()
window.mainloop()
