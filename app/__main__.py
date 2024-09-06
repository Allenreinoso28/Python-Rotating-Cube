import pygame
import pygame.tests

pygame.init()

window_size = (800, 800)
screen = pygame.display.set_mode(window_size)

pygame.display.set_caption('Cube Go Burrrrr')

clock = pygame.time.Clock()

fps = 60

#vertices


#colours
black = (0,0,0)
white = (255, 255, 255)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(black)

    pygame.display.flip()

    clock.tick(fps)

    pygame.draw.circle()
    
pygame.quit()