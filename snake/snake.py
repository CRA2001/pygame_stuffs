'''
Author : Carlos Raniel Ariate Arro
Description: A basic game in pygame 
'''

#imports
import pygame
import random

#initialization of pygame
pygame.init()

#screen setup
#screen  width and height
w, h = 600, 600
#set up of screen with respect to w and h vars 
scrn = pygame.display.set_mode((w,h))
#caption of the game 
pygame.display.set_caption("Snake game")
#set of time and frame rate of game
clock = pygame.time.Clock()
#setup of background 
#----- DO THIS LATER -----
bg_image = pygame.image.load('snake/background.jpg').convert() #convert is used to speed up rendering process in pygame (after loading)
bg_image = pygame.transform.scale(bg_image,(w,h))
#setup of font
font = pygame.font.SysFont('Arial',32)
#render function of score
def draw_score(scrn,score_value):
    score_surface = font.render(f'Score: {score_value}',True,(255,255,255))
    scrn.blit(score_surface,(10,10))



#Grid 
CELL_SIZE = 20
#food sprite setup
food_img = pygame.image.load('snake/apple.png')
food_img = pygame.transform.scale(food_img,(20,20)) #resizing to fit grid of 20

#setting up eat sound
eat_sound = pygame.mixer.Sound('snake/eatSound.wav')

snake = [(300, 300)]
direction = (0, 0)
points = 0
# Food
food = (random.randrange(0, w, CELL_SIZE),
        random.randrange(0, h, CELL_SIZE))
running = True
while running:
    # EVENTS
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                direction = (0, -CELL_SIZE)
            if event.key == pygame.K_DOWN:
                direction = (0, CELL_SIZE)
            if event.key == pygame.K_LEFT:
                direction = (-CELL_SIZE, 0)
            if event.key == pygame.K_RIGHT:
                direction = (CELL_SIZE, 0)
    
    # UPDATE SNAKE
    if direction != (0, 0):
        head_x = snake[0][0] + direction[0]
        head_y = snake[0][1] + direction[1]
        new_head = (head_x, head_y)

        snake.insert(0, new_head)

        # FOOD COLLISION
        if new_head == food:
            food = (random.randrange(0, w, CELL_SIZE),
                    random.randrange(0, h, CELL_SIZE))
            points +=1
            eat_sound.play()
        else:
            snake.pop()

        # WALL COLLISION
        if (head_x < 0 or head_x >= w or
            head_y < 0 or head_y >= h):
            running = False

        # SELF COLLISION
        if new_head in snake[1:]:
            running = False

    # DRAW
    scrn.blit(bg_image,(0,0))

    # Draw snake
    for segment in snake:
        pygame.draw.rect(scrn, (0, 255, 0),
                         (*segment, CELL_SIZE, CELL_SIZE))

    # Draw food
    #pygame.draw.rect(scrn, (255, 0, 0),
    #                 (*food, CELL_SIZE, CELL_SIZE))
    scrn.blit(food_img,food)
    draw_score(scrn,points)
    pygame.display.update()
    clock.tick(10)  # slow = easier to understand

pygame.quit()