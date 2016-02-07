import pygame
from Colors import colors
pygame.init()
screen = pygame.display.set_mode((800,600))
done = False


screen.fill(colors["White"])

while not done:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE or event.type == pygame.QUIT:
            pygame.QUIT()
    pygame.display.flip()