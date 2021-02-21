import tkinter as tk

class StringField():
    def __init__(self, parent, label_name, row=1, col=1):
        self.value = tk.StringVar

        self._lbl = tk.Label(
            parent, text=label_name+': ').grid(
                row=row, column=col, padx=5, pady=3, sticky="W")
        self._entry = tk.Entry(
            parent, textvariable=self.value).grid(
                row=row, column=col+1, padx=5, pady=3)


class RadioField():
    def __init__(self, parent, label_name, row=1, col=1, **kwargs):
        self.value = tk.StringVar()
        idx = 1

        self._lbl = tk.Label(
            parent, text=label_name+': ').grid(
                row=row, column=col, padx=5, pady=3, sticky="W")
        
        self._radiobtns = dict()
        for key, value in kwargs.items():
            rb = tk.Radiobutton(
                    parent, text=value, variable=self.value, value=key
                ).grid(
                    row=row, column=col+idx, padx=5, pady=3
                )
            self._radiobtns.update({key : value})
            idx += 1


class DropdownField():
    def __init__(self, parent, label_name, row=1, col=1, **options):
        self.value = tk.StringVar()
        self.value.set('')
        
        self._lbl = tk.Label(
            parent, text=label_name+': ').grid(
                row=row, column=col, padx=5, pady=3, sticky="W")
        
        self._dropdown = tk.OptionMenu(
                parent, self.value,*options
            ).grid(
                row=row, column=col+1, padx=5, pady=3
            )