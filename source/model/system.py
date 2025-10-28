# source/model/system.py

from source.model.chick import Chick

class System:
    """게임 전반 시스템 관리 클래스"""

    def __init__(self):
        self.day = 1
        self.actions = 5
        self.chick = Chick()
        self.stats = self.chick.get_stats()

    def get_day(self):
        """외부에서 day 값 접근"""
        return self.day

    def pass_day(self):
        """다음날로 넘어감"""
        self.day += 1

    def get_actions(self):
        """외부에서 행동 횟수 접근"""
        return self.actions

    def use_action(self):
        """행동 횟수 사용"""
        self.actions -= 1

    def update_stat(self, stat, amount):
        """스탯 값 업데이트"""

        current_value = self.stats[stat]
        new_value = current_value + amount
        new_value = max(0, min(100, new_value))
        self.stats[stat] = new_value

    def get_stats(self):
        """외부에서 전체 스탯 딕셔너리 접근"""
        return self.stats

    def get_stat(self, stat):
        """외부에서 특정 스탯 값 접근"""
        return self.stats[stat]
