from tkinter import Tk, Label, Frame, Button, messagebox, filedialog, ttk, Scrollbar, VERTICAL, HORIZONTAL
import pandas as pd

window = Tk()
window.config(bg='black')
window.geometry('600x400')
window.minsize(width=600,height=400)
window.title('Read Excel Data')

window.columnconfigure(0, weight = 25)
window.rowconfigure(0, weight = 25)
window.columnconfigure(0, weight = 1)
window.rowconfigure(1, weight = 1)

frame1 = Frame(window, bg='gray26')
frame1.grid(column=0,row=0,sticky='nsew')
frame2 = Frame(window, bg='gray26')
frame2.grid(column=0,row=1,sticky='nsew')

frame1.columnconfigure(0, weight = 1)
frame1.rowconfigure(0, weight = 1)

frame2.columnconfigure(0, weight = 1)
frame2.rowconfigure(0, weight = 1)
frame2.columnconfigure(1, weight = 1)
frame2.rowconfigure(0, weight = 1)

frame2.columnconfigure(2, weight = 1)
frame2.rowconfigure(0, weight = 1)

frame2.columnconfigure(3, weight = 2)
frame2.rowconfigure(0, weight = 1)

table = ttk.Treeview(frame1, height=16)
table.grid(column=0, row=1, sticky='nsew')


window.mainloop()
