import pygame
pygame.init()
screen = pygame.display.set_mode((800,600))
done = False

Black = (0,0,0)
White = (255,255,255)
Red = (255,0,0)
Lime = (0,255,0)
Blue = (0,0,255)
Yellow = (255,255,0)
Cyan = (0,255,255)
Magenta = (255,0,255)
Silver = (192,192,192)
Gray = (128,128,128)
Maroon = (128,0,0)
Olive = (128,128,0)
Green = (0,128,0)
Purple = (128,0,128)
Teal = (0,128,128)
Navy = (0,0,128)

colors = {"Black" : (0,0,0),
"White" : (255,255,255),
"Red" : (255,0,0),
"Lime" : (0,255,0),
"Blue" : (0,0,255),
"Yellow" : (255,255,0),
"Cyan" : (0,255,255),
"Magenta" : (255,0,255),
"Silver" : (192,192,192),
"Gray" : (128,128,128),
"Maroon" : (128,0,0),
"Olive" : (128,128,0),
"Green" : (0,128,0),
"Purple" : (128,0,128),
"Teal" : (0,128,128),
"Navy" : (0,0,128)}

screen.fill(colors["White"])

while not done:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE or event.type == pygame.QUIT:
            pygame.QUIT()
    pygame.display.flip()