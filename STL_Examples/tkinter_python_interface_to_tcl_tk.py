# tkinter is the standard python interface to the Tcl/Tk GUI toolkit.

# python3 -m tkinter from cmd line should open a window demonstrating a smiple Tk interface, letting you konw that
# tkinter is properly installed on your system.

from tkinter import *
from tkinter import ttk

root = Tk()
frm = ttk.Frame(root, padding=100)
frm.grid()
ttk.Label(frm, text="hello world").grid(column=0, row=0)
ttk.Button(frm, text="Quit", command=root.destroy).grid(column=0, row=1)
root.mainloop()