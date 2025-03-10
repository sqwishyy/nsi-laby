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
        
        return
    
    
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
        

        
        
    
        
            
            
            
            
        
    
    
