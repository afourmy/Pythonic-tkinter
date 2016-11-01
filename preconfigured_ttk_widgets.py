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
              
    @property
    def text(self):
        return self.get()
        
    @text.setter
    def text(self, value):
        self.configure(text=value)
        
    widget_functions = {'grid': grid, 'text': text}
        
    if name == 'Button':
        @property
        def command(self):
            self.cget('command')
            
        @command.setter
        def command(self, value):
            self.configure(command=value)
            
        widget_functions.update({'command': command})
            
    newclass = type(name, (OriginalWidget,), widget_functions)
    globals()[name] = newclass
    
subwidget_creation = (
                      ('Label', ttk.Label, (4, 4, 'w')), 
                      ('Entry', ttk.Entry, (4, 4, 'w')), 
                      ('Button', ttk.Button, (4, 4, 'w')),
                      ('Labelframe', ttk.LabelFrame, (10, 10, 'w')),
                      ('Listbox', ImprovedListbox, (0, 0, 'w')),
                      ('Scrollbar', tk.Scrollbar, (0, 0, 'ns'))
                      )
    
for subwidget, ttk_class, defaults in subwidget_creation:
    class_factory(subwidget, ttk_class, defaults)