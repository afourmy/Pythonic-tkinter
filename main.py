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
        first_frame = MainFrame()
        second_frame = SecondFrame()
        frame_notebook.add(first_frame, text='Frame 1')
        frame_notebook.add(second_frame, text='Frame 2')
        frame_notebook.pack(side=tk.LEFT, fill=tk.BOTH, expand=1)
            
        # title of the main window
        self.title('Title')
        
        # main menu
        menubar = tk.Menu(self)
        upper_menu = tk.Menu(menubar, tearoff=0)
        upper_menu.add_command(label='First menu', command=lambda: _)
        upper_menu.add_command(label='Second menu', command=lambda: _)
        upper_menu.add_separator()
        upper_menu.add_command(label='Separated menu', command=lambda: _)
        menubar.add_cascade(label='Main menu',menu=upper_menu)
        self.config(menu=menubar)
        
class SecondFrame(CustomFrame):
    
    def __init__(self):
        super().__init__()
        
        # label frame
        lf = Labelframe(self)
        lf.text = 'Interdependant combobox'
    
        # first combobox
        self.combobox1 = Combobox(self, width=11)
        self.combobox1['values'] = ('A', 'B')
        self.combobox1.current(0)
        self.combobox1.bind('<<ComboboxSelected>>', lambda _: self.update())
        
        # second combobox, which values depends on the first combobox
        self.combobox2 = Combobox(self, width=11)
        self.combobox2.set('Initial value')
        
        # place the labelframe in the frame
        lf.grid(0, 0)
        # place widgets in the labelframe
        self.combobox1.grid(0, 0, in_=lf)
        self.combobox2.grid(1, 0, in_=lf)
        
    def update(self):
        value = self.combobox1.get()
        values = {'A': ('1', '2'), 'B': ('3', '4')}
        self.combobox2['values'] = values[value]
        self.combobox2.current(0)
        
class MainFrame(CustomFrame):
    
    def __init__(self):
        super().__init__()
        
        # label frame
        lf = Labelframe(self)
        lf.text = 'A customized listbox'
                                                        
        # label + associated entry
        label = Label(self)
        label.text = 'Write something :'
        entry = Entry(self, width=13)
        
        # object listbox and associated scrollbar
        listbox = Listbox(self, width=15, height=7)   
        yscroll = Scrollbar(self, command=listbox.yview)
        listbox.configure(yscrollcommand=yscroll.set)
        
        # button to add an entry in the list
        button_add = Button(self, width=13)
        button_add.text = 'Add to list'
        button_add.command = lambda: listbox.insert(entry.get())
        
        # button to delete and print the listbox selection
        button_delete = Button(self, width=13)
        button_delete.text = 'Delete selection'
        button_delete.command = listbox.pop_selected
        
        # button to empty the listbox
        button_clear = Button(self, width=13)
        button_clear.text = 'Clear'
        button_clear.command = listbox.clear
                                        
        # place the label frame in the toplevel window
        lf.grid(0, 0)
        # place the widgets inside the label frame
        label.grid(0, 0, in_=lf)
        entry.grid(1, 0, in_=lf)
        button_add.grid(2, 0, in_=lf)
        button_delete.grid(3, 0, in_=lf)
        button_clear.grid(4, 0, in_=lf)
        listbox.grid(0, 3, 5, in_=lf)
        yscroll.grid(0, 4, 5, in_=lf)

if __name__ == '__main__':
    gui = GUI(path_app)
    gui.mainloop()