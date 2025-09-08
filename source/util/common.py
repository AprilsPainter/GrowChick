# util/common.py

from config import STAT_MIN, STAT_MAX

def clamp_stat(value):                               # 스탯 값 0~100으로 제한
    return max(STAT_MIN, min(STAT_MAX, value))

def change_stat(stats_dict, stat_name, amount):      # 스탯을 증감시키고 clamp 적용
    if stat_name in stats_dict:
        stats_dict[stat_name] = clamp_stat(stats_dict[stat_name] + amount)

def daily_decay(stats_dict, decay_values):           # 하루 자연 감소 적용
    for stat, dec in decay_values.items():
        change_stat(stats_dict, stat, -dec)
