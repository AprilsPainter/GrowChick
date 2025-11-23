# source/model/chick.py

import config

class Chick:
    """병아리 객체 클래스"""

    def __init__(self):
        self.stats = config.DEFAULT_STATS

    def get_stats(self):
        """외부에서 스탯 값 접근"""

        return self.stats
