"""Scene 전환 및 공용 시스템 관리"""
# main.py

import pygame as py
from source.model.system import System
from source.model.status_window import StatusWindow
from source.scenes.title_scene import TitleScene
from source.scenes.living_room import LivingRoom

py.init()

def main():
    """메인 루프: 현재 씬 실행 및 전환 관리"""

    screen = py.display.set_mode((1920, 1080), py.FULLSCREEN)
    py.display.set_caption("Grow Chick!")

    system = System.get_instance()
    status_window = StatusWindow(screen, system)

    current_scene_name = "title"

    while True:

        if current_scene_name == "quit":
            print("[종료] 'quit' 씬으로 이동하여 게임이 종료됩니다.")
            break

        if current_scene_name == "title":
            current_scene = TitleScene(screen, system)

        elif current_scene_name == "living room":
            current_scene = LivingRoom(screen, system)

        else:
            print(f"[오류] 알 수 없는 씬 이름: {current_scene_name}")
            break

        # 현재 씬 루프 시작
        running = True
        clock = py.time.Clock()

        while running:
            for event in py.event.get():
                if event.type == py.QUIT:
                    running = False
                    current_scene_name = "quit"
                    break

                # 씬 내부 이벤트 처리
                current_scene.manage_event(event)

                # 타이틀 씬이 아닐 때만 스탯창 이벤트 활성
                if not isinstance(current_scene, TitleScene):
                    status_window.manage_event(event)

            current_scene.draw()

            # TitleScene이 아닐 때만 스탯창 표시
            if not isinstance(current_scene, TitleScene):
                status_window.draw()

            py.display.flip()
            clock.tick(60)

            # 씬 전환 요청 확인
            next_scene = current_scene.next_scene_name if hasattr(current_scene, "next_scene_name") else None
            if next_scene and next_scene != current_scene_name:
                current_scene_name = next_scene
                running = False

    py.quit()


if __name__ == "__main__":
    main()
