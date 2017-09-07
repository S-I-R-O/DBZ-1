#IMPORTING MODULES
import pygame
from pygame.locals import *
import sys
import time
import pyganim

#Images of goku
goku_icon = pygame.image.load('Images/Resources/goku_icn.png')
#goku_icon = pygame.transform.scale2x(goku_icon)
goku_hp = pygame.image.load('Images/Resources/goku_hp.png')
goku_stay = pygame.image.load('Images/Move_Char/dbz_goku_stay.001.png')
goku_stay = pygame.transform.scale2x(goku_stay)
goku_bomb = pygame.image.load('Images/Attack_Bomb/dbz_goku_bomb.009.png')
goku_bomb = pygame.transform.scale(goku_bomb,(180,170))
goku_shoot = pygame.image.load('Images/Goku/dbz_goku_shoot.005.png')
goku_shoot = pygame.transform.scale2x(goku_shoot)



#DEFINING CONSTANTS
UP = 'up'
DOWN = 'down'
LEFT = 'left'
RIGHT = 'right'

#DEFINING VARIABLES
#1.Goku Coordinates
xGoku = 70 
yGoku = 200

#2.Controlling Goku
gokuLeft = gokuRight = False
gokuDirection = LEFT

#3.Goku Size
gokuWidth, gokuHeight =goku_stay.get_size()

#4.Goku Attack Bool
goku_atk=False

#5.Goku Bomb Coordinates
xGokuBomb,yGokuBomb=xGoku+10,yGoku-10

#6.Goku Shoot Coordinates
xGokuShoot,yGokuShoot=xGoku+10,yGoku-10

#7.Goku HP
goku_hp_Rate=251







    
   


