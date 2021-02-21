import tkinter as tk
from tkinter.simpledialog import *
import sys
import os

from runtime_handler import RuntimeHandler

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

class MainWindow(tk.Frame):
    def __init__(self, runtimeHandler,*args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)
        self.button = tk.Button(
                self, text='+ Neuer Patient', 
                command=runtimeHandler.process
            ).pack(
                padx=10, pady=20, fill='x'
            )


if __name__ == '__main__':
    root = tk.Tk()
    root.title('Dataflow')
    root.geometry('200x200')

    runtimeHandler = RuntimeHandler()

    main = MainWindow(master=root,runtimeHandler=runtimeHandler)
    main.pack(side='top', fill='both', expand=True)

    root.mainloop()