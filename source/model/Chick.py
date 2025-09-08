# source/model/Chick.py

from config import INITIAL_STATS, DAILY_DECAY, GROWTH_STAGES, GAME_OVER_ZERO_DAYS
from util.common import change_stat, daily_decay

class Chick:
    def __init__(self):
        self.day = 1
        self.stage = GROWTH_STAGES[1]           # day 1 기준 stage
        self.stats = INITIAL_STATS.copy()       # charm, fullness, happiness, cleanliness
        self.zero_days = {stat: 0 for stat in self.stats}  # 스탯 0 연속일수
        self.game_over = False

    def change_stat(self, stat, amount):        # 외부에서 스탯 올리기/내리기
        change_stat(self.stats, stat, amount)

    def end_of_day(self):                       # 하루가 지나면서 스탯 감소, # , 게임오버 체크
        daily_decay(self.stats, DAILY_DECAY)
        self.check_zero_stats()
        self.day += 1
        self.update_stage()

    def check_zero_stats(self):                 # 스탯 0일 연속 체크 후 게임오버 여부
        for stat, value in self.stats.items():
            if value == 0:
                self.zero_days[stat] += 1
                if self.zero_days[stat] >= GAME_OVER_ZERO_DAYS:
                    self.game_over = True
            else:
                self.zero_days[stat] = 0

    def update_stage(self):                     # 성장 단계 갱신
        applicable_days = [d for d in GROWTH_STAGES if d <= self.day]
        self.stage = GROWTH_STAGES[max(applicable_days)]

    def get_top_two_stats(self):                # 엔딩용: 가장 높은 두 스탯 반환
        sorted_stats = sorted(self.stats.items(), key=lambda x: x[1], reverse=True)
        return [sorted_stats[0][0], sorted_stats[1][0]]

    def get_stats(self):
        return self.stats

    def get_stage(self):
        return self.stage

    def get_day(self):
        return self.day
