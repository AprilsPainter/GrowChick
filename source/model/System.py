# source/model/System.py

from model.Chick import Chick

class System:
    def __init__(self):
        self.chick = Chick()
        self.day = Chick.get_day()
        self.actions_left = 5
        self.ending_flags = set()

    def use_action(self):
        if self.actions_left = 0:
            print("행동 횟수를 모두 소비함.")   # 임시
            return
        else:
            self.actions_left -= 1

    def pass_day(self):
        if self.actions_left > 0:
            print("잔여 행동 횟수가 존재함.")   # 임시
            return
        else:
            self.day += 1
            self.actions_left = 5

    def get_ending_flags(self):
        return self.ending_flags.copy()
    
    def add_ending_flgs(self, ending_key):
        self.ending_flags.add(ending_key)

system = System()