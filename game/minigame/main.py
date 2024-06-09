import pygame
import sys
import os

# 작업 디렉토리를 이미지 폴더로 변경
os.chdir("C:/Users/Win10/Downloads/renpy-8.2.1-sdk/Projects/ITShow/game/images/main")

pygame.init()

screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("메인화면")

background = pygame.image.load("mainmenu.jpg")

start_button_idle = pygame.image.load("START.png")
start_button_hover = pygame.image.load("START.png")
start_button_rect = start_button_idle.get_rect()
start_button_rect.x = int(screen_width * 0.6)
start_button_rect.y = int(screen_height * 0.75)

character_image = pygame.image.load("여주.png")
character_rect = character_image.get_rect()
character_rect.x = int(screen_width * 0.57)
character_rect.y = int(screen_height * 0.01)

# 남자 주인공 이미지와 설명 로드
male_characters = [
    {"image": "완자.png", "description": "내 남자친구 김완자"},
    {"image": "푸준.jpg", "description": "피규어 집착남 이푸준"},
    {"image": "두부.jpg", "description": "카페인 중독자 한두부"}
]

waste_image = pygame.image.load("waste.png")

# 폰트 설정
font = pygame.font.SysFont("malgungothic", 18)

# 이미지 로드
for character in male_characters:
    character["image"] = pygame.image.load(character["image"])


# 메인 루프
def main():
    running = True
    while running:
        # 이벤트 처리
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False


        # 배경 이미지 표시
        screen.blit(background, (0, 0))

        # 여주인공 이미지 표시
        screen.blit(character_image, character_rect)

        # 완자 위에 쓰레기 이미지 표시
        screen.blit(waste_image, (60, 17))

        # 남자 주인공 이미지와 설명 표시
        y_offset = 140
        x_offset = 100
        text_x_offset = 220
        image_text_gap = 10
        block_gap = 30
        for character in male_characters:
            screen.blit(character["image"], (x_offset, y_offset))
            description = font.render(character["description"], True, (0, 0, 0))
            screen.blit(description, (text_x_offset, y_offset + image_text_gap))
            y_offset += character["image"].get_height() + block_gap

        # 버튼의 마우스 호버 처리
        mouse_pos = pygame.mouse.get_pos()
        if start_button_rect.collidepoint(mouse_pos):
            screen.blit(start_button_hover, start_button_rect)
        else:
            screen.blit(start_button_idle, start_button_rect)

        # 화면 업데이트
        pygame.display.flip()

    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    main()
