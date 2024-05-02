import pygame
import sys
import random
import psycopg2

pygame.init()

SCREEN_WIDTH, SCREEN_HEIGHT = 600, 400
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

snake_pos = [[100, 50], [90, 50], [80, 50]]
snake_speed = [10, 0]
food = {'pos': [0, 0], 'weight': 1, 'spawn_time': 0}
food_spawn = True
score = 0
level = 1
speed_increase = 0.1
food_counter = 0  

fps = pygame.time.Clock()
paused = False

def insert_score(name, score, level):
    conn = psycopg2.connect(dbname='postgres', user='postgres', password='qwerty', host='localhost', port='5432')
    cur = conn.cursor()
    insert_query = "INSERT INTO snake_game_scores (player_name, score, level) VALUES (%s, %s, %s)"
    cur.execute(insert_query, (name, score, level))
    conn.commit()
    cur.close()
    conn.close()

def get_scores(name):
    conn = psycopg2.connect(dbname='postgres', user='postgres', password='qwerty', host='localhost', port='5432')
    cur = conn.cursor()
    query = "SELECT score, level FROM snake_game_scores WHERE player_name = %s ORDER BY score DESC"
    cur.execute(query, (name,))
    results = cur.fetchall()
    cur.close()
    conn.close()
    return results

def get_player_name():
    input_rect = pygame.Rect(200, 200, 200, 32)
    color_active = pygame.Color('lightskyblue3')
    color_passive = pygame.Color('chartreuse4')
    color = color_passive
    active = False
    text = ''
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if input_rect.collidepoint(event.pos):
                    active = True
                else:
                    active = False
                color = color_active if active else color_passive
            if event.type == pygame.KEYDOWN:
                if active:
                    if event.key == pygame.K_RETURN:
                        return text
                    elif event.key == pygame.K_BACKSPACE:
                        text = text[:-1]
                    else:
                        text += event.unicode

        screen.fill((30, 30, 30))
        pygame.draw.rect(screen, color, input_rect, 2)
        font = pygame.font.Font(None, 32)
        text_surface = font.render(text, True, color)
        screen.blit(text_surface, (input_rect.x + 5, input_rect.y + 5))
        input_rect.w = max(200, text_surface.get_width() + 10)
        pygame.display.flip()
        fps.tick(30)

player_name = get_player_name()
player_name = player_name.encode('utf-8', 'ignore').decode('utf-8')
scores = get_scores(player_name)
if scores:
    print("Your previous scores:")
    for score, level in scores:
        print(f"Score: {score}, Level: {level}")
    sys.exit()  # Exit if scores are found

def check_collision(pos):
    if pos[0] < 0 or pos[0] > SCREEN_WIDTH - 10 or pos[1] < 0 or pos[1] > SCREEN_HEIGHT - 10:
        return True
    if pos in snake_pos[1:]:
        return True
    return False

def get_random_food():
    global food_counter
    while True:
        pos = [random.randrange(1, (SCREEN_WIDTH // 10)) * 10, random.randrange(1, (SCREEN_HEIGHT // 10)) * 10]
        if pos not in snake_pos:
            weight = 2 if food_counter >= 2 else 1
            food_counter = 0 if weight == 2 else food_counter + 1
            return {'pos': pos, 'weight': weight, 'spawn_time': pygame.time.get_ticks()}

try:
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP and snake_speed[1] == 0:
                    snake_speed = [0, -10]
                elif event.key == pygame.K_DOWN and snake_speed[1] == 0:
                    snake_speed = [0, 10]
                elif event.key == pygame.K_LEFT and snake_speed[0] == 0:
                    snake_speed = [-10, 0]
                elif event.key == pygame.K_RIGHT and snake_speed[0] == 0:
                    snake_speed = [10, 0]
                elif event.key == pygame.K_p:
                    paused = not paused


        if not paused:
            snake_pos.insert(0, list(map(lambda x, y: x + y, snake_pos[0], snake_speed)))

            if check_collision(snake_pos[0]):
                insert_score(player_name, score, level)
                pygame.quit()
                sys.exit()

            if snake_pos[0] == food['pos']:
                score += food['weight']
                if score % 3 == 0:
                    level += 1
                    fps.tick(10 + level * speed_increase)
                food_spawn = True
            else:
                snake_pos.pop()

            if food_spawn:
                food = get_random_food()
                food_spawn = False

            current_time = pygame.time.get_ticks()
            if current_time - food['spawn_time'] > 10000:
                food_spawn = True

        screen.fill(BLACK)
        for pos in snake_pos:
            pygame.draw.rect(screen, GREEN, pygame.Rect(pos[0], pos[1], 10, 10))

        food_color = RED if food['weight'] == 1 else (255, 165, 0)
        pygame.draw.rect(screen, food_color, pygame.Rect(food['pos'][0], food['pos'][1], 10, 10))

        font = pygame.font.SysFont('arial', 20)
        score_text = font.render(f"Score: {score} Level: {level}", True, WHITE)
        screen.blit(score_text, [0, 0])

        if paused:
            pause_text = font.render("Paused", True, WHITE)
            screen.blit(pause_text, [SCREEN_WIDTH // 2 - 30, SCREEN_HEIGHT // 2])

        pygame.display.flip()
        fps.tick(10 + level * speed_increase)
except SystemExit:
    pygame.quit()
