# Pythonic tkinter
Pythonic tkinter is an attempt to make tkinter code idiomatic by:
- breaking the definition of the most common widgets on several lines with getters and setters
- creating new widgets when necessary

## Widget creation
For most widgets, tkinter syntax is the following:
```
widget = tk.Widget(parent_window, text=..., command=..., width=..., height=...)
```

This syntax makes it hard to comply by the 80-characters PEP8 rule without using multi-line constructs or backslashes.
With getters and setters, the text and command parameters can be defined after the widget is created.

Creation of a widget with tkinter classic syntax:
```
button = tkinter.Button(self, width=15, text='test_button', command=function)
label = tkinter.Label(self, width=15, text='test_label')
```

Creation of a widget with pythonic tkinter syntax:
```
button = Button(self, width=15)
button.text = 'test_button'
button.command=function

label = Label(self, width=15)
label.text = 'test_label'
```

## Grid method

The syntax of the grid method is simplified:
- the two first parameters are mandatory: they define the row and the column numbers
- the two following parameters are optional (default: 1): they define the rowspan and column
- the padding value (padx and pady) have default values (4 for most widgets)

Use of grid with tkinter classic syntax:
```
button.grid(row=1, column=1, rowspan=2, columnspan=2, padx=4, pady=4)
```

Use of grid with pythonic tkinter syntax:
```
button.grid(1, 1, 2, 2)
```

## Menu creation

With pythonic tkinter, each entry is an object of its own, as well as each cascade menu:
- an entry object has getters and setters for the text and command properties
- a cascade object has getters and setters for the a text and menu properties 

Creation of a menu with tkinter classic syntax:
```
root = Tk()
menu = Menu(root)
root.config(menu=menu)
first_menu = Menu(menu)
menu.add_cascade(label="cascade", menu=first_menu)
first_menu.add_command(label="first entry", command=function1)
first_menu.add_separator()
first_menu.add_command(label="second entry", command=function2)
```

Creation of a menu with pythonic tkinter syntax:
```
root = Tk()
menu = Menu(root)
root.menu = menu

first_menu = Menu(menu)

first_entry = MenuEntry(first_menu)
first_entry.text = 'first entry'
first_entry.command = function1

first_menu.separator()

second_entry = MenuEntry(first_menu)
second_entry.text = 'first entry'
second_entry.command = function2

cascade = MenuCascade(menu)
main_cascade.text = 'cascade'
main_cascade.inner_menu = first_menu
```

## Bindings

With pythonic tkinter, a binding is an object of its own:
- getters and setters are implemented to define the associated event and command
- bind() and unbind() function allows the user to activate or deactivate the binding

Creation of a binding with tkinter classic syntax
```
widget.bind(event, function, add='')
widget.tag_bind(tag, event, function, add='')
```

Creation of a binding with pythonic tkinter syntax
```
binding = Binding(self.cvs, tag=None, add='')
binding.event = event
binding.command = function
binding.bind() (or binding.unbind())
```

# Basic example to compare the syntax

## Classic tkinter
```
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
```

## Pythonic tkinter
```
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
```

## Result

The differences result from:
- Pythonic tkinter using ttk widgets by default, instead of standard tkinter widgets.
- the preconfigured style and padding in pythonic tkinter

This .py file of this example is available in the 'comparison.py' file. 
