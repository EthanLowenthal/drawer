#PyDraw v. NoIdea.NoIdea

import pygame
import time
from Colors import *
from pygame.locals import *

screen = pygame.display.set_mode((800,600))
pygame.init()

clock = pygame.time.Clock()
pygame.mouse.set_visible(0)
pygame.key.set_repeat(500, 30)

done = False
size_x = 60
size_y = 60
x_pos = 60
y_pos = 60
c = 5
row = 75
column = 10
gui_on = False


screen.fill(White)

class Rectangle:

    def __init__(self, x, y, width, height, screen, color):

        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.screen = screen
        self.color = color


    def draw(self):

        pygame.draw.rect(self.screen, self.color, [self.x, self.y, self.height, self.width])
        pygame.draw.rect(self.screen, Black, [screen.get_width() - 60, screen.get_height() - 60, 40, 40])
        pygame.draw.rect(self.screen, self.color, [screen.get_width() - 55, screen.get_height() - 55, 30, 30])


    def move(self, change_x, change_y):

        self.x += change_x
        self.y += change_y


    def borders(self):

        if self.x > screen.get_width() - self.width - 10:
             self.x -= 3
        if self.x < 10:
             self.x += 3
        if self.y < 10:
             self.y += 3
        if self.y > screen.get_height() - self.height - 10:
             self.y -= 3
        if self.width < 2:
            self.width = 2
            self.height = 2
        if self.width > 120:
            self.width = 120
            self.height = 120

    def size(self, change_x, change_y):
        self.height += change_x
        self.width += change_y

    def change_colors(self):
        global c
        time.sleep(0.1)
        c += 2
        c %= len(colors)
        self.color = colors_names[c]

class gui:

    def __init__(self, colors, screen):
        self.colors = colors
        self.border = Rect(40, 40, screen.get_width() - 80, screen.get_height() - 80)
        self.window = Rect(50, 50, screen.get_width() - 100, screen.get_height() - 100)
        self.screen = screen


    def draw(self):
        global gui_on
        gui_on = True
        global press
        column = 10
        row = 75
        pygame.draw.rect(self.screen, Black, self.border)
        pygame.draw.rect(self.screen, (238, 255, 238), self.window)
        for i in self.colors:
            column += 60
            pygame.draw.rect(self.screen, Black, Rect(column - 5, row - 5, 40, 40))
            pygame.draw.rect(self.screen, i, Rect(column, row, 30, 30))
            if column >= screen.get_width() - 160:
                column = 10
                row += 70



    def select(self):
        global select_column
        global select_row
        global c
        global gui_on
        global last_selected
        last_selected = c

        gui.draw()

        pygame.draw.rect(screen, Yellow, Rect(select_column - 5, select_row - 5, 40, 40))
        pygame.draw.rect(self.screen, colors[c], Rect(select_column, select_row, 30, 30))

        print(select_column, select_row)
        pygame.display.update()

        time.sleep(0.09)

        if pygame.key.get_pressed()[K_RIGHT] == 1:



            if screen.get_width() - 160 and select_row == len(colors) * 60 + 160:
                c = c

            elif select_column >= screen.get_width() - 160:
                select_column = 70
                select_row += 70
                c += 1
                c %= len(colors)

            else:
                c += 1
                c %= len(colors)
                select_column += 60
                select_row = 75
                last_selected = c + 1



        if pygame.key.get_pressed()[K_LEFT] == 1:




            if select_column <= 70 and select_row == 75:
                    print('hi')
                    c = c

            elif select_column <= 159:
                select_column = 70
                select_row = 75
                c -= 1
                c %= len(colors)

            else:
                c -= 1
                c %= len(colors)
                select_column -= 60
                select_row = 75
                last_selected = c + 1




gui = gui(colors, screen)

Brush = Rectangle(x_pos, y_pos, size_y, size_x, screen, colors_names[c])

pygame.display.flip()

def draw_rect():
    Brush.borders()
    Brush.draw()


def move_brush():
    global gui_on
    global select_column
    global select_row
    global c

    press = pygame.key.get_pressed()

    if press[K_w] == 1:
        Brush.move(0,-3)
    if press[K_a] == 1:
        Brush.move(-3,0)
    if press[K_s] == 1:
        Brush.move(0,3)
    if press[K_d] == 1:
        Brush.move(3,0)
    if press[K_MINUS] or press[K_KP_MINUS] == 1:
        Brush.size(-3,-3)
    if press[K_EQUALS] or press[K_PLUS] or press[K_KP_PLUS] == 1:
        Brush.size(3,3)
    if press[K_SPACE] == 1:
        Brush.change_colors()
    if press[K_c] == 1:
        pygame.mouse.set_visible(1)
        select_column = 70
        select_row = 75
        gui.draw()
        gui_on = True
        c = 0




def check_for_quit():
    global done
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
            pygame.QUIT()


def main():
    while not done:
        move_brush()
        if gui_on == True:
            gui.select()
            check_for_quit()
            pygame.display.update()

        else:
            draw_rect()
            check_for_quit()
            pygame.display.update()





while not done:
    main()
