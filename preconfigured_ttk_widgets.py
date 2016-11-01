## Label, Entry, Button, LabelFrame, Listbox, Scrollbar => L, E, B, LF, LB, SB
# the grid method is overwritten to create pre-padded (with preinitialized 
#  padx, pady) widgets.
# 'x' / 'y' parameters are used instead of the classic ttk row / column
# arguments, and 'xs' / 'ys' replace rowspan and columnspan.
# sticky is initialized to its most common value: west (~ left)

import tkinter as tk
from tkinter import ttk
from improved_listbox import ImprovedListbox
            
def overrides(interface_class):
    def overrider(method):
        assert(method.__name__ in dir(interface_class))
        return method
    return overrider  
    
def class_factory(name, OriginalWidget, defaults):
    
    px, py, sy = defaults
        
    @overrides(OriginalWidget)
    def grid(self, x, y, xs=1, ys=1, padx=px, pady=py, sticky=sy, cnf={}, **kw):
        # x (resp. y) is the row (resp. column) number
        # xs and ys stands for xspan / yspan (~ rowspan / columnspan)
        kw.update({
                   'padx': padx, 
                   'pady': pady,
                   'row': x,
                   'rowspan': xs,
                   'column': y,              
                   'columnspan': ys,
                   'sticky': sticky
                   })
        self.tk.call(('grid', 'configure', self._w) + self._options(cnf, kw))
              
    newclass = type(name, (OriginalWidget,), {'grid': grid})  
    globals()[name] = newclass
    
subwidget_creation = (
                      ('L', ttk.Label, (4, 4, 'w')), 
                      ('E', ttk.Entry, (4, 4, 'w')), 
                      ('B', ttk.Button, (4, 4, 'w')),
                      ('LF', ttk.LabelFrame, (10, 10, 'w')),
                      ('LB', ImprovedListbox, (0, 0, 'w')),
                      ('SB', tk.Scrollbar, (0, 0, 'ns'))
                      )
    
for subwidget, ttk_class, defaults in subwidget_creation:
    class_factory(subwidget, ttk_class, defaults)