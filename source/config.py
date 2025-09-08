# source/config.py

# 스탯 범위
STAT_MIN = 0
STAT_MAX = 100

# 초기 스탯 값
INITIAL_STATS = {
    "charm": 50,
    "fullness": 50,
    "happiness": 50,
    "cleanliness": 50
}

# 하루 자연 감소량
DAILY_DECAY = {
    "charm": 2,
    "fullness": 5,
    "happiness": 3,
    "cleanliness": 4
}

# 성장 단계 기준
GROWTH_STAGES = {
    1: "egg",
    3: "newborn_chick",
    4: "young_chick",
    7: "grown_chick",
    16: "ending"
}

# 게임오버 기준: 연속 0일
GAME_OVER_ZERO_DAYS = 2
