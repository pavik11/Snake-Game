# imports and initializing pygame
import pygame
from pygame.locals import *
import sys
pygame.init()

# variables for initializing the height and width of the game window
window_width = 800
window_height = 600

# displaying the window
screen = pygame.display.set_mode((window_width, window_height))
# giving a name to the window displayed
pygame.display.set_caption("Snake Game")

# Setting up different colors used in this game
red = (255, 0, 0) 
dark_green = (164, 232, 132)
light_green = (161, 255, 117)
blue = (94, 127, 235)


def draw_background():
    ''' This function draws the checkered board background using forloops to make the repeated squares'''
    # intitializing coordinate variables
    x = 0
    y = 0
    spacing = True

    # first for loop sets rows 
    for a in range(1,21):
        # second loop is for the columns
        for n in range(1, 15):
            pygame.draw.rect(screen, dark_green,(x ,y ,30 ,30))
            x = x + 60
        # if conditions check if squares shoud be spaced forward or not
        if spacing == False:
            x = 0
            spacing = True
        else:
            x = 30
            spacing = 0
        y = y + 30

snake_x = 300
snake_y = 300
flag = "none"
while True:
    screen.fill(light_green)
    # calling the draw background function
    draw_background()
    # drawing the snake
    snake=pygame.draw.rect(screen,blue,(snake_x,snake_y,30,30))

    # handling events
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.KEYDOWN:
            # changing the direction of snake based on key pressed
            if event.key == K_UP and flag != "down":
                flag = "up"
            if event.key == K_DOWN and flag != "up":
                flag = "down"
            if event.key == K_RIGHT and flag != "left":
                flag = "right"
            if event.key == K_LEFT and flag != "right":
                flag = "left" 
        else:
            # resetting the flag when key is released
            if event.type == pygame.KEYUP:
                flag = "none"
    
    # moving the snake in the direction based on flag value
    if flag == "up":
        snake_y = snake_y - 1
    if flag == "down":
        snake_y = snake_y + 1
    if flag == "right":
        snake_x = snake_x + 1
    if flag == "left":
        snake_x = snake_x - 1
    # quitting the window
    pygame.display.update()
    