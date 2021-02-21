import tkinter
from tkinter.simpledialog import *
import sys
import os

#### DOCS #####
#
# https://docs.python.org/3/library/tkinter.html
# https://github.com/python/cpython/blob/216cb1469f566ba5493bf53a73da9ccdac05ccfc/Lib/tkinter/ttk.py#L720
# http://openbook.rheinwerk-verlag.de/python/39_002.html#u39.2.1
# https://www.tcl.tk/man/tcl8.6/TkCmd/contents.htm
#
###############

# Set display
if os.environ.get('DISPLAY','') == '':
    print('no display found. Using :0.0')
    os.environ.__setitem__('DISPLAY', ':0.0')

# Create main window
master = tkinter.Tk()
master.title("Dataflow")
master.geometry("400x400")

# make a label for the window
label1 = tkinter.Label(master, text='Hellooooo')
# Lay out label
label1.pack()

# f = askfloat('askfloat', 'put in a float value:')
d = Dialog(label1, 'Dialog')
print(d, type(d))

# Run forever
master.mainloop()
