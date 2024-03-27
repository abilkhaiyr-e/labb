import pygame

pygame.init()
screen = pygame.display.set_mode((550, 550)) 
clock = pygame.time.Clock()

x = 40
y = 40

running = True
while running:
    
    

    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        y = max(25, y - 20)
    if keys[pygame.K_DOWN]:
        y = min(550 - 25, y + 20)
    if keys[pygame.K_LEFT]:
        x = max(25, x - 20)
    if keys[pygame.K_RIGHT]:
        x = min(550 - 25, x + 20)
    screen.fill(('White'))  
    pygame.draw.circle(screen, ('Red'), (x, y), 25)  
    pygame.display.flip() 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False 
    clock.tick(60) 

pygame.quit()