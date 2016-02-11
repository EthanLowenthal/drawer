import pygame
from Colors import colors
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
color = colors["Red"]
brush = pygame.draw.rect(screen, color, (x_pos,y_pos,size_x,size_y))

class Brush(pygame.sprite.Sprite):

        def __init__(self, display, x_axis, y_axis, w, h):
                self.screen = display
                self.rect = pygame.Rect(x_axis,y_axis,w,h)


screen.fill(colors["White"])

pygame.display.flip()

def draw_rect():
    global brush
    brush.normalize()
    brushsprite = pygame.sprite.RenderPlain(brush)
    screen.blit(background, ball.rect, ball.rect)
    brushsprite.draw(screen)

def borders():
    global x_pos
    global y_pos

    if x_pos > 790:
         x_pos -= size_x + 13
    if x_pos < 10:
         x_pos += 3
    if y_pos > 590:
         y_pos -= 3
    if y_pos < 10:
         y_pos += 3


def move_brush():
    global x_pos
    global y_pos
    global size_x
    global size_y
    global brush
    press = pygame.key.get_pressed()

    if press[K_w] == 1:
        y_pos -= 3
    if press[K_a] == 1:
        x_pos -= 3
    if press[K_s] == 1:
        y_pos += 3
    if press[K_d] == 1:
        x_pos += 3
    if press[K_MINUS] or press[K_KP_MINUS] == 1:
        brush.inflate(-3,-3)
    if press[K_EQUALS] or press[K_PLUS] or press[K_KP_PLUS] == 1:
        brush.inflate(3,3)


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
        borders()
        draw_rect()
        pygame.display.update()


while not done:
    main()
