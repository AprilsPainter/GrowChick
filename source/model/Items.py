# source/model/Items.py
from model.Chick import Chick

class FoodItem:
    def __init__(self, name, description, **effect):
        self.name = name
        self.description = description
        self.effect = effect
        self.chick = Chick()

    def eat(self):
        for stat, amount in self.effect.items():
            self.chick.change_stat(stat, amount)
        print(f"{self.name}을/를 먹었다.")

    def get_name(self):
        return self.name
    
    def get_description(self):
        return self.description
    
    def get_effect(self):
        return self.effect
