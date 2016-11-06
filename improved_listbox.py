# Pythonic Tkinter
# Copyright (C) 2016 Antoine Fourmy (antoine.fourmy@gmail.com)
# Released under the GNU General Public License GPLv3

import tkinter as tk

class ImprovedListbox(tk.Listbox):
    
    def __init__(self, *args, **kwargs):

        if 'activestyle' not in kwargs:
            kwargs['activestyle'] = 'none'
        if 'selectmode' not in kwargs:
            kwargs['selectmode'] = 'extended'
            
        super().__init__(*args, **kwargs)
        self.bind('<Button-1>', self.set_index)
        self.bind('<B1-Motion>', self.move_selected_row)
        self.cur_index = None
    
    def __contains__(self, obj):
        return obj in self.get(0, "end")
        
    def insert(self, obj):
        super(ImprovedListbox, self).insert(tk.END, obj)
        
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
            self.pop(self.get(obj - idx))
        
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