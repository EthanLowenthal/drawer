import pygame
import pyglet
from pygame.constants import *

import Drawer
from Colors import *
from pyglet.window import key

def menu(screen):

    def reset_var():
        # global column
        # global row
        # global select_column
        # global select_row
        # global c

        Drawer.row = 95
        Drawer.column = 10
        Drawer.select_column = 70
        Drawer.select_row = 95
        Drawer.c = 0

    reset_var()

    def Draw_gui():
        # global column
        # global row
        # global select_column
        # global select_row
        # global c

        pygame.draw.rect(screen, colors_alpha[0], (40, 40, Drawer.height - 80, Drawer.width - 80))
        pygame.draw.rect(screen, (238, 255, 238, 100), (50, 50, Drawer.height - 100, Drawer.width - 100))

        for i in colors_alpha:

            Drawer.column += 60
            pygame.draw.rect(screen, colors_alpha[0],  (Drawer.column - 5, Drawer.height -  Drawer.row - 5, 40, 40))
            pygame.draw.rect(screen, i, (Drawer.column, Drawer.height - Drawer.row, 30, 30))
            if  Drawer.column >= Drawer.width - 160:
                 Drawer.column = 10
                 Drawer.row += 70
        pygame.display.flip()

    # def update():
    #     window.flip()

    # def pygame.draw.rect(_color_, x, y, Drawer.height, Drawer.width):
    #     Drawer.width = int(round(Drawer.width))
    #     Drawer.height = int(round(Drawer.height))
    #     image_pattern = pyglet.image.SolidColorImagePattern(color=_color_)
    #     image = image_pattern.create_image(Drawer.width, Drawer.height)
    #     image.blit(x, y)

    def on_key_press():
        while True:
            # global column
            # global row
            # global select_column
            # global select_row
            # global c

            pygame.event.get()
            press = pygame.key.get_pressed()


            pygame.draw.rect(screen, colors_alpha[6],  (Drawer.select_column - 5, Drawer.height -  Drawer.select_row - 5, 40, 40))
            pygame.draw.rect(screen, colors_alpha[Drawer.c], (Drawer.select_column, Drawer.height - Drawer.select_row, 30, 30))
            if press[K_RIGHT] == 1:
                if  Drawer.c == 15:
                     Drawer.c = 15
                     Drawer.select_row = 165

                elif  Drawer.select_column >= Drawer.width - 160:
                     Drawer.select_column = 70
                     Drawer.select_row += 70
                     Drawer.c += 1
                     Drawer.c %= len(colors) + 1


                else:
                     Drawer.c += 1
                     Drawer.c %= len(colors) +1
                     Drawer.select_column += 60
                pygame.draw.rect(screen, (255,255,255,100), (0, 0, Drawer.height, Drawer.width))
                Draw_gui()
                pygame.draw.rect(screen, colors_alpha[6],  (Drawer.select_column - 5, Drawer.height -  Drawer.select_row - 5, 40, 40))
                pygame.draw.rect(screen, colors_alpha[Drawer.c], (Drawer.select_column, Drawer.height - Drawer.select_row, 30, 30))
                Drawer.row = 95
                Drawer.column = 10

            elif press[K_LEFT] == 1:

                if Drawer.select_column <= 70 and Drawer.select_row == 95:
                    Drawer.c = 0

                elif Drawer.c == 11:
                     Drawer.select_column = Drawer.width - 130
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
                pygame.draw.rect(screen, (255,255,255,100), (0, 0, Drawer.height, Drawer.width))
                Draw_gui()
                pygame.draw.rect(screen, colors_alpha[6],  (Drawer.select_column - 5, Drawer.height -  Drawer.select_row - 5, 40, 40))
                pygame.draw.rect(screen, colors_alpha[Drawer.c], (Drawer.select_column, Drawer.height - Drawer.select_row, 30, 30))
                Drawer.row = 95
                Drawer.column = 10

            elif press[K_RETURN] == 1:
                return


    Draw_gui()
    on_key_press()
    # Run new event loop

