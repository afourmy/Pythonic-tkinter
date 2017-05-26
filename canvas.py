import sys
from inspect import getsourcefile
from os.path import abspath

# prevent python from writing *.pyc files / __pycache__ folders
sys.dont_write_bytecode = True

path_app = abspath(getsourcefile(lambda: 0))[:-9]
if path_app not in sys.path:
    sys.path.append(path_app)

from os.path import abspath, pardir, join
from pythonic_tkinter import *
from math import cos, sin
from random import choice
from PIL import ImageTk

class GUI(MainWindow):
    
    def __init__(self, path_app):
        super().__init__()
        
        path_parent = abspath(join(path_app, pardir))
        path_icon = join(path_app, 'images')
        
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
        
        imenu = Menu(menubar)
        
        move_entry = MenuEntry(imenu)
        move_entry.text = 'Move'
        move_entry.command = galaxy.move
        
        stop_entry = MenuEntry(imenu)
        stop_entry.text = 'Stop'
        stop_entry.command = galaxy.stop
        
        draw_entry = MenuEntry(imenu)
        draw_entry.text = 'Draw'
        draw_entry.command = galaxy.draw
        
        cascade = MenuCascade(menubar)
        cascade.text = 'Cascade'
        cascade.inner_menu = imenu

        self.config(menu=menubar)
        
class Galaxy(Canvas):
    
    def __init__(self, gui):
        super().__init__()
        
        # force focus on the canvas for the bindings to work properly
        self.focus_force()
        
        # use the right-click to move the background
        scroll_binding_start = Binding(self)
        scroll_binding_start.event = '<ButtonPress-1>'
        scroll_binding_start.command = self.scroll_start
        
        scroll_binding_move = Binding(self)
        scroll_binding_move.event = '<B1-Motion>'
        scroll_binding_move.command = self.scroll_move
        
        self.binds(scroll_binding_start, scroll_binding_move)
        
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