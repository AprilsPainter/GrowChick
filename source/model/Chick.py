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

    def change_stat(self, stat, amount):
        if stat in self.stats:
            self.stats[stat] = max(0, min(100, self.stats[stat] + amount))

    def update_stage(self):
        if self.day == 1:
            self.stage = "baby"
        elif self.day == 5:
            self.stage = "kid"
        elif self.day == 10:
            self.stage = "grown"
        elif self.day == 14:
            self.stage = "chicken"

    def get_stats(self):
        return self.stats
    
    def get_stage(self):
        return self.stage
    
    def check_ending(self):
        sorted_stats = sorted(self.stats.items(), key=lambda x : x[1], reverse=True)
        top1, top2 = sorted_stats[0][0], sorted_stats[1][0]
        return (top1, top2)
    
    def get_day(self):
        return self.day
    
chick = Chick()