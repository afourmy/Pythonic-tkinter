import sys
from inspect import getsourcefile
from os.path import abspath

# prevent python from writing *.pyc files / __pycache__ folders
sys.dont_write_bytecode = True

path_app = abspath(getsourcefile(lambda: 0))[:-9]
if path_app not in sys.path:
    sys.path.append(path_app)

from os.path import abspath, pardir, join
from preconfigured_widgets import *
from math import cos, sin
from random import choice
from PIL import ImageTk

class GUI(MainWindow):
    
    def __init__(self, path_app):
        super().__init__()
        
        path_parent = abspath(join(path_app, pardir))
        path_icon = join(path_app, 'Icons')
        
        # dictionnary containing all images 
        self.dict_img = {}
        for obj, size in (('sun', 100), ('earth', 30), ('moon', 10)):
            image = ImageTk.Image.open(join(path_icon, obj + '.png'))
            resized_image = image.resize((size, size))
            self.dict_img[obj] = ImageTk.PhotoImage(resized_image)
        
        galaxy = Galaxy(self)
        galaxy.pack()
            
        # title of the main window
        self.title('Galaxy')
        
        self.bind('d', lambda _: galaxy.draw())

        # main menu
        menubar = Menu(self)
        

        
        # test = Menu(menubar)
        
        ooo = Menu(menubar)
        
        move_entry = MenuEntry(ooo)
        move_entry.text = 'Move'
        move_entry.cmd = galaxy.move
        
        move_entry1 = MenuEntry(ooo)
        move_entry1.text = 'Move'
        move_entry1.cmd = galaxy.move
        
        move_entry2 = MenuEntry(ooo)
        move_entry2.text = 'Move'
        move_entry2.cmd = galaxy.move
        
        inner_menu = MenuCascade(menubar)
        inner_menu.imenu = ooo
        inner_menu.text = 'inner_menu'

        # menubar.add_cascade(label='Main menu', menu=ooo)

        
        # upper_menu = Menu(menubar)
        # upper_menu.entry('Move', galaxy.move)
        # upper_menu.entry('Stop moving', galaxy.stop)
        # upper_menu.entry('Draw', galaxy.draw)
        # upper_menu.create_menu()
        # menubar.add_cascade(label='Main menu', menu=upper_menu)
        # menubar.create_menu()
        self.config(menu=menubar)
        
class Galaxy(Canvas):
    
    def __init__(self, gui):
        super().__init__()
        
        # force focus on the canvas for the bindings to work properly
        self.focus_force()
        
        # use the right-click to move the background
        self.bind('<ButtonPress-1>', self.scroll_start)
        self.bind('<B1-Motion>', self.scroll_move)
        
        self.motion = None
        
        # create colored lines between the sun and the moon when pressing space
        self.draw_lines = False
        
        self.time = 0
        self.colors = ('blue', 'red', 'green', 'gold', 'pink', 'purple')
        
        self.sun = self.create_image(400, 400, image=gui.dict_img['sun'])
        self.earth = self.create_image(400, 300, image=gui.dict_img['earth'])
        self.moon = self.create_image(100, 300, image=gui.dict_img['moon'])
        
        self.move()
        
    ## Right-click scroll

    def scroll_start(self, event):
        # we record the position of the mouse when left-click is pressed
        # to check, when it is released, if the intent was to drag the canvas
        # or to have access to the right-click menu
        self._start_pos_main_node = event.x, event.y
        self.scan_mark(event.x, event.y)

    def scroll_move(self, event):
        self.scan_dragto(event.x, event.y, gain=1)
        
    ## Planet motion
        
    def move(self):
        self.time += 1
        # compute the position of the earth / moon on the canvas
        x = 550 + 400 * cos(self.time * 0.00005)
        y = 400 + 200 * sin(self.time * 0.00005)
        p = x + 40 * cos(2 + self.time * 0.001)
        q = y + 40 * sin(2 + self.time * 0.001)
        # if the drawing mode is activated, draw a line every 20 iterations
        if self.draw_lines and not self.time % 20:
            # choose a random color
            line_color = choice(self.colors)
            # draw the line
            self.create_line(500, 400, p, q, fill=line_color)
        # update the position of the earth / moon images on the canvas
        self.coords(self.earth, x, y)
        self.coords(self.moon, p, q)
        # start over in 1 ms
        self.motion = self.after(1, self.move)
        
    def stop(self):
        if self.motion is not None:
            self.after_cancel(self.motion)
            self._job = None
        
    ## Draw colored lines 
    
    def draw(self):
        self.stop()
        self.draw_lines = not self.draw_lines
        self.move()
        
if __name__ == '__main__':
    gui = GUI(path_app)
    gui.mainloop()