import pygame

class Cursor:
    def __init__(self, default_path, hover_path=None):
        self.default_img = pygame.image.load(default_path).convert_alpha()
        self.hover_img = pygame.image.load(hover_path).convert_alpha() if hover_path else self.default_img
        self.current_img = self.default_img
        pygame.mouse.set_visible(False)  # 기본 커서 숨기기
        self.hover_rects = []  # hover 시 이미지 변경 대상 rect 리스트

    def add_hover_rect(self, *rects):
        """
        여러 rect를 한 번에 등록 가능
        사용 예: add_hover_rect(button1.rect, button2.rect)
        또는 add_hover_rect(*list_of_rects)
        """
        for rect in rects:
            self.hover_rects.append(rect)

    def update(self, mouse_pos):
        """마우스 위치에 따라 현재 커서 이미지 결정"""
        self.current_img = self.default_img
        for rect in self.hover_rects:
            if rect.collidepoint(mouse_pos):
                self.current_img = self.hover_img
                break

    def draw(self, screen, mouse_pos):
        """현재 커서를 화면에 그림"""
        screen.blit(self.current_img, mouse_pos)
