import tkinter
import sys
import os

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

# Run forever
master.mainloop()
