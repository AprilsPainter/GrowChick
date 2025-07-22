# source/model/Walk.py

import random

class WalkEvent:
    def __init__(self, description, stat_change=None, item=None):
        self.description = description
        self.stat_change = stat_change or {}
        self.item = item

    def apply(self, chick):
        for stat, amount in self.stat_change.items():
            chick.update_stats(stat, amount)
        return self.description, self.item

class WalkManager:
    
    def __init__(self):
        self.locations = {
            "공원" : [
                WalkEvent("맑은 공기를 마시며 힐링했어요!",
                          {"happiness" : +20, "stress" : -15, "cleanliness" : -10}),

                WalkEvent("공원에서 행운의 네잎 클로버를 발견했어요!", 
                          {"happiness" : +15, "stress" : -5, "cleanliness" : -10},
                          item = "Four-leaf clover"),

                WalkEvent("비둘기 떼와 추격전을 벌였어요...",
                          {"happiness" : -10, "stress" : +20, "cleanliness" : -10})
            ],

            "뒷골목" : [
                WalkEvent("좁은 골목을 탐험하며 즐겁게 산책했어요!",
                          {"happiness" : +15, "stress" : -20, "cleanliness" : -15}),

                WalkEvent("길바닥에서 지렁이 친구들을 만났어요! *꿀꺽*",
                          {"happiness" : +10, "stress" : -10, "cleanliness" : -15},
                          item = "Earthworm"),
                
                WalkEvent("깡패 패거리가 시비를 걸었어요...",
                          {"happiness" : -15, "stress" : +25, "cleanliness" : -15}),
            ],

            "치킨집" : [
                WalkEvent("...")
            ]
        }

    def get_locations(self):
        return list(self.locations.keys())
    
    def walk(self, location, chick):
        if location not in self.locations:
            return f"{location}은/는 존재하지 않는 장소에요.", None
        else:
            event = random.choice(self.locations[location])
            return event.apply(chick)