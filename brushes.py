import pygame
from colors import *
from drawer import *
from functions import *

pygame.init()

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

    def change_colors(self):
        global shade
        global c
        time.sleep(0.09)
        c += 2
        if c > len(colors_names):
            c = 1
        self.color = colors_names[c]

class gui:

    def __init__(self, colors):
        self.colors = colors


    def draw_gui(self):
        pass



Brush = Rectangle(x_pos, y_pos, size_y, size_x, screen, colors_names[c])
