import pygame
import random

# 게임 초기화
pygame.init()

# 색 정의
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# 화면 크기 설정
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("똥 피하기 게임")

# 플레이어 설정
player_width = 50
player_height = 50
player_x = screen_width // 2
player_y = screen_height - player_height - 10
player_speed = 10

# 똥 설정
poop_width = 50
poop_height = 50
poop_speed = 7
poops = []

# 점수 설정
score = 0
font = pygame.font.SysFont(None, 55)

# 점수 표시 함수
def show_score(score):
    text = font.render(f"Score: {score}", True, BLACK)
    screen.blit(text, (10, 10))

# 게임 오버 함수
def game_over():
    screen.fill(WHITE)
    text = font.render("Game Over", True, RED)
    screen.blit(text, (screen_width // 2 - 100, screen_height // 2 - 30))
    pygame.display.flip()
    pygame.time.wait(2000)
    pygame.quit()
    quit()

# 메인 게임 루프
running = True
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_x > 0:
        player_x -= player_speed
    if keys[pygame.K_RIGHT] and player_x < screen_width - player_width:
        player_x += player_speed

    # 똥 생성
    if random.randint(1, 20) == 1:
        poop_x = random.randint(0, screen_width - poop_width)
        poops.append(pygame.Rect(poop_x, 0, poop_width, poop_height))

    # 똥 이동
    for poop in poops:
        poop.y += poop_speed
        if poop.y > screen_height:
            poops.remove(poop)
            score += 1

    # 충돌 감지
    player_rect = pygame.Rect(player_x, player_y, player_width, player_height)
    for poop in poops:
        if player_rect.colliderect(poop):
            game_over()

    # 화면 그리기
    screen.fill(WHITE)
    pygame.draw.rect(screen, BLACK, player_rect)
    for poop in poops:
        pygame.draw.rect(screen, RED, poop)

    show_score(score)
    pygame.display.flip()
    clock.tick(30)

pygame.quit()