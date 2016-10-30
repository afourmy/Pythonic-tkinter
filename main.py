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
from custom_widgets import CustomFrame, ObjectListbox, PE, PL, PB
from tkinter import ttk

class GUI(tk.Tk):
    
    def __init__(self, path_app):
        tk.Tk.__init__(self)
        
        # ACLizer GUI is a ttk notebook made of two frames
        frame_notebook = ttk.Notebook(self)
        first_frame = MainFrame(self)
        second_frame = CustomFrame()
        frame_notebook.add(first_frame, text='Configuration')
        frame_notebook.add(second_frame, text='Commands')
        frame_notebook.pack(side=tk.LEFT, fill=tk.BOTH, expand=1)
            
        # title of the main window
        self.title('ACLizer')
        
        # main menu
        menubar = tk.Menu(self)
        upper_menu = tk.Menu(menubar, tearoff=0)
        upper_menu.add_command(label='test', command=lambda: 0)
        upper_menu.add_separator()
        menubar.add_cascade(label='Main',menu=upper_menu)
        self.config(menu=menubar)
        
class MainFrame(CustomFrame):
    
    def __init__(self, master):
        super().__init__()
        
        # label frame used to create a new ACL
        lf_fr = ttk.Labelframe(self, padding=(6, 6, 12, 12), text='ACL creation')
        lf_fr.grid(row=0, column=0, columnspan=10, pady=5, padx=5, sticky='nsew')
                                                        
        # ACL number
        label_number = PL(self, text = 'ACL number')
        entry_number = PE(self, width=10)
        
        # ACL permit / deny option
        label_mode = PL(self, text = 'Mode')
        mode_list = ttk.Combobox(self, width=11)
        mode_list['values'] = ('Permit', 'Deny')
        mode_list.current(0)
        
        # ACL source address and wildcard mask
        label_source_ip = PL(self, text = 'Source IP')
        entry_source_ip = PE(self, width=15)
        
        label_source_wc = PL(self, text = 'Source wilcard mask')
        entry_source_wc = PE(self, width=15)
        
        # button to create a new ACL
        button_add = PB(self, text='Create ACL', command=lambda:0)
        # button to add an ACL entry
        button_add = PB(self, text='Add new entry', command=lambda:0)
        
        # ACL listbox
        self.acl_listbox = ObjectListbox(self, activestyle='none', width=75, 
                                        height=7, selectmode='extended')
        yscroll = tk.Scrollbar(self, 
                            command=self.acl_listbox.yview, orient=tk.VERTICAL)
        self.acl_listbox.configure(yscrollcommand=yscroll.set)
                                        
        # widget placement in the grid
        label_number.grid(in_=lf_fr, row=0, column=0, pady=2, padx=5, sticky=tk.W)
        entry_number.grid(in_=lf_fr, row=1, column=0, pady=2, padx=5, sticky=tk.W)
        label_mode.grid(in_=lf_fr, row=0, column=1, pady=2, padx=5, sticky=tk.W)
        mode_list.grid(in_=lf_fr, row=1, column=1, pady=2, padx=5, sticky=tk.W)
        
        label_source_ip.grid(in_=lf_fr, row=0, column=2, pady=2, padx=5, sticky=tk.W)
        entry_source_ip.grid(in_=lf_fr, row=1, column=2, pady=2, padx=5, sticky=tk.W)
        label_source_wc.grid(in_=lf_fr, row=0, column=3, pady=2, padx=5, sticky=tk.W)
        entry_source_wc.grid(in_=lf_fr, row=1, column=3, pady=2, padx=5, sticky=tk.W)
        
        button_add.grid(in_=lf_fr, row=2, column=0, pady=2, padx=5, sticky=tk.W)
        
        self.acl_listbox.grid(row=1, rowspan=2, column=0, columnspan=10, pady=2, padx=5)
        yscroll.grid(row=1, column=10, rowspan=2, pady=5, padx=5, sticky='ns')
        
    def create_acl(self):
        pass
        
    def add_acl_entry(self):
        pass

if __name__ == "__main__":
    gui = GUI(path_app)
    gui.mainloop()