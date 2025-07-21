class WalkEvent:
    def __init__(self, description, stat_change=None, item=None):
        self.description = description
        self.stat_change = stat_change or {}
        self.item = item

    def apply(self, chick):
        for stat, amount in self.stat_change.items():
            chick.update_stats(stat, amount)
        return self.description, self.item