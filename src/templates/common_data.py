import tkinter as tk
from templates.fragments import (
    StringField,
    RadioField,
    DropdownField) 

class CommonDataFrame(tk.Frame):
    def __init__(self, runtimeHandler, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)

        t = tk.Toplevel(self)
        t.title('Allgemeine Daten')

        self.runtimeHandler = runtimeHandler

        # Geburtsdatum
        self.geburtsdatum = StringField(t, 'Geburtsdatum',1, 1)
        
        # Geschlecht
        sex = {
            'm' : 'm',
            'w' : 'w'
        }
        self.geschlecht = RadioField(t, 'Geschlecht',2, 1, **sex)

        # AZ med. Diagnosen
        self.medDiagnosen = StringField(t, 'AZ med. Diagnosen', 3, 1)

        # Kognitive Fähigkeit
        kog_abilities = {
            'orientiert' : '1',
            'geht so' : '2'
        }
        self.kogFaehigkeiten = DropdownField(t, 'Kognitive Fähigkeit', 4, 1, **kog_abilities)


        # Button to commit data
        self.apply_btn = tk.Button(
                t, text='Bestätigen', command=self.commit_data
            ).grid(
                row=5, column=1, columnspan=2, padx=5, pady=3
            )
    
    def commit_data(self):
        
        # TODO : Commit data via excel data handler

        self.runtimeHandler.process()