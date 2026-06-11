'''
Enemy and attack basics
'''
import pygame, sys

pygame.init()
screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()


def load_frames(paths,size=(40,40)):
    return  [pygame.transform.scale(pygame.image.load(p),size)for p in paths]

#player frame animation
idle_frames= load_frames(['idle/sprite-1-1.png','idle/sprite-1-2.png','idle/sprite-1-3.png','idle/sprite-1-4.png','idle/sprite-1-5.png','idle/sprite-1-6.png'])
#movement frames
run_frames =load_frames(['run/sprite-1-1.png','run/sprite-1-2.png','run/sprite-1-3.png','run/sprite-1-4.png','run/sprite-1-5.png','run/sprite-1-6.png']) 
jump_frames = load_frames(["jump/sprite-1-1.png","jump/sprite-1-2.png","jump/sprite-1-3.png","jump/sprite-1-4.png","jump/sprite-1-5.png","jump/sprite-1-6.png","jump/sprite-1-7.png","jump/sprite-1-8.png","jump/sprite-1-9.png","jump/sprite-1-10.png","jump/sprite-1-11.png","jump/sprite-1-12.png",])
#combat frames
attack1_frames =load_frames(['attack1/sprite-1-1.png','attack1/sprite-1-2.png','attack1/sprite-1-3.png','attack1/sprite-1-4.png','attack1/sprite-1-5.png','attack1/sprite-1-6.png','attack1/sprite-1-7.png','attack1/sprite-1-8.png'])
stab_frames = load_frames(["stab/sprite-1-1.png","stab/sprite-1-2.png","stab/sprite-1-3.png"])
attack2_frames = load_frames(["attack2/sprite-1-1.png","attack2/sprite-1-2.png","attack2/sprite-1-3.png","attack2/sprite-1-4.png"])

#enemy frame animation
enemyRun =  load_frames(['enemy/enemyRun/sprite-1-1.png','enemy/enemyRun/sprite-1-2.png','enemy/enemyRun/sprite-1-3.png','enemy/enemyRun/sprite-1-4.png','enemy/enemyRun/sprite-1-5.png','enemy/enemyRun/sprite-1-6.png','enemy/enemyRun/sprite-1-7.png','enemy/enemyRun/sprite-1-8.png'])
enemyHurt = load_frames(['enemy/enemyHurt/sprite-1-1.png','enemy/enemyHurt/sprite-1-2.png','enemy/enemyHurt/sprite-1-3.png'])

#player set up variables
player = pygame.Rect(100, 500,40,20) # starting position
vel_y = 0
on_ground = False
facing_right = True

#animation state
state = "idle" #could be either "idle" , "run","attack1","attack2" ,"stab","jump"
frame_index = 0.0
anim_spd = 0.15
jump = False


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
    moving = False
    if keys[pygame.K_LEFT]:  
        player.x -= 5
        facing_right = False
        moving = True
    if keys[pygame.K_RIGHT]: 
        player.x += 5
        facing_right = True
        moving = True
    if keys[pygame.K_SPACE] and on_ground:
        vel_y = -14
        on_ground = False
        jump = True

    if keys[pygame.K_a]:
        state = "attack1"
    elif keys[pygame.K_s]:
        state = "stab"
    elif keys[pygame.K_d]:
        state = "attack2"
    elif jump and moving:
        state = "jump"
    elif moving:
        state = "run"
    elif jump:
        state = "jump"
    else:
        state = "idle"

    frames = {"idle":idle_frames,"run":run_frames,"attack1":attack1_frames,"attack2":attack2_frames,"stab":stab_frames,"jump":jump_frames}[state]
    frame_index +=anim_spd
    if frame_index >= len(frames):
        frame_index = 0
        if state == "attack"or state == "stab" or state == "attack2" or state == "jump" :
            state = "idle"

    vel_y += 0.6
    player.y += int(vel_y)

    on_ground = False
    for p in platforms:
        if player.colliderect(p) and vel_y > 0:
            player.bottom = p.top
            vel_y = 0
            on_ground = True
            jump = False

    screen.fill((135, 206, 235))
    for p in platforms:
        pygame.draw.rect(screen, (200, 50, 50), p)
    frame = frames[int(frame_index)]
    if not facing_right:
        frame = pygame.transform.flip(frame,True,False)
    screen.blit(frame,player)    
    pygame.display.flip()
    clock.tick(50)
pygame.quit()