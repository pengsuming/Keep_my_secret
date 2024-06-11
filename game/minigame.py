import pygame
import random

def run_game():
    print("Minigame started")

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
    pygame.display.set_caption("쓰레기 줍기")

    # 플레이어 설정
    player_width = 50
    player_height = 50
    player_x = screen_width // 2
    player_y = screen_height - player_height - 10
    player_speed = 10

    # 쓰레기 설정
    waste_width = 50
    waste_height = 50
    waste_speed = 7
    waste = []

    # 쓰레기 이미지 로드
    waste_images = [
        pygame.image.load('images/char/쓰레기1.png'),
        pygame.image.load('images/char/쓰레기2.png'),
        pygame.image.load('images/char/쓰레기3.png'),
        pygame.image.load('images/char/쓰레기4.png'),
        pygame.image.load('images/char/쓰레기5.png')
    ]
    waste_images = [pygame.transform.scale(img, (waste_width, waste_height)) for img in waste_images]

    # 점수 설정
    score = 0
    font = pygame.font.SysFont("malgungothic", 40)

    # 제한 시간 설정
    time_limit = 20000  # 20초 (밀리초 단위)
    start_ticks = pygame.time.get_ticks()  # 시작 시간

    # 점수 표시 함수
    def show_score(score):
        text = font.render(f"Score: {score}", True, BLACK)
        screen.blit(text, (10, 10))

    # 게임 오버 함수
    def game_over():
        screen.fill(WHITE)
        if score <= 60:
            message = "쓰레기가 부족해...ㅠ 다시해야겠어"
        else:
            message = "쓰레기 다 모았다!!!!!!"

        text = font.render(message, True, RED)
        text_rect = text.get_rect(center=(screen_width // 2, screen_height // 2))
        screen.blit(text, text_rect)
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

        # 쓰레기 생성
        if random.randint(1, 10) <= 2:
            waste_x = random.randint(0, screen_width - waste_width)
            img = random.choice(waste_images)
            waste.append({"rect": pygame.Rect(waste_x, 0, waste_width, waste_height), "image": img})

        if random.randint(1, 10) == 1:  # 10% 확률로 한 번에 여러 개 생성
            for _ in range(random.randint(1, 3)):  # 1에서 5개의 쓰레기 추가 생성
                waste_x = random.randint(0, screen_width - waste_width)
                img = random.choice(waste_images)
                waste.append({"rect": pygame.Rect(waste_x, 0, waste_width, waste_height), "image": img})

        # 쓰레기 이동
        for trash in waste:
            trash["rect"].y += waste_speed
            if trash["rect"].y > screen_height:
                waste.remove(trash)

        # 충돌 감지
        player_rect = pygame.Rect(player_x, player_y, player_width, player_height)
        for trash in waste:
            if player_rect.colliderect(trash["rect"]):
                score += 1
                waste.remove(trash)

        # 화면 그리기
        screen.fill(WHITE)
        pygame.draw.rect(screen, BLACK, player_rect)
        for trash in waste:
            screen.blit(trash["image"], trash["rect"])

        show_score(score)
        pygame.display.flip()

        # 시간 확인
        elapsed_time = pygame.time.get_ticks() - start_ticks
        if elapsed_time >= time_limit:
            game_over()

        clock.tick(30)

    pygame.quit()

if __name__ == "__main__":
    run_game()
