import sys
from inspect import getsourcefile
from os.path import abspath

# prevent python from writing *.pyc files / __pycache__ folders
sys.dont_write_bytecode = True

path_app = abspath(getsourcefile(lambda: 0))[:-8]
if path_app not in sys.path:
    sys.path.append(path_app)

from preconfigured_ttk_widgets import *

class GUI(MainWindow):
    
    def __init__(self):
        super().__init__()
        
        # A ttk notebook made of two frames
        frame_notebook = Notebook(self)
        frame_notebook.add(FirstFrame(), text='Listbox')
        frame_notebook.add(SecondFrame(), text='Combobox')
        frame_notebook.add(ThirdFrame(), text='Window')
        frame_notebook.pack()
            
        # title of the main window
        self.title('Title')
        
        # main menu
        menubar = Menu(self)
        upper_menu = Menu(menubar)
        first = MenuEntry(upper_menu)
        first.text = 'First entry'
        first.command = self.print42
        upper_menu.add_separator()
        upper_menu.create_menu()
        menubar.add_cascade(label='Main menu', menu=upper_menu)
        self.config(menu=menubar)
        
    def print42(self):
        print(42)
        
class FirstFrame(CustomFrame):
    
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
        yscroll = Scrollbar(self)
        yscroll.command = listbox.yview
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
        
class SecondFrame(CustomFrame):
    
    def __init__(self):
        super().__init__()
        
        # label frame
        lf = Labelframe(self)
        lf.text = 'Interdependent Combobox'
    
        # first combobox
        self.combobox1 = Combobox(self, width=11)
        self.combobox1['values'] = ('A', 'B')
        self.combobox1.current(0)
        self.combobox1.bind('<<ComboboxSelected>>', self.update)
        
        # second combobox, which values depends on the first combobox
        self.combobox2 = Combobox(self, width=11)
        self.combobox2.set('Initial value')
        
        # place the labelframe in the frame
        lf.grid(0, 0)
        # place widgets in the labelframe
        self.combobox1.grid(0, 0, in_=lf)
        self.combobox2.grid(1, 0, in_=lf)
        
    def update(self, _):
        value = self.combobox1.get()
        values = {'A': ('1', '2'), 'B': ('3', '4')}
        self.combobox2['values'] = values[value]
        self.combobox2.current(0)
        
class TopLevel1(CustomTopLevel):

    def __init__(self):
        super().__init__()
        
        label1 = Label(self)
        label1.text = 'First window'
        label1.grid(0, 0)
        
class TopLevel2(FocusTopLevel):

    def __init__(self):
        super().__init__()
        
        label1 = Label(self)
        label1.text = 'Second window'
        label1.grid(1, 0)

class ThirdFrame(CustomFrame):
    
    def __init__(self):
        super().__init__()
        
        # button to create a FocusTopLevelWindow
        button1 = Button(self)
        button1.text = 'Normal window'
        button1.command = TopLevel1
        
        # button to create a FocusTopLevelWindow
        button2 = Button(self)
        button2.text = 'Window with focus button'
        button2.command = TopLevel2
        
        # place widgets in the grid
        button1.grid(0, 0)
        button2.grid(1, 0)

if __name__ == '__main__':
    gui = GUI()
    gui.mainloop()