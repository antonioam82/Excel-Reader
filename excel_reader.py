from tkinter import Tk, Label, Button, messagebox, filedialog, ttk, Scrollbar, VERTICAL, HORIZONTAL
import pandas as pd

window = Tk()
window.config(bg='black')
window.geometry('600x400')
window.minsize(width=600,height=400)
window.title('Read Excel Data')

window.columnconfigure(0, weight = 25)
window


window.mainloop()
