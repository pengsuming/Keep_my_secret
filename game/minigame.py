import pygame
import random

def run_minigame():
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
    player_image = pygame.image.load('images/char/minichar.png')
    player_image = pygame.transform.scale(player_image, (player_width, player_height))

    # 쓰레기 설정
    waste_width = 30
    waste_height = 37
    waste_speed = 7
    waste = []

    # 쓰레기 이미지 로드 및 호감도 설정
    waste_images = [
        {"image": pygame.image.load('images/char/쓰레기1.png'), "score": 0, "character": "완자"},
        {"image": pygame.image.load('images/char/쓰레기2.png'), "score": 0, "character": "푸준"},
        {"image": pygame.image.load('images/char/쓰레기3.png'), "score": 0, "character": "두부"}
    ]
    for waste_data in waste_images:
        waste_data["image"] = pygame.transform.scale(waste_data["image"], (waste_width, waste_height))

    # 점수 표시용 작은 이미지 생성
    small_images = [pygame.transform.scale(waste_data["image"], (20, 20)) for waste_data in waste_images]

    # 폰트 설정
    font = pygame.font.SysFont("malgungothic", 20)

    # 제한 시간 설정
    time_limit = 20000  # 20초 (밀리초 단위)
    start_ticks = pygame.time.get_ticks()  # 시작 시간

    # 호감도 초기화
    favor = {"완자": 0, "푸준": 0, "두부": 0}

    # 점수 표시 함수
    def show_scores(waste_images):
        for i, waste_data in enumerate(waste_images):
            screen.blit(small_images[i], (10, 10 + i * 30))
            text = font.render(f": {waste_data['score']}", True, BLACK)
            screen.blit(text, (40, 10 + i * 30))

    # 게임 오버 화면 표시 함수
    def show_game_over():
        screen.fill(WHITE)
        total_score = sum(waste_data["score"] for waste_data in waste_images)
        if total_score <= 60:
            message = "쓰레기가 부족해...ㅠ 다시해야겠어"
        else:
            message = "쓰레기 다 모았다!!!!!!"

        text = font.render(message, True, RED)
        text_rect = text.get_rect(center=(screen_width // 2, screen_height // 2))
        screen.blit(text, text_rect)

        # 각 캐릭터의 호감도 표시
        favor_texts = [
            f"완자의 호감도가 올라갔습니다: {favor['완자']}",
            f"푸준의 호감도가 올라갔습니다: {favor['푸준']}",
            f"두부의 호감도가 올라갔습니다: {favor['두부']}"
        ]
        for i, favor_text in enumerate(favor_texts):
            text = font.render(favor_text, True, BLACK)
            text_rect = text.get_rect(center=(screen_width // 2, screen_height // 2 + 40 + i * 30))
            screen.blit(text, text_rect)

        # 종료 버튼
        button_text = font.render("종료", True, WHITE)
        button_rect = pygame.Rect(screen_width // 2 - 50, screen_height // 2 + 150, 100, 50)
        pygame.draw.rect(screen, RED, button_rect)
        screen.blit(button_text, (screen_width // 2 - 30, screen_height // 2 + 160))

        return button_rect

    # 게임 오버 함수
    def game_over():
        button_rect = show_game_over()
        pygame.display.flip()

        waiting_for_exit = True
        while waiting_for_exit:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if button_rect.collidepoint(event.pos):
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
        if random.randint(1, 4) <= 2:
            waste_x = random.randint(0, screen_width - waste_width)
            waste_data = random.choice(waste_images)
            waste.append({"rect": pygame.Rect(waste_x, 0, waste_width, waste_height), "data": waste_data})

        if random.randint(1, 50) == 1:  # 2% 확률로 한 번에 여러 개 생성
            for _ in range(random.randint(1, 2)):  # 1-2개의 쓰레기 추가 생성
                waste_x = random.randint(0, screen_width - waste_width)
                waste_data = random.choice(waste_images)
                waste.append({"rect": pygame.Rect(waste_x, 0, waste_width, waste_height), "data": waste_data})

        # 쓰레기 이동
        for trash in waste:
            trash["rect"].y += waste_speed
            if trash["rect"].y > screen_height:
                waste.remove(trash)

        # 충돌 감지
        player_rect = pygame.Rect(player_x, player_y, player_width, player_height)
        for trash in waste:
            if player_rect.colliderect(trash["rect"]):
                trash["data"]["score"] += 1
                favor[trash["data"]["character"]] += 1
                waste.remove(trash)

        # 화면 그리기
        screen.fill(WHITE)
        screen.blit(player_image, player_rect)
        for trash in waste:
            screen.blit(trash["data"]["image"], trash["rect"])

        show_scores(waste_images)
        pygame.display.flip()

        # 시간 확인
        elapsed_time = pygame.time.get_ticks() - start_ticks
        if elapsed_time >= time_limit:
            game_over()

        clock.tick(30)

    pygame.quit()
