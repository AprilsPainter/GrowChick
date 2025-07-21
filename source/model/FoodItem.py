class FoodItem:
    def __init__(self, name, affected_stat, amount, image):
        self.name = name
        self.affected_stat = affected_stat
        self.amount = amount
        self.image = image
    
    def apply(self, chick):
        chick.update_stats(self.affected_stat, self.amount)