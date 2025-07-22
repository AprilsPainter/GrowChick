# source/model/GameManager.py

from model.Chick import Chick
from model.Walk import WalkManager

class GameManager:

    # 클래스 초기 상태 설정: 일수, 행동 횟수, 병아리, 엔딩 기록
    def __init__(self):
        self.day = 1
        self.actions_left = 5
        self.chick = Chick()
        self.ending_flags = set()
        self.walk_manager = WalkManager()

    # 행동 횟수 사용
    def use_action(self):
        if self.actions_left > 0:
            self.actions_left -= 1
            return True
        else:
            print("오늘은 더 행동할 수 없어요!")    # 임시
            return False

    # 다음날로 넘기고 성장 단계 갱신(수면)
    def advance_day(self):
        if self.actions_left > 0:
            print("아직 더 행동할 수 있어요!")  # 임시
            return False
        else:
            self.day += 1
            self.actions_left = 5
            self.chick.update_stage(self.day)
            return True
        
    # 병아리 스탯 변경
    def update_stat(self, stat, amount):
        self.chick.update_stats(stat, amount)    

    # 현재 일차 반환
    def get_day(self):
        return self.day

    # 현재 잔여 행동 횟수 반환
    def get_actions_left(self):
        return self.actions_left

    # 현재 병아리 성장 단계 반환
    def get_chick_stage(self):
        return self.chick.get_stage()

    # 현재 병아리 전체 스탯 값 반환
    def get_chick_stats(self):
        return self.chick.get_stats()

    # 봤던 엔딩 기록 반환
    def get_ending_flags(self):
        return self.ending_flags.copy()
    
    def get_walk_manager(self):
        return self.walk_manager

    # 엔딩 조건용 1, 2순위 스탯 종류 반환
    def check_ending(self):
        return self.chick.check_ending()

    # 본 엔딩 추가
    def add_ending_flag(self, ending_key):
        self.ending_flags.add(ending_key)

game_manager = GameManager()