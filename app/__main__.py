import pygame
import pygame.tests
import numpy as np
import math

pygame.init()
pygame.font.init()
my_font = pygame.font.SysFont('Arial', 20)

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



# colours
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
blue = (0, 255, 0)
green = (0, 0 , 255)
yellow = (0, 255, 255)
purple = (255, 255, 0)

fill = False

#positioning values
SCALE = 100
OFFSET = WINDOW_SIZE/2
angle_x = angle_y = angle_z = 0
SPEED = 0.05
 
def multiplyMatrices(a,b):
    result = np.dot(a,b)
    return result

def drawLine(point1, point2):
    pygame.draw.line(screen, white, point1, point2, 3)

def drawFace(face):
    pygame.draw.polygon(screen, face[4], (face[0], face[1],face[2], face[3]))

def display_data(screen, data, furthest):
    # Starting position for the text (top-left corner)
    x, y = 10, 10
    # Loop through each item in the list and render it on the screen
    for item in data:
        text_surface = my_font.render(str(item), True, white)  # Render text in white color
        screen.blit(text_surface, (x, y))  # Draw the text at position (x, y)
        text_furthest = my_font.render(str(furthest), True, white)
        screen.blit (text_furthest, (10, 750))
        y += 25  # Move down for the next item (adjust 40 to control spacing)


running = True
paused = False
while running:
    clock.tick(fps)
    if paused == False:
        screen.fill(black)

        #rotation matrix goes here
        x_rotation_matrix = np.matrix([[1,0,0],
                                    [0,math.cos(angle_x),(-math.sin(angle_x))],
                                    [0,math.sin(angle_x),math.cos(angle_x)]])
        
        y_rotation_matrix = np.matrix([[math.cos(angle_y),0,math.sin(angle_y)],
                                    [0,1,0],
                                    [(-math.sin(angle_y)),0,math.cos(angle_y)]])
        
        z_rotation_matrix = np.matrix([[math.cos(angle_z),(-math.sin(angle_z)),0],
                                    [math.sin(angle_z),math.cos(angle_z),0],
                                    [0,0,1]])
        
        #store 2d points for line drawing
        rotated_points = [n for n in range(8)]
        points_final = [n for n in range(8)]
        count = 0
        #will store furthest point to know which faces not to draw
        furthest = 0
        furthest_point = None 
        furthest_pointID = 0
        for point in cube_points:

        

            #apply rotation to point
            point_spinX = multiplyMatrices(x_rotation_matrix, point)
            point_spinXY = multiplyMatrices(y_rotation_matrix, point_spinX)
            point_spinY = multiplyMatrices(y_rotation_matrix, point)
            point_spinXYZ = multiplyMatrices(z_rotation_matrix, point_spinXY)
            rotated_points[count] = (round(float(point_spinXY[0,0]),4), round(float(point_spinXY[1,0]),4), round(float(point_spinXY[2,0]),4))

            #finding the point with the most neg z-value
            if rotated_points[count][2] <= furthest:
                furthest = point_spinXY[2,0]
                furthest_point = rotated_points[count]
                furthest_pointID = count
                
            # print(point_spinXYZ)
            #convert point to a 2coord and draw
            point_2d = multiplyMatrices(projection_matrix, point_spinXY)

            x = point_2d[0,0] * SCALE + OFFSET
            y = point_2d[1,0] * SCALE + OFFSET
            #store 2d point
            points_final[count] = (x,y)
            count += 1
            # pygame.draw.circle(screen, red, (x,y), 7)
        
        #line drawing
        if fill == False:
            drawLine(points_final[0], points_final[1])
            drawLine(points_final[1], points_final[3])
            drawLine(points_final[3], points_final[2])
            drawLine(points_final[2], points_final[0])
            drawLine(points_final[4], points_final[5])
            drawLine(points_final[5], points_final[7])
            drawLine(points_final[7], points_final[6])
            drawLine(points_final[6], points_final[4])
            drawLine(points_final[0], points_final[4])
            drawLine(points_final[1], points_final[5])
            drawLine(points_final[3], points_final[7])
            drawLine(points_final[2], points_final[6])

        if fill == True:
            faces = [n for n in range(6)]
            faces[0] = (points_final[0], points_final[1], points_final[3], points_final[2], white) 
            faces[1] = (points_final[0], points_final[6], points_final[2], points_final[4], red) 
            faces[2] = (points_final[0], points_final[1], points_final[4], points_final[5], blue) 
            faces[3] = (points_final[6], points_final[4], points_final[5], points_final[7], yellow) 
            faces[4] = (points_final[7], points_final[5], points_final[3], points_final[1], green) 
            faces[5] = (points_final[7], points_final[6], points_final[3], points_final[2], purple) 

            for face in faces:
                if points_final[furthest_pointID] not in face:
                    drawFace(face)

        angle_x += SPEED
        angle_y += SPEED
        angle_z += SPEED

        display_data(screen, rotated_points, furthest_point)


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_SPACE:
                if paused == True:
                    paused = False
                else:
                    paused = True

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_f:
                if fill == True:
                    fill = False
                else:
                    fill = True
            



    pygame.display.update()   
pygame.quit()