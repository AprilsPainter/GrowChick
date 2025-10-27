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
