class Chick:
    # 클래스 초기 상태 설정
    def __init__(self):
        self.day = 1
        self.stage = "egg"  # egg -> baby -> young -> grown -> chicken
        self.stats = {
            "tiredness": 50,
            "fullness": 50,
            "stress": 0,
            "happiness": 50,
            "cleanliness": 50
        }
        self.actions_left = 5
        self.ending_flags = set()

    # 스탯 값 변경(0 ~ 100)
    def update_stats(self, stat, amount):
        if stat in self.stats:
            self.stats[stat] = max(0, min(100, self.stats[stat] + amount))

    # 하루 넘기고 성장 단계 갱신
    def advance_day(self):
        if self.actions_left > 0:
            print("아직 더 행동할 수 있어요!")
            return
        
        self.day += 1
        self.actions_left = 5
        self.update_stage()

    # 일수에 따라 성장 단계 변경
    def update_stage(self):
        if self.day == 2:
            self.stage = "baby"
        elif self.day == 5:
            self.stage = "young"
        elif self.day == 9:
            self.stage = "grown"
        elif self.day == 16:
            self.stage - "chicken"

    # 행동 횟수 소모
    def use_action(self):
        if self.actions_left > 0:
            self.actions_left -= 1
            return True
        else:
            print("오늘은 더 행동할 수 없어요!")
            return False
        
    # 엔딩 조건용 스탯 순위(1, 2순위) 반환
    def check_ending(self):
        sorted_stats = sorted(self.stats.items(), key=lambda x : x[1], reverse=True)
        top1, top2 = sorted_stats[0][0], sorted_stats[1][0]
        return (top1, top2)
    
    # 현재 성장 단계 반환
    def get_stage(self):
        return self.stage
    
    # 현재 전체 스탯 값 반환
    def get_stats(self):
        return self.stats.copy()
    
    # 현재 남은 행동 횟수 반환
    def get_actions_left(self):
        return self.actions_left