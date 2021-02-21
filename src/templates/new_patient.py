
import tkinter as tk
from templates.fragments import StringField

class NewPatientFrame(tk.Frame):
    def __init__(self, runtimeHandler, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)

        t = tk.Toplevel(self)
        t.title('Neuer Patient')

        self.runtimeHandler = runtimeHandler

        # Pat Nr
        self.pat_nr = StringField(t, 'Pat Nr',1)
        
        # Pat Name
        self.pat_name = StringField(t, 'Pat Name',2)

        # Anmerkung
        self.anmerkung = StringField(t, 'Anmerkung',3)

        # Button to commit data
        self.apply_btn = tk.Button(
                t, text='Bestätigen', command=self.commit_data
            ).grid(
                row=4, column=1, columnspan=2, padx=5, pady=3
            )
    
    def commit_data(self):
        
        # TODO : Commit data via excel data handler

        self.runtimeHandler.process()