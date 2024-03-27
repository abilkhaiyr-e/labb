import pygame

pygame.init()
clock = pygame.time.Clock()

screen = pygame.display.set_mode((500, 700))
pygame.display.set_caption("Yandex Music")

Yandex = pygame.image.load('C:/MyPythonProjects/TSIS/PyGame/files/tot.png')
Music = pygame.image.load('C:/MyPythonProjects/TSIS/PyGame/files/50.png')

Song1 = pygame.image.load('C:/MyPythonProjects/TSIS/PyGame/files/03.jpg')

image_list = [
    pygame.image.load('C:/MyPythonProjects/TSIS/PyGame/files/01.jpg'),
    pygame.image.load('C:/MyPythonProjects/TSIS/PyGame/files/02.jpg'),
    pygame.image.load('C:/MyPythonProjects/TSIS/PyGame/files/03.jpg'),
    pygame.image.load('C:/MyPythonProjects/TSIS/PyGame/files/04.jpg'),
    pygame.image.load('C:/MyPythonProjects/TSIS/PyGame/files/05.jpg'),
]
image_list2 = [
    pygame.image.load('C:/MyPythonProjects/TSIS/PyGame/files/001.jpg'),
    pygame.image.load('C:/MyPythonProjects/TSIS/PyGame/files/002.jpg'),
    pygame.image.load('C:/MyPythonProjects/TSIS/PyGame/files/003.jpg'),
    pygame.image.load('C:/MyPythonProjects/TSIS/PyGame/files/004.jpg'),
    pygame.image.load('C:/MyPythonProjects/TSIS/PyGame/files/005.jpg'),
]


song_list = [
    'C:/MyPythonProjects/TSIS/PyGame/files/01.mp3',
    'C:/MyPythonProjects/TSIS/PyGame/files/02.mp3',
    'C:/MyPythonProjects/TSIS/PyGame/files/03.mp3',
    'C:/MyPythonProjects/TSIS/PyGame/files/04.mp3',
    'C:/MyPythonProjects/TSIS/PyGame/files/05.mp3',
]

running = True
current_image_index = 2  # Установка начального изображения
current_song_index = 2    # Установка начальной песни

while running:
    screen.fill((255, 255, 255))
    keys = pygame.key.get_pressed()
    if keys[pygame.K_RETURN]:
        screen.blit(Music, (100, 200))
        screen.blit(Yandex, (30, 450))
        pygame.display.update()
        current_image_index = 0
        current_image = Song1
        pygame.mixer.music.stop()
        pygame.mixer.music.load(song_list[current_song_index])
        pygame.mixer.music.play()
        screen.blit(current_image, (0, 0))
        pygame.display.update()
    elif keys[pygame.K_LEFT]:
        current_song_index = (current_song_index - 1) % len(song_list)
        current_image_index = current_song_index
        current_image = image_list[current_image_index]
        pygame.mixer.music.stop()
        pygame.mixer.music.load(song_list[current_song_index])
        pygame.mixer.music.play()
        screen.blit(current_image, (0, 0))
        pygame.display.update()
    elif keys[pygame.K_RIGHT]:
        current_song_index = (current_song_index + 1) % len(song_list)
        current_image_index = current_song_index
        current_image = image_list[current_image_index]
        pygame.mixer.music.stop()
        pygame.mixer.music.load(song_list[current_song_index])
        pygame.mixer.music.play()
        screen.blit(current_image, (0, 0))
        pygame.display.update()
        
    elif keys[pygame.K_UP]:  # Остановить музыку
        pygame.mixer.music.pause()
        current_image = image_list2[current_image_index]
        screen.blit(current_image, (0, 0))
        pygame.display.update()
    elif keys[pygame.K_DOWN]:  # Возобновить музыку
        pygame.mixer.music.unpause()
        current_image = image_list[current_image_index]
        screen.blit(current_image, (0, 0))
        pygame.display.update()
    clock.tick(9)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()