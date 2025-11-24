# source/model/base_scene.py


class BaseScene:
    def on_enter(self):
        """씬 시작 시 호출"""
    pass

    def on_exit(self):
        """씬 종료 시 호출"""
    pass

    def draw(self, screen):
        """프레임마다 그리기"""
    pass
