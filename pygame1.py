import pygame #need this import
pygame.init() #initializes the pygame class alongside the game
#setup
screen = pygame.display.set_mode((800,600))
pygame.display.set_caption("My first game")
clock = pygame.time.Clock()
#game loop
running = True
while running:
    #Events (input)
    for event in pygame.event.get():
        if event.type ==pygame.QUIT:
            running = False
    #update game logic
    screen.fill((0,0,0))
    pygame.display.update()
    clock.tick(60)
pygame.quit()