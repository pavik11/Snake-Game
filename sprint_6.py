# imports and initializing pygame
import random
import pygame
import time
from pygame.locals import QUIT, K_UP, K_DOWN, K_LEFT, K_RIGHT
import sys
pygame.init()

# variables for initializing the height and width of the game window
window_width = 810
window_height = 600

# displaying the window
screen = pygame.display.set_mode((window_width, window_height))
# giving a name to the window displayed
pygame.display.set_caption("Snake Game")

# Setting up different colors used in this game
red = (231, 71, 29) 
dark_green = (162, 209, 73)
light_green = (170, 215, 81)
blue = (70, 116, 233)
black = (0, 0, 0)
white = (255, 255, 255)
border_green = (68, 86, 32)

# setting up score varibale
score = 0

# loading the apple image and scaling it to fit the game
apple = pygame.image.load("apple.png")
apple = pygame.transform.scale(apple, (60, 45))

# loading the poison berry image and scaling it to fit the game
berry = pygame.image.load("berry.png")
berry = pygame.transform.scale(berry, (45, 45))


def show_text(msg, x, y, color, size):
    ''' this function displays text on the screen at given coordinates'''
    fontobj= pygame.font.SysFont("freesans", size)
    msgobj = fontobj.render(msg,False,color)
    screen.blit(msgobj,(x, y))

def draw_background(tile_size):
    ''' This function draws the checkered board background using forloops to make the repeated squares'''
    # intitializing coordinate variables
    x = 0
    y = 0
    spacing = True

    # first for loop sets rows 
    for a in range(1, 21):
        # second loop is for the columns
        for n in range(1, 15):
            pygame.draw.rect(screen, dark_green,(x ,y ,30 ,30))
            x = x + (tile_size * 2)
        # if conditions check if squares shoud be spaced forward or not
        if spacing == False:
            x = 0
            spacing = True
        else:
            x = tile_size
            spacing = 0
        y = y + tile_size
    
    pygame.draw.line(screen, border_green, (0,0), (0,600), 60)
    pygame.draw.line(screen, border_green, (0,600), (810,600), 60)
    pygame.draw.line(screen, border_green, (810,600), (810,0), 60)
    pygame.draw.line(screen, border_green, (810,0), (0,0), 120)

# initializing snake and apple positions
snake_x = 300
snake_y = 300
apple_x = 115
apple_y = 115
berry_x = 415
berry_y = 415

# initilizing apple rectangle for collision detection
apple_rect = apple.get_rect(topleft=(apple_x, apple_y))
flag = "none"

# initilizing apple rectangle for collision detection
berry_rect = berry.get_rect(topleft=(berry_x, berry_y))
flag2 = "none"

# setting up clock for controlling game speed
clock = pygame.time.Clock()

# initializing snake body list
body = [[snake_x, snake_y]]
snake_list = []

while True:

    ''' main game loop '''
    screen.fill(light_green)
    # calling the draw background function
    draw_background(30)

    # drawing the snake
    ate_apple = False
    ate_berry = False
    snake_head = None
    snake_list = []

    # display score
    show_text(str(score), 75, 20, white, 25)
    apple_display = pygame.image.load("apple.png")
    apple_display = pygame.transform.scale(apple_display, (60, 45))
    screen.blit(apple_display, (25, 10))

    # drawing the snake body
    for index, n in enumerate(body):
        # drawing each segment of the snake
        snake_body = pygame.draw.rect(screen, blue, (n[0], n[1], 30, 30))
        snake_list.append(snake_body)

        # setting the snake head for collision detection
        if index == 0:
            snake_head = snake_body
            
    # displaying apple and posion berry
    screen.blit(apple, apple_rect)
    screen.blit(berry, berry_rect)

    # checking for collision between snakec head and apple
    if snake_head and snake_head.colliderect(apple_rect):
        # respositioning apple to random grid spot of 30
        apple_x = random.randint(0, 25) * 30
        apple_y = random.randint(0, 18) * 30
        
        # updating score
        score += 1

        # updating apple rectangle position
        apple_rect.topleft = (apple_x+15, apple_y+15)
        ate_apple = True
        pygame.display.update()

    if snake_head and snake_head.colliderect(berry_rect):
        # respositioning apple to random grid spot of 30
        berry_x = random.randint(0, 25) * 30
        berry_y = random.randint(0, 18) * 30
        
        # updating score
        score -= 1

        body.pop()

        # updating berry rectangle position
        berry_rect.topleft = (berry_x+15, berry_y+15)
        ate_berry = True
        pygame.display.update()


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
    
    # moving the snake in the direction based on flag value
    if flag == "up":
        snake_y = snake_y - 30
    if flag == "down":
        snake_y = snake_y + 30
    if flag == "right":
        snake_x = snake_x + 30
    if flag == "left":
        snake_x = snake_x - 30

    # updating the snake body list
    body.insert(0, [snake_x, snake_y])

    # removing the last segment of the snake if apple not eaten
    if not ate_apple:
        body.pop()

    # checking for collision with top and bottom walls
    if snake_x>=800 or snake_x<=-30:
        screen.fill(black)
        show_text("End Game", 300, 300, white, 50)
        show_text("Final Score: "+str(score), 300, 400, white, 50)
        pygame.display.update()
        time.sleep(2)
        break

    # checking for collision with left and rightwalls
    if snake_y>=600 or snake_y<=-50:
        screen.fill(black)
        show_text("End Game", 300, 300, white, 50)
        show_text("Final Score: "+str(score), 300, 400, white, 50)
        pygame.display.update()
        time.sleep(2)
        break

    # checkig if score is less than 0
    if score < 0:
        screen.fill(black)
        show_text("End Game", 300, 300, white, 50)
        show_text("Score too low", 300, 400, white, 50)
        pygame.display.update()
        time.sleep(2)
        break

    # quitting the window
    pygame.display.update()

    # controlling the speed of the game
    clock.tick(13)
    