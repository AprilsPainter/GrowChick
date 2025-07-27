# source/model/Chick.py

class Chick:
    def __init__(self):
        self.day = 1
        self.stage = "young"
        self.stats = {
            "happiness" : 50,
            "cleanliness" : 50,
            "fullness" : 50,
            "tiredness" : 30,
            "stress" : 0
        }
        self.actions_left = 5
        self.ending_flags = set()

    def change_stat(self, stat, amount):
        if stat in self.stats:
            self.stats[stat] = max(0, min(100, self.stats[stat] + amount))
    
    def use_action(self):
        if self.actions_left > 0:
            return True
        else:
            print("행동 횟수를 모두 소비하였습니다.")   # 임시
            return False
        
    def pass_day(self):
        if self.actions_left > 0:
            print("잔여 행동 횟수가 존재합니다.")   # 임시
            return
        self.day += 1
        self.actions_left = 5
        self.update_stage()

    def update_stage(self):
        if self.day == 1:
            self.stage = "baby"
        elif self.day == 5:
            self.stage = "kid"
        elif self.day == 10:
            self.stage = "grown"
        elif self.day == 14:
            self.stage = "chicken"
