import tkinter as tk
from tkinter import ttk


class ModuleDialog(tk.Toplevel):
    def __init__(self, parent, module_names, lang):
        super().__init__(parent)
        
        self.result = None
        
        self.title("Module Switch")
        self.module_vars = {}
        for name in module_names:
            var = tk.BooleanVar(value=name[list(name.keys())[0]])
            chk = ttk.Checkbutton(self, text=list(name.keys())[0], variable=var)
            chk.pack(anchor="w")
            self.module_vars[list(name.keys())[0]] = var
        
        btn_frame = ttk.Frame(self)
        print(lang)
        btn_ok = ttk.Button(btn_frame, text=lang['ACCEPT'], command=self.on_ok)
        btn_cancel = ttk.Button(btn_frame, text=lang['CANCEL'], command=self.on_not_ok) 
        btn_ok.pack(side="left")
        btn_cancel.pack(side="left")
        btn_frame.pack()
        
    def on_ok(self):
        self.result = {name:var.get() for name, var in self.module_vars.items()}
        self.destroy()

    def on_not_ok(self):
        self.result = "STOP"
        self.destroy()
