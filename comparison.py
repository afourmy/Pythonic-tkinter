import sys
from inspect import stack
from os.path import abspath, dirname

# prevent python from writing *.pyc files / __pycache__ folders
sys.dont_write_bytecode = True

path_app = dirname(abspath(stack()[0][1]))

if path_app not in sys.path:
    sys.path.append(path_app)

## Standard tkinter

import tkinter as tk

class ClassicTkinter(tk.Tk):
    
    def __init__(self):
        super().__init__()
        
        label = tk.Label(self, text='Write something :')
        label.grid(row=0, column=0)
        
        self.entry = tk.Entry(self, width=17)
        self.entry.grid(row=1, column=0)
        
        button = tk.Button(self, text='OK', command=self.print_entry, width=16)
        button.grid(row=2, column=0)
        
    def print_entry(self):
        print(self.entry.text)
        
## Pythonic tkinter

import pythonic_tkinter as pt

class PythonicTkinter(pt.MainWindow):
    
    def __init__(self):
        super().__init__()
        
        label = pt.Label(self)
        label.text = 'Write something :'
        label.grid(0, 0)
        
        self.entry = pt.Entry(self, width=17)
        self.entry.grid(1, 0)
        
        button = pt.Button(self, width=16)
        button.text = 'OK'
        button.command = self.print_entry
        button.grid(2, 0)
        
    def print_entry(self):
        print(self.entry.text)
        self.destroy()
        
if __name__ == '__main__':
    example = PythonicTkinter()
    example.mainloop()