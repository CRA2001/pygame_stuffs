import pygame, sys

pygame.init()
screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()

player = pygame.Rect(100, 500, 40, 40)
vel_y = 0
on_ground = False

platforms = [
    pygame.Rect(0, 560, 800, 40),   # floor
    pygame.Rect(100, 440, 150, 20),
    pygame.Rect(300, 360, 150, 20),
    pygame.Rect(500, 280, 150, 20),
]
running = True
while running:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit(); sys.exit()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:  player.x -= 5
    if keys[pygame.K_RIGHT]: player.x += 5
    if keys[pygame.K_SPACE] and on_ground:
        vel_y = -14
        on_ground = False

    vel_y += 0.6
    player.y += int(vel_y)

    on_ground = False
    for p in platforms:
        if player.colliderect(p) and vel_y > 0:
            player.bottom = p.top
            vel_y = 0
            on_ground = True

    screen.fill((135, 206, 235))
    for p in platforms:
        pygame.draw.rect(screen, (200, 50, 50), p)
    pygame.draw.rect(screen, (50, 200, 80), player)
    pygame.display.flip()
    clock.tick(50)
pygame.quit()