import pyglet
import Drawer
from Colors import *
from pyglet.window import key

window = pyglet.window.Window(800,600)
window.set_caption('Menu')
window.minimize()

def menu():
    window.maximize()
    def reset_var():
        global column
        global row
        global select_column
        global select_row
        global c

        Drawer.row = 95
        Drawer.column = 10
        Drawer.select_column = 70
        Drawer.select_row = 95
        Drawer.c = 0

    reset_var()

    def Draw_gui():
        global column
        global row
        global select_column
        global select_row
        global c

        Draw_rect(colors_alpha[0], 40, 40, window.height - 80, window.width - 80)
        Draw_rect((238, 255, 238, 100), 50, 50, window.height - 100, window.width - 100)

        for i in colors_alpha:

            Drawer.column += 60
            Draw_rect(colors_alpha[0],  Drawer.column - 5, window.height -  Drawer.row - 5, 40, 40)
            Draw_rect(i, Drawer.column, window.height - Drawer.row, 30, 30)
            if  Drawer.column >= window.width - 160:
                 Drawer.column = 10
                 Drawer.row += 70

    def Draw_rect(_color_, x, y, height, width):
        width = int(round(width))
        height = int(round(height))
        image_pattern = pyglet.image.SolidColorImagePattern(color=_color_)
        image = image_pattern.create_image(width, height)
        image.blit(x, y)

    @window.event
    def on_key_press(symbol, modifiers):
        global column
        global row
        global select_column
        global select_row
        global c
        Draw_rect(colors_alpha[6],  Drawer.select_column - 5, window.height -  Drawer.select_row - 5, 40, 40)
        Draw_rect(colors_alpha[Drawer.c], Drawer.select_column, window.height - Drawer.select_row, 30, 30)
        if symbol == key.RIGHT:
            if  Drawer.c == 15:
                 Drawer.c = 15
                 Drawer.select_row = 165

            elif  Drawer.select_column >= window.width - 160:
                 Drawer.select_column = 70
                 Drawer.select_row += 70
                 Drawer.c += 1
                 Drawer.c %= len(colors) + 1


            else:
                 Drawer.c += 1
                 Drawer.c %= len(colors) +1
                 Drawer.select_column += 60
            Draw_rect((255,255,255,100), 0, 0, window.height, window.width)
            Draw_gui()
            Draw_rect(colors_alpha[6],  Drawer.select_column - 5, window.height -  Drawer.select_row - 5, 40, 40)
            Draw_rect(colors_alpha[Drawer.c], Drawer.select_column, window.height - Drawer.select_row, 30, 30)
            Drawer.row = 95
            Drawer.column = 10

        elif symbol == key.LEFT:

            if Drawer.select_column <= 70 and Drawer.select_row == 95:
                Drawer.c = 0

            elif Drawer.c == 11:
                 Drawer.select_column = window.width - 130
                 Drawer.select_row = 95
                 Drawer.c -= 1
                 Drawer.c %= len(colors)

            elif Drawer.select_column <= 70 and Drawer.select_row == 95:
                 Drawer.select_column = 70
                 Drawer.select_row = 95
                 Drawer.c -= 1
                 Drawer.c %= len(colors)

            else:
                 Drawer.c -= 1
                 Drawer.c %= len(colors)
                 Drawer.select_column -= 60
            Draw_rect((255,255,255,100), 0, 0, window.height, window.width)
            Draw_gui()
            Draw_rect(colors_alpha[6],  Drawer.select_column - 5, window.height -  Drawer.select_row - 5, 40, 40)
            Draw_rect(colors_alpha[Drawer.c], Drawer.select_column, window.height - Drawer.select_row, 30, 30)
            Drawer.row = 95
            Drawer.column = 10

        elif symbol == key.ENTER:
            window.minimize()

    def on_draw():
        Draw_rect((255,255,255,100), 0, 0, window.height, window.width)
        Draw_gui()


    pyglet.app.run()

