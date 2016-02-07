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
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_d or pygame.K_RIGHT:
                x_pos += 60


def check_for_quit():
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN and  event.key == pygame.K_ESCAPE or pygame.QUIT:
                done = True
                pygame.quit()


def main():
    while not done:
        move_rect()
        draw_rect()
        check_for_quit()
        pygame.display.update()

screen.fill(colors["White"])

while not done:
    main()
    pygame.display.flip()