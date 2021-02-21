

import tkinter
import os

# Set display
if os.environ.get('DISPLAY','') == '':
    print('no display found. Using :0.0')
    os.environ.__setitem__('DISPLAY', ':0.0')

class MyApp(tkinter.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.pack()
        self.createWidgets()
    def createWidgets(self):
        self.nameEntry = tkinter.Entry(self)
        self.nameEntry.pack()
        self.name = tkinter.StringVar()
        self.name.set("Ihr Name...")
        self.nameEntry["textvariable"] = self.name
        self.ok = tkinter.Button(self)
        self.ok["text"] = "Ok"
        self.ok["command"] = self.quit
        self.ok.pack(side="right")
        self.rev = tkinter.Button(self)
        self.rev["text"] = "Umdrehen"
        self.rev["command"] = self.onReverse
        self.rev.pack(side="right")
    def onReverse(self):
        self.name.set(self.name.get()[::-1])

if __name__ == "__main__":
    # # # workx
    #root = tkinter.Tk()
    #main = MyApp(root)
    #main.pack(side="top", fill="both", expand=True)
    #root.mainloop()
    
    # # # workx
    myapp = MyApp()
    myapp.mainloop()