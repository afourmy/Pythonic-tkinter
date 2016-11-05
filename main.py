# Pythonic Tkinter
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
        lf = Labelframe(self, padding=(6, 6, 12, 12), text='Example with listbox')
                                                        
        # label + associated entry
        label = Label(self)
        label.text = 'Write something :'
        self.entry = Entry(self, width=13)
        
        # button to add an entry in the list
        button_add = Button(self, width=13)
        button_add.text = 'Add to list'
        button_add.command = self.add
        
        # button to delete and print the listbox selection
        button_delete = Button(self, width=13)
        button_delete.text = 'Delete selection'
        button_delete.command = self.delete                               
        
        # button to empty the listbox
        button_clear = Button(self, width=13)
        button_clear.text = 'Clear'
        button_clear.command = self.clear
        
        # object listbox and associated scrollbar
        self.listbox = Listbox(self, width=15, height=7)   
        yscroll = Scrollbar(self, command=self.listbox.yview)
        self.listbox.configure(yscrollcommand=yscroll.set)
                                        
        # place the label frame in the toplevel window
        lf.grid(0, 0)
        # place the widgets inside the label frame
        label.grid(0, 0, in_=lf)
        self.entry.grid(1, 0, in_=lf)
        button_add.grid(2, 0, in_=lf)
        button_delete.grid(3, 0, in_=lf)
        button_clear.grid(4, 0, in_=lf)
        self.listbox.grid(0, 3, 5, in_=lf)
        yscroll.grid(0, 4, 5, in_=lf)
        
    def add(self):
        user_input = self.entry.get()
        self.listbox.insert(user_input)
        
    def delete(self):
        self.listbox.pop_selected()
        
    def clear(self):
        self.listbox.clear()

if __name__ == '__main__':
    gui = GUI(path_app)
    gui.mainloop()