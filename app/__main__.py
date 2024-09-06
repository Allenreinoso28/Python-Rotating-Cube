import pygame
import pygame.tests
import numpy as np

pygame.init()

WINDOW_SIZE = 800
window_size = (WINDOW_SIZE, WINDOW_SIZE)
screen = pygame.display.set_mode(window_size)

pygame.display.set_caption('Cube Go Burrrrr')

clock = pygame.time.Clock()

fps = 60

#projection matrix converts 3d coord into 2d coord
projection_matrix = np.matrix([[1,0,0],
                              [0,1,0],
                              [0,0,0]])

#vertices
cube_points = [n for n in range(8)]
cube_points[0]= np.matrix([[1],[1],[1]])
cube_points[1]= np.matrix([[1],[-1],[1]])
cube_points[2]= np.matrix([[-1],[1],[1]])
cube_points[3]= np.matrix([[-1],[-1],[1]])
cube_points[4]= np.matrix([[1],[1],[-1]])
cube_points[5]= np.matrix([[1],[-1],[-1]])
cube_points[6]= np.matrix([[-1],[1],[-1]])
cube_points[7]= np.matrix([[-1],[-1],[-1]])

## dot product is the function that does what i want
# result = np.dot(orthogonal_matrix, cube_points[0])
# print(result)

#how to access int from matrix where cube_points[point][row,column]
# print(cube_points[0][0,0])

def multipleMatrices(a,b):
    result = np.dot(a,b)
    return result

# colours
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)

#positioning values
SCALE = 100
OFFSET = WINDOW_SIZE/2

running = True
while running:
    angle_a = angle_b = angle_c = 0
    clock.tick(fps)
    screen.fill(black)

    #rotation matrix goes here


    for point in cube_points:
        #apply rotation to point

        #convert point to a 2coord and draw
        point_2d = multipleMatrices(projection_matrix, point)
        x = point_2d[0,0] * SCALE + OFFSET
        y = point_2d[1,0] * SCALE + OFFSET
        pygame.draw.circle(screen, red, (x,y), 7)


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    

    angle_a += 0.1
    pygame.display.update()   

pygame.quit()