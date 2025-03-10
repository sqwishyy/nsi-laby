from labyrinthe import *
from pygame import *
from random import randint
from player.py import * 


class Level:
    
    def __init__(self, labyrinthe, player,exit_coordonnee,player_coordonnee):
        self.labyrinthe = labyrinthe
        self.player = player
        self.enemies = []
        self.time_remaining = 1000 * 60 * 2
        self.exit_coordonnee = "a attendre"
        self.player_coordonnee = "a attendre"
        
    def enemies_spawn(self,enemies):
        pass
        
                
    def tick(self):
        while self.time_remaining > 0:
            if randint(0, 10) == 1:
                pass
                
    
    
    def timer_end(self):
        if self.time_remaining == 0:
            player.death
    
    def win():
        if self.player_coordonnee  == self.exit_coordonnee:
            print("win")
                
                
                
                
                
                
        
      
