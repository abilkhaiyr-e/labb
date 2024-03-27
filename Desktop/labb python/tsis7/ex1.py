import pygame
from datetime import datetime
pygame.init()

clock = pygame.time.Clock()

screen = pygame.display.set_mode((1400, 1050))
pygame.display.set_caption("Abl")

bg_sound = pygame.mixer.Sound('C:\MyPythonProjects\TSIS\PyGame/files/444.mp3')
bg_sound.play()

icon = pygame.image.load('C:\MyPythonProjects\TSIS\PyGame/files/icon.png')
pygame.display.set_icon(icon)

bg = pygame.image.load('C:\MyPythonProjects\TSIS\PyGame/files/mainclock.png')
minute= pygame.image.load('C:\MyPythonProjects\TSIS\PyGame/files/rightarm.png')
second = pygame.image.load('C:\MyPythonProjects\TSIS\PyGame/files/leftarm.png')
rect = bg.get_rect(center=(700, 525))

myfont = pygame.font.Font('C:\MyPythonProjects\TSIS\PyGame/files/Ewert-Regular.ttf' , 30)
text_surface = myfont.render('Mickey Mouse Clock',True , 'Black')

running = True

while running:
    
    screen.blit(bg, (0, 0))
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
    
    time = datetime.now().time()
    sang = -(time.second * 6)
    news = pygame.transform.rotate(second, sang)
    sec_rect = news.get_rect(center=rect.center)
    screen.blit(news, sec_rect.topleft)
    
    mang = -(time.minute * 6) 
    newm = pygame.transform.rotate(minute, mang)
    min_rect = newm.get_rect(center=rect.center)
    screen.blit(newm, min_rect.topleft)
    
    screen.blit(text_surface , (1000,860))
    
    pygame.display.flip()