# Tkinter widgets
# Copyright (C) 2016 Antoine Fourmy (antoine.fourmy@gmail.com)
# Released under the GNU General Public License GPLv3

import sys
from inspect import getsourcefile
from os.path import abspath

# prevent python from writing *.pyc files / __pycache__ folders
sys.dont_write_bytecode = True

path_app = abspath(getsourcefile(lambda: 0))[:-7]
if path_app not in sys.path:
    sys.path.append(path_app)

import os
import tkinter as tk
from custom_widgets import CustomFrame
from preconfigured_ttk_widgets import *
from tkinter import ttk

class GUI(tk.Tk):
    
    def __init__(self, path_app):
        tk.Tk.__init__(self)
        
        # A ttk notebook made of two frames
        frame_notebook = ttk.Notebook(self)
        first_frame = MainFrame(self)
        second_frame = CustomFrame()
        frame_notebook.add(first_frame, text='Frame 1')
        frame_notebook.add(second_frame, text='Frame 2')
        frame_notebook.pack(side=tk.LEFT, fill=tk.BOTH, expand=1)
            
        # title of the main window
        self.title('Title')
        
        # main menu
        menubar = tk.Menu(self)
        upper_menu = tk.Menu(menubar, tearoff=0)
        upper_menu.add_command(label='First menu', command=lambda: 0)
        upper_menu.add_command(label='Second menu', command=lambda: 0)
        upper_menu.add_separator()
        upper_menu.add_command(label='Separated menu', command=lambda: 0)
        menubar.add_cascade(label='Main menu',menu=upper_menu)
        self.config(menu=menubar)
        
class MainFrame(CustomFrame):
    
    def __init__(self, master):
        super().__init__()
        
        # label frame
        lf_fr = LF(self, padding=(6, 6, 12, 12), text='Example with listbox')
        lf_fr.grid(x=0, y=0)
                                                        
        # label + associated entry
        label = L(self, text = 'Write something :')
        self.entry = E(self, width=13)
        
        # button to add an entry in the list
        button_add = B(self, text='Add to list', command=self.add, width=13)
        
        # button to delete and print the listbox selection
        button_delete = B(self, text='Delete selection', command=self.delete,
                                                                    width=13)
        
        # button to empty the listbox
        button_clear = B(self, text='Clear', command=self.clear, width=13)
        
        # object listbox and associated scrollbar
        self.listbox = LB(self, width=15, height=7)   
        yscroll = SB(self, command=self.listbox.yview)
        self.listbox.configure(yscrollcommand=yscroll.set)
                                        
        # place all widgets in the grid
        label.grid(in_=lf_fr, x=0, y=0)
        self.entry.grid(in_=lf_fr, x=1, y=0)
        button_add.grid(in_=lf_fr, x=2, y=0)
        button_delete.grid(in_=lf_fr, x=3, y=0)
        button_clear.grid(in_=lf_fr, x=4, y=0)
        self.listbox.grid(in_=lf_fr, x=0, xs=5, y=3)
        yscroll.grid(in_=lf_fr, x=0, xs=5, y=4)
        
    def add(self):
        user_input = self.entry.get()
        self.listbox.insert(user_input)
        
    def delete(self):
        self.listbox.pop_selected()
        
    def clear(self):
        self.listbox.clear()

if __name__ == "__main__":
    gui = GUI(path_app)
    gui.mainloop()