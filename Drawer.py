import pygame
from Colors import colors

screen = pygame.display.set_mode((800,600))
pygame.init()

clock = pygame.time.Clock()
pygame.mouse.set_visible(0)


done = False
size_x = 60
size_y = 60
x_pos = 60
y_pos = 60
color = colors["Red"]


screen.fill(colors["White"])

pygame.display.flip()

def draw_rect():
    print('draw_rect')
    pygame.draw.rect(screen, color, (x_pos,y_pos,size_x,size_y))


def borders():
    print('borders')
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

def move_rect():
    print('move_rect')
    global x_pos
    global y_pos

    for event in pygame.event.get():
        print('keyboard')
        if event.type == pygame.KEYDOWN and event.key == pygame.K_a:
            x_pos -= 3
        if event.type == pygame.KEYDOWN and event.key == pygame.K_d:
            x_pos += 3
        if event.type == pygame.KEYDOWN and event.key == pygame.K_w:
            y_pos -= 3
        if event.type == pygame.KEYDOWN and event.key == pygame.K_s:
            y_pos += 3
        pygame.display.update()


def check_for_quit():
    print('check_for_quit')
    global done
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
            pygame.QUIT()


def main():
    print('main')
    check_for_quit()
    move_rect()
    borders()
    draw_rect()


while not done:
    print('loop')
    main()
    pygame.display.update()
    print('update')
