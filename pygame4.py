'''

'''


import pygame
import random

# Initialize pygame
pygame.init()

# Screen setup
w, h = 600, 600
scrn = pygame.display.set_mode((w, h))
pygame.display.set_caption("Snake Game")
clock = pygame.time.Clock()


def draw_exit_btn():
    #Button colors
    light, dark = (170,170,170),(100,100,100)
    #getting the button's position
    mouse = pygame.mouse.get_pos()
    #button dimensions
    bttnWidth,bttnHeight = 100, 40
    #button position
    b_pos_x = w -bttnWidth - 200
    b_pos_y = 250
    #checking if current mouse position is on top of the button
    is_over = (b_pos_x<=mouse[0]<=b_pos_x+bttnWidth and b_pos_y<=mouse[1]<=b_pos_y+bttnHeight)

    color = light if is_over else dark
    pygame.draw.rect(scrn,color,(b_pos_x,b_pos_y,bttnWidth,bttnHeight))
def draw_start_btn():
    pass

def show_menu():
    '''
    light = (170,170,170)
    dark = (100,100,100)
    mouse = pygame.mouse.get_pos()
    #button dimensions
    bttnWidth,bttnHeight = 100, 40
    #start button location
    startX, startY = 300, 300
    #exit button location
    exitX, exitY = 300,350 

    #checking if the cursor hovering on top of the respective buttons
    isOverStart = None
    isOverExit = None

    #drawing the buttons



    smallfont = pygame.font.SysFont("Corbell",35)
    titleText = smallfont.render("SNAKE GAME",True,white)
    titleRect = titleText.get_rect(center = (w//2,250))
    startText = smallfont.render("Start",True,white)
    startRect = startText.get_rect(center = (w//2,300))
    exitText = smallfont.render("Exit",True,white)
    exitRect = exitText.get_rect(center = (w//2,350))
    pygame.draw.rect(scrn,(111, 219, 99),titleRect.inflate(20,10))
    scrn.blit(titleText,titleRect)
    pygame.draw.rect(scrn,(111, 219, 99),startRect.inflate(20,10))
    scrn.blit(startText,startRect)
    pygame.draw.rect(scrn,(111, 219, 99),exitRect.inflate(20,10))
    scrn.blit(exitText,exitRect)
    '''

#button setup
def draw_button_reset():
    color_light = (170,170,170)
    color_dark = (100,100,100)
    mouse = pygame.mouse.get_pos()
    #button dimensions
    b_width = 100
    b_height = 40
    b_x = w- b_width - 10
    b_y = 10
    #if cursor hovering on top of button
    is_over = (b_x<=mouse[0]<=b_x+b_width and b_y<=mouse[1]<=b_y+b_height)
    #draw button
    color = color_light if is_over else color_dark
    pygame.draw.rect(scrn,color,(b_x,b_y,b_width,b_height))
    smallfont = pygame.font.SysFont('Corbel',35)
    text = smallfont.render('RESET?', True,(255,255,255))
    text_rect = text.get_rect(center=(b_x+b_width//2,b_y+b_height//2))
    scrn.blit(text,text_rect)

    return is_over and pygame.mouse.get_pressed()[0]

# Game variables
CELL_SIZE = 20
snake = [(300, 300)]
direction = (0, 0)
points = 0
food = (random.randrange(0, w, CELL_SIZE), random.randrange(0, h, CELL_SIZE))
show_reset = False 
# Font for score
font = pygame.font.SysFont('Arial', 32)

def draw_score(scrn, score_value):
    score_surface = font.render(f'Score: {score_value}', True, (255, 255, 255))
    scrn.blit(score_surface, (10, 10))

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    scrn.fill((0,0,0))
    menu = show_menu()
    pygame.display.update()
    clock.tick(10)

'''
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
            food = (random.randrange(0, w, CELL_SIZE), random.randrange(0, h, CELL_SIZE))
            points += 1
        else:
            snake.pop()

        # WALL COLLISION
        if (head_x < 0 or head_x >= w or head_y < 0 or head_y >= h):
            show_reset = True

        # SELF COLLISION
        if new_head in snake[1:]:
            running = False

    # DRAW
    scrn.fill((0, 0, 0))  # Black background
    
    # Draw snake
    for segment in snake:
        pygame.draw.rect(scrn, (0, 255, 0), (*segment, CELL_SIZE, CELL_SIZE))

    # Draw food
    pygame.draw.rect(scrn, (255, 0, 0), (*food, CELL_SIZE, CELL_SIZE))

    # Draw score

    draw_score(scrn, points)

    if show_reset:
        reset = draw_button_reset()
        if reset:
            snake = [(300,300)]
            direction = (0,0)
            points = 0
            food = (random.randrange(0,w,CELL_SIZE),random.randrange(0,h,CELL_SIZE))
            show_reset = False
    pygame.display.update()
    clock.tick(10)
'''
pygame.quit()