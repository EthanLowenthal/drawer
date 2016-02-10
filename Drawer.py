import pygame
from Colors import colors

screen = pygame.display.set_mode((800,600))
pygame.init()

clock = pygame.time.Clock()
pygame.mouse.set_visible(0)
pygame.key.set_repeat(10, 10)

done = False
size_x = 60
size_y = 60
x_pos = 60
y_pos = 60
color = colors["Red"]


screen.fill(colors["White"])

pygame.display.flip()

def draw_rect():
    pygame.draw.rect(screen, color, (x_pos,y_pos,size_x,size_y))


def borders():
    global x_pos
    global y_pos

    if x_pos > 790:
         x_pos -= 3
    if x_pos < 10:
         x_pos += 3
    if y_pos > 590:
         y_pos -= 3
    if y_pos < 10:
         y_pos += 3

def move_rect(x_pos,y_pos):
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN and event.key == pygame.K_a:
            x_pos -= 3
            print(x_pos)
        if event.type == pygame.KEYDOWN and event.key == pygame.K_d:
            x_pos += 3
            print(x_pos)
        if event.type == pygame.KEYDOWN and event.key == pygame.K_w:
            y_pos -= 3
            print(y_pos)
        if event.type == pygame.KEYDOWN and event.key == pygame.K_s:
            y_pos += 3
            print(y_pos)




def check_for_quit():
    global done
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
            pygame.QUIT()


def main():
    while not done:
        check_for_quit()
        move_rect(x_pos,y_pos)
        borders()
        draw_rect()
        pygame.display.update()


while not done:
    main()
