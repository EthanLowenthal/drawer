import pygame
from Colors import colors
screen = pygame.display.set_mode((800,600))
pygame.init()

done = False
size_x = 60
size_y = 60
x_pos = 60
y_pos = 60
color = colors["Red"]



def draw_rect():
    pygame.draw.rect(screen, color, (x_pos,y_pos,size_x,size_y))

def move_rect():
    global x_pos
    global y_pos

    if(pygame.key.get_pressed()[pygame.K_w]):
         y_pos += 3
    if(pygame.key.get_pressed()[pygame.K_s]):
         y_pos -= 3
    if(pygame.key.get_pressed()[pygame.K_d]):
         x_pos += 3
    if(pygame.key.get_pressed()[pygame.K_a]):
         x_pos -= 3
    borders()

def borders():
    if x_pos > 790:
         x_pos += 3

def main():
    while not done:
        draw_rect()
        move_rect()

screen.fill(colors["White"])

while not done:
    main()
    pygame.display.flip()
