"""Scene 전환 관리"""

import pygame as py
from source.scenes.title_scene import TitleScene
from source.scenes.living_room import LivingRoom

def main():
    """메인 루프: 현재 씬 실행 및 씬 전환 관리"""

    screen = py.display.set_mode((1920, 1080), py.FULLSCREEN)
    py.display.set_caption("Grow Chick!")

    current_scene_name = "title"

    while True:
        if current_scene_name == "quit":
            print("[종료] 'quit' 씬으로 이동하여 종료되었습니다.")
            break

        # 씬 객체 생성
        if current_scene_name == "title":
            scene = TitleScene(screen)
        elif current_scene_name == "living room":
            scene = LivingRoom(screen)
        else:
            # 알 수 없는 씬 이름일 경우 종료
            print("[오류] 알 수 없는 Scene 이름입니다.")
            break

        # 씬 실행 후 다음 씬 결정
        current_scene_name = scene.run()

    py.quit()


if __name__ == "__main__":
    main()
