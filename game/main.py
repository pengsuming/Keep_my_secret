import pygame
import sys
import os
import subprocess
from minigame import run_minigame

# Pygame 초기화 및 오디오 초기화
pygame.init()

screen_width = 1920
screen_height = 1080
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("메인화면")

# 이미지 경로 설정
image_dir = "images/main"
background = pygame.image.load(os.path.join(image_dir, "mainmenu.jpg"))

start_button_idle = pygame.image.load(os.path.join(image_dir,"START.png"))
start_button_hover = pygame.image.load(os.path.join(image_dir,"START.png"))
start_button_rect = start_button_idle.get_rect()
start_button_rect.x = int(screen_width * 0.62)
start_button_rect.y = int(screen_height * 0.7)

character_image = pygame.image.load(os.path.join(image_dir,"여주.png"))
character_rect = character_image.get_rect()
character_rect.x = int(screen_width * 0.6)
character_rect.y = int(screen_height * 0.05)

# 호감도 파일 읽기
def load_affection():
    try:
        with open("affection_values.txt", "r") as f:
            values = f.readline().strip().split(",")
            return [int(value) for value in values]
    except FileNotFoundError:
        return [0, 0, 0]

호감도_완자, 호감도_푸준, 호감도_두부 = load_affection()

# 남자 주인공 이미지와 설명 로드
male_characters = [
    {"image": "완자.png", "description": f"나만의 완자님    {호감도_완자}"},
    {"image": "푸준.png", "description": f"피규어 집착남 이푸준    {호감도_푸준}"},
    {"image": "두부.png", "description": f"카페인 중독자 한두부    {호감도_두부}"}
]

# 쓰레기 이미지
waste_image = pygame.image.load(os.path.join(image_dir,"waste.png"))

# 음소거 버튼 이미지 로드
mute_button_idle = pygame.image.load(os.path.join(image_dir, "mute_button.png"))
mute_button_hover = pygame.image.load(os.path.join(image_dir, "mute_button.png"))
mute_button_rect = mute_button_idle.get_rect()
mute_button_rect.x = screen_width - mute_button_rect.width - 200
mute_button_rect.y = 80

# 폰트 설정
font = pygame.font.SysFont("malgungothic", 30)

# 이미지 로드
for character in male_characters:
    character["image"] = pygame.image.load(os.path.join(image_dir,character["image"]))

# 배경 음악 로드 및 재생 함수
def play_background_music():
    bg_music_path = os.path.join("song", "startsong.mp3")
    try:
        if os.path.exists(bg_music_path):
            pygame.mixer.music.load(bg_music_path)
            pygame.mixer.music.play(-1)  # -1은 무한 반복
        else:
            print(f"음악 파일 '{bg_music_path}'이(가) 존재하지 않습니다. 배경 음악을 재생할 수 없습니다.")
    except pygame.error as e:
        print(f"음악 파일을 로드하거나 재생하는 도중 오류가 발생했습니다: {e}")

# 메인 루프
def main():
    music_playing = True  # 음악 재생 상태 변수
    running = True
    while running:
        # 이벤트 처리
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if waste_rect.collidepoint(event.pos):
                    pygame.quit()
                    run_minigame()
                    running = False
                    sys.exit()
                elif mute_button_rect.collidepoint(event.pos):
                    if music_playing:
                        pygame.mixer.music.pause()
                        music_playing = False
                    else:
                        pygame.mixer.music.unpause()
                        music_playing = True

        # 배경, 여주인공, 쓰레기통 이미지 표시
        screen.blit(background, (0, 0))
        screen.blit(character_image, character_rect)
        waste_rect = screen.blit(waste_image, (200, 60))

        # 남자 주인공 이미지와 설명 표시
        y_offset = 120
        x_offset = 300
        text_x_offset = 530
        image_text_gap = 10
        block_gap = -70
        for character in male_characters:
            screen.blit(character["image"], (x_offset, y_offset))
            description = font.render(character["description"], True, (0, 0, 0))
            screen.blit(description, (text_x_offset, y_offset+130 + image_text_gap))
            y_offset += character["image"].get_height() + block_gap

        # 버튼의 마우스 호버 처리
        mouse_pos = pygame.mouse.get_pos()
        if start_button_rect.collidepoint(mouse_pos):
            screen.blit(start_button_hover, start_button_rect)
        else:
            screen.blit(start_button_idle, start_button_rect)

        if music_playing:
            screen.blit(mute_button_idle, mute_button_rect)
        else:
            screen.blit(mute_button_hover, mute_button_rect)

        # 화면 업데이트
        pygame.display.flip()

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    play_background_music()  # 배경 음악 재생
    main()
