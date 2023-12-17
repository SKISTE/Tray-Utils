from utils.commands import Defs_for_all
import tkinter as tk
class MyDialog(tk.Toplevel):
    def __init__(self, parent):
        tk.Toplevel.__init__(self, parent)
        self.title('Выключение ПК')
        self.time_input = tk.IntVar()
        self.is_cancelled = True
        label = tk.Label(self, text='Через сколько минут выключить ПК?')
        spinbox = tk.Spinbox(self, from_=0, to=120, textvariable=self.time_input)
        button_apply = tk.Button(self, text="Применить", command=self.apply) 
        button_cancel = tk.Button(self, text="Отменить все запланированное", command=self.cancel)

        label.pack(pady=10)
        spinbox.pack()
        button_apply.pack() 
        button_cancel.pack()

    def apply(self):
        self.is_cancelled = False
        self.destroy()
        
    def cancel(self):
        self.destroy()

class pc_shutdown(Defs_for_all):
    def __init__(self, config):
        self.name = 'pc_shutdown'          # Name for you func in menu, you can write ID and append in language file or hardcore write name
        # self.subname = 'SUBNAME'    # Name + subname, you can delete this, if wantn't

    def run(self):
        root = tk.Tk()
        root.withdraw()
        
        dialog = MyDialog(root)
        dialog.grab_set()  
        root.wait_window(dialog)
            
        if not dialog.is_cancelled:
            print(f'Выключение через {dialog.time_input.get()} минут')
            self._run_cmd('shutdown /s /t '+str(dialog.time_input.get()*60))
        else:
            self._run_cmd('shutdown /a')

        root.destroy()
        return True