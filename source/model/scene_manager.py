# source/model/scene_manager.py

class SceneManager:
    def __init__(self):
        self.current_scene = None  # 현재 활성 씬
        self.scenes = {}           # 씬 이름: 씬 객체

    def add_scene(self, name: str, scene_obj):
        """씬 등록"""
        self.scenes[name] = scene_obj

    def change_scene(self, name: str):
        """씬 전환"""
        if name in self.scenes:
            if self.current_scene:
                self.current_scene.on_exit()  # 이전 씬 종료 처리
            self.current_scene = self.scenes[name]
            self.current_scene.on_enter()   # 새 씬 진입 처리
        else:
            raise ValueError(f"Scene '{name}' not found!")

    def update(self, dt):
        """게임 루프에서 호출: 현재 씬 업데이트"""
        if self.current_scene:
            self.current_scene.update(dt)

    def draw(self, screen):
        """게임 루프에서 호출: 현재 씬 그리기"""
        if self.current_scene:
            self.current_scene.draw(screen)
