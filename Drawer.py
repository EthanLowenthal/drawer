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
    pressed = pygame.key.get_pressed
    if(pressed()[pygame.K_d]):
        x_pos += 3

def main():
    while not done:
        move_rect()
        draw_rect()
        pygame.dispaly.update()

screen.fill(colors["White"])

while not done:
    main()
    pygame.display.flip()