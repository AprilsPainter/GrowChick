# source/model/System.py

from model.Chick import Chick

py.init()

class System:
    
    def __init__(self):

        self.chick = Chick()
        self.max_day = 16
        self.gameover = False
        self.ending = None
        self.zero_days = {
            "fullness": 0,
            "happiness": 0,
            "cleanliness": 0
        }

    def change_stat(self, stat: str, amount: int):

        stats = self.chick.stats

        stats[stat] += amount

        if stats[stat] < 0:
            stats[stat] = 0
        elif stats[stat] > 100:
            stats[stat] = 100

        self.chick.stats[stat] = stats[stat]

    def change_stage(self):

        day = self.chick.day
        stage = self.chick.stage

        if day == 1:
            stage = "egg"    
        elif 1 < day <= 4:
            stage = "newborn"
        elif 4 < day <= 8:
            stage = "young"
        elif 9 < day <= 15:
            stage = "grown"
        elif day == 16:
            stage = "chicken"
        
        self.chick.day = day
        self.chick.stage = stage

    def next_day(self)
        
        self.chick.day += 1

        for stat in self.chick.stats:
            self.chick.stats[stat] = max(0, self.chick.stats[stat] - 15)

    def zero_gameover(self):
        
        for stat in ["fullness", "happiness", "cleanliness"]:
            if self.chick.stats[stat] == 0:
                self.zero_days += 1
            else:
                self.zero_days = 0

            if self.zero_days >= 2:
                self.gameover = True
                self.ending = f"{stat} 값으로 인한 게임오버"
                
                return True
        return False