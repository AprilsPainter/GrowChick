import pygame as py
import os

def show_mainscreen(screen, events):

    # 색상 설정
    WHITE = (255, 255, 255)
    YELLOW = (255, 196, 0)

    screen.fill(WHITE)

    # 디스플레이 너비, 높이 설정
    WIDTH, HEIGHT = screen.get_size()

    # 경로 설정
    btn_PLAY_path = os.path.join("assets", "ui", "icons", "button_play.png")
    font_path = os.path.join("assets", "ui", "fonts", "Paperlogy-8ExtraBold.ttf")

    # PLAY 버튼 이미지 로드
    btn_PLAY = py.image.load(btn_PLAY_path)
    btn_PLAY = py.transform.scale(btn_PLAY, (400, 400))
    btn_PLAY_rect = btn_PLAY.get_rect(center = (WIDTH // 2, HEIGHT * 2 / 3))

    # 폰트 & 텍스트 설정
    font = py.font.Font(font_path, 200)
    title_GrowChick = font.render("병아리를 키워라!", True , YELLOW)
    title_GrowChick_rect = title_GrowChick.get_rect(center = (WIDTH // 2, HEIGHT * 3 / 8))

    # PLAY 버튼, 타이틀 텍스트 화면에 그리기
    screen.blit(btn_PLAY, btn_PLAY_rect)
    screen.blit(title_GrowChick, title_GrowChick_rect)

    # PLAY 버튼 클릭 이벤트 루프
    for event in events:
        if event.type == py.MOUSEBUTTONDOWN:
            if btn_PLAY_rect.collidepoint(event.pos):
                print("추후 게임 시작 함수로 연결")
                
    py.display.update()