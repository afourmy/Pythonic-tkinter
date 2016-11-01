# ACLizer
# Copyright (C) 2016 Antoine Fourmy (antoine.fourmy@gmail.com)
# Released under the GNU General Public License GPLv3

import tkinter as tk
from tkinter import ttk
from tkinter.scrolledtext import ScrolledText

class CustomFrame(tk.Frame):
    
    def __init__(self):
        super().__init__()
        color = "#A1DBCD"
        self.configure(background=color)        
        ttk.Style().configure("TButton", background=color)
        ttk.Style().configure("TLabel", background=color)
        ttk.Style().configure('TLabelframe', background=color)
        ttk.Style().configure('TLabelframe.Label', background=color)
        ttk.Style().configure('TCheckbutton', background=color)
        
class CustomTopLevel(tk.Toplevel):
    
    def __init__(self):
        super().__init__()
        color = "#A1DBCD"
        self.configure(background=color)        
        ttk.Style().configure("TButton", background=color)
        ttk.Style().configure("TLabel", background=color)
        ttk.Style().configure('TLabelframe', background=color)
        ttk.Style().configure('TLabelframe.Label', background=color)
        ttk.Style().configure('TCheckbutton', background=color)
        
class FocusTopLevel(CustomTopLevel):
    
    def __init__(self):
        super().__init__()
        self.var_focus = tk.IntVar()
        self.checkbutton_focus = tk.Checkbutton(
                                                self, 
                                                text = "Focus", 
                                                bg = "#A1DBCD", 
                                                variable = self.var_focus, 
                                                command = self.change_focus
                                                )
                                                
        self.checkbutton_focus.grid(row=0, column=0, sticky=tk.W)
            
    def change_focus(self):
        self.wm_attributes("-topmost", self.var_focus.get())
        
class CustomScrolledText(ScrolledText):
    
    def __init__(self, parent_frame):
        super().__init__(
        parent_frame,
        wrap = "word",
        bg = "beige"
        )
        
        self.tag_config(
        "title", 
        foreground="blue", 
        font=("Helvetica", "12", "bold underline")
        )
        