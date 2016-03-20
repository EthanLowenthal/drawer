
import pygame
import time
from Colors import *
from pygame.locals import *
from menu import *

width = 800
height = 600

screen = pygame.display.set_mode((width,height))
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
pause = False


screen.fill(White)

class Rectangle:

    def __init__(self, x, y, width, height, screen, color_):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.screen = screen
        self.color = color_


    def draw(self):

        pygame.draw.rect(self.screen, self.color, [self.x, self.y, self.height, self.width])
        pygame.draw.rect(self.screen, Black, [width - 60, height - 60, 40, 40])
        pygame.draw.rect(self.screen, self.color, [width - 55, height - 55, 30, 30])


    def move(self, change_x, change_y):

        self.x += change_x
        self.y += change_y


    def borders(self):

        if self.x > width - self.width - 10:
             self.x -= 3
        if self.x < 10:
             self.x += 3
        if self.y < 10:
             self.y += 3
        if self.y > height - self.height - 10:
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
        c %= len(colors)
        self.color = colors[c - 1]

Brush = Rectangle(x_pos, y_pos, size_y, size_x, screen, colors_alpha[c])

pygame.display.flip()

def draw_rect():
    Brush.borders()
    Brush.draw()


def move_brush():
    global select_column
    global select_row
    global c
    global pause

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
    if press[K_c] == 1:
        pygame.mouse.set_visible(1)
        select_column = 70
        select_row = 75
        menu(screen)
        Brush.change_colors()
        pygame.mouse.set_visible(0)
    if press[K_p] == 1:
        if pause == True:
            pause = False
        else: pause = True
        time.sleep(0.09)




def check_for_quit():
    global done
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
            pygame.QUIT()


def main():
    global pause
    while not pause:
        move_brush()
        draw_rect()
        check_for_quit()
        pygame.display.update()
    while pause:
        if press[K_p] == 1:
            if pause == True:
                pause = False
            else: pause = True
            time.sleep(0.09)





main()
