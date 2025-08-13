# source/model/Items.py
from model.Chick import Chick

class FoodItem:
    def __init__(self, name, description, **effect):
        self.name = name
        self.description = description
        self.effect_stat = effect.keys()
        self.effect_amount = effect.values()
        self.chick = Chick()

    def eat(self):
        Chick.change_stat(self.chick, self.effect_stat, self.effect_amount)
        print(f"{self.name}을/를 먹음.")

    def get_name(self):
        return self.name
    
    def get_description(self):
        return self.description
    
    def get_effect_stat(self):
        return self.effect_stat
    
    def get_effect_amount(self):
        return self.effect_amount