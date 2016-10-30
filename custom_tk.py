# ACLizer
# Copyright (C) 2016 Antoine Fourmy (antoine.fourmy@gmail.com)
# Released under the GNU General Public License GPLv3

import tkinter as tk
from tkinter import ttk
from tkinter.scrolledtext import ScrolledText

class CustomFrame(tk.Frame):
    
    def __init__(self):
        super().__init__()
        self.configure(background="#A1DBCD")        
        ttk.Style().configure("TButton", background="#A1DBCD")
        ttk.Style().configure("TLabel", background="#A1DBCD")
        ttk.Style().configure('TLabelframe', background="#A1DBCD")
        ttk.Style().configure('TLabelframe.Label', background="#A1DBCD")
        ttk.Style().configure('TCheckbutton', background="#A1DBCD")
        
class CustomTopLevel(tk.Toplevel):
    
    def __init__(self):
        super().__init__()
        self.configure(background="#A1DBCD")        
        ttk.Style().configure("TButton", background="#A1DBCD")
        ttk.Style().configure("TLabel", background="#A1DBCD")
        ttk.Style().configure('TLabelframe', background="#A1DBCD")
        ttk.Style().configure('TLabelframe.Label', background="#A1DBCD")
        ttk.Style().configure('TCheckbutton', background="#A1DBCD")
        
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
    
class ObjectListbox(tk.Listbox):
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.bind('<Button-1>', self.set_index)
        self.bind('<B1-Motion>', self.move_selected_row)
        self.cur_index = None
    
    def __contains__(self, obj):
        return obj in self.get(0, "end")
        
    def yield_all(self):
        for obj in self.get(0, "end"):
            yield obj
        
    def selected(self):
        for selected_line in self.curselection():
            yield self.get(selected_line)
        
    def pop(self, obj):
        if str(obj) in self:
            obj_index = self.get(0, tk.END).index(str(obj))
            self.delete(obj_index)
            return obj
        
    def pop_selected(self):
        # indexes stored in curselection are retrieved once and for all,
        # and as we remove objects from the listbox, the real index is updated:
        # we have to decrease the curselection index by how many objects
        # we've deleted so far.
        for idx, obj in enumerate(self.curselection()):
            yield self.pop(self.get(obj - idx))
        
    def clear(self):
        self.delete(0, tk.END)
        
    def set_index(self, event):
        self.cur_index = self.nearest(event.y)
        
    def move_selected_row(self, event):
        row_id = self.nearest(event.y)
        value = self.get(row_id)
        if row_id != self.cur_index:
            self.delete(row_id)
            self.insert(row_id + 1 - 2*(row_id > self.cur_index), value)
            self.cur_index = row_id
            
## Pre-padded ttk widgets
            
def overrides(interface_class):
    def overrider(method):
        assert(method.__name__ in dir(interface_class))
        return method
    return overrider  
    
def class_factory(name, OriginalWidget):
        
    @overrides(OriginalWidget)
    def grid(self, cnf={}, padx=4, pady=4, **kw):
        kw.update({"padx": padx, "pady": pady})
        self.tk.call(
              ('grid', 'configure', self._w)
              + self._options(cnf, kw))
              
    newclass = type(
                    name,
                    (OriginalWidget,),
                    {"grid": grid}
                    )
                    
    globals()[name] = newclass
    
subwidget_creation = (("PB", ttk.Button), ("PE", ttk.Entry), ("PL", ttk.Label))
    
for subwidget, ttk_class in subwidget_creation:
    class_factory(subwidget, ttk_class)
    