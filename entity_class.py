from random import randint
from render import renderFog
import time

class Entity:
    def __init__(self, hp, time, atk_rate, atk, speed, range, pos_player):
        
        self.hp = hp
        self.time = time
        self.atk_rate = atk_rate
        self.atk = atk
        self.speed = speed
        self.range = range
        self.pos = (0, 0)
        
    
    def death(self):
        print('JORDAN T MORT')
        
        
            
    def decrease_hp(self , damage):
        self.hp -= damage
        if self.hp < 0 :
            self.hp = 0

    def attack(self, target, damage ):
        target.decrease_hp(damage)
    
    
    def tick(self):
        pass
    
    def freeze_time(self):
        pass
    
    
    
class Player(Entity):
    def __init__(self, hp, time, atk_rate, atk, speed, range, pos_player):
        super().__init__(hp, time, atk_rate, atk, speed, range, pos_player)
        
class Monster(Entity):
    def __init__(self, hp, time, atk_rate, atk, speed, range, pos_player):
        super().__init__(hp, time, atk_rate, atk, speed, range, pos_player)
        
class Caecior(Monster):
    def __init__(self, hp, time, atk_rate, atk, speed, range, pos_player):
        super().__init__(hp, time, atk_rate, atk, speed, range, pos_player)
        
    def attack(self, target, damage):
        super().attack(target, damage)
        self.activate_warfog()
    
    def activate_warfog(self):
        renderFog == True
        print("Warfog effect activated")
        time.sleep(15)
    
        
        
    
        
            
            
            
            
        
    
    
