import pygame
from Colors import *
from pygame.locals import *

screen = pygame.display.set_mode((800,600))
pygame.init()

clock = pygame.time.Clock()
pygame.mouse.set_visible(0)
pygame.key.set_repeat(50, 50)

done = False
size_x = 60
size_y = 60
x_pos = 60
y_pos = 60
c = 5
shade = colors_names[c]

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


Brush = Rectangle(x_pos, y_pos, size_y, size_x, screen, shade)

screen.fill(colors_names[3])

pygame.display.flip()

def draw_rect():
    Brush.borders()
    Brush.draw()

def change_colors():
    global shade
    global c
    c += 2
    c = a
    shade = colors_names[c]
    print(c - 1)

def move_brush():

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
        change_colors()


def check_for_quit():
    global done
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
            pygame.QUIT()


def main():
    while not done:
        check_for_quit()
        move_brush()
        draw_rect()
        pygame.display.update()


while not done:
    main()
