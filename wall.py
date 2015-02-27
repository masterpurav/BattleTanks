__author__ = 'Purav'
import pygame
import game_constants
from projectile import projectile, active_projectiles

class wall:
    wall_height = 0
    wall_width = 0
    wall_image = ""
    def __init__(self):
        self.wall_height = 350
        self.wall_width = 20
        self.wall_image = pygame.image.load("images/wall.jpg")

    def draw(self,surface):
        x = game_constants.scr_width/2-self.wall_width/2
        y = game_constants.scr_height-self.wall_height
        surface.blit(self.wall_image, (x,y),area=((x,y),(self.wall_width,self.wall_height)))

    def hit_wall(self):
        for x in active_projectiles:
            print (x.pos_x,x.pos_y)
            print (game_constants.scr_width/2+self.wall_width/2,game_constants.scr_height-self.wall_height)
            if(x.pos_y > game_constants.scr_height-self.wall_height and x.pos_x < game_constants.scr_width/2+self.wall_width/2 and x.pos_x > game_constants.scr_width/2 - self.wall_width/2):
                active_projectiles.remove(x)