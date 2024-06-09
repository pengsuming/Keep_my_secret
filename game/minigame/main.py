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

        # 버튼의 마우스 호버 처리
        mouse_pos = pygame.mouse.get_pos()
        if start_button_rect.collidepoint(mouse_pos):
            screen.blit(start_button_hover, start_button_rect)
        else:
            screen.blit(start_button_idle, start_button_rect)

        # 여주인공 이미지 표시
        screen.blit(character_image, character_rect)

        # 화면 업데이트
        pygame.display.flip()

    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    main()
