import pygame, math
pygame.init()
W, H = 600, 400
screen = pygame.display.set_mode((W, H))
clock = pygame.time.Clock()

# --- state ---
x, y   = W / 2, H / 2
angle  = 0       # degrees, 0 = pointing right
speed  = 0
TURN   = 3       # deg/frame
ACCEL  = 0.3
MAX_SP = 6
DRAG   = 0.92

def draw_ship(surf, x, y, angle):
    # rotate a small triangle
    rad = math.radians(angle)
    pts = [
        (20, 0),   # nose
        (-12, 9),  # rear-left
        (-12, -9), # rear-right
    ]
    def rot(px, py):
        rx = px*math.cos(rad) - py*math.sin(rad)
        ry = px*math.sin(rad) + py*math.cos(rad)
        return x+rx, y+ry
    world = [rot(px, py) for px, py in pts]
    pygame.draw.polygon(surf, (99,210,255),
                          world, 2)

while True:
    for e in pygame.event.get():
        if e.type == pygame.QUIT: pygame.quit()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_a]: angle -= TURN
    if keys[pygame.K_d]: angle += TURN
    if keys[pygame.K_w]:
        speed = min(speed + ACCEL, MAX_SP)
    elif keys[pygame.K_s]:
        speed = max(speed - ACCEL, -MAX_SP/2)
    else:
        speed *= DRAG   # friction

    rad = math.radians(angle)
    x += math.cos(rad) * speed
    y += math.sin(rad) * speed
    x %= W; y %= H    # wrap screen edges

    screen.fill((13, 17, 23))
    draw_ship(screen, x, y, angle)
    pygame.display.flip()
    clock.tick(60)