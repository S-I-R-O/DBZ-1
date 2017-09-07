#IMPORTING MODULES
import pygame
from pygame.locals import *
import sys
import time
import pyganim

#DEFINING CONSTANTS
UP = 'up'
DOWN = 'down'
LEFT = 'left'
RIGHT = 'right'

#Vegeta images
vegeta_icon = pygame.image.load('Images/Resources/vegeta_icn.png')
#vegeta_icon = pygame.transform.scale2x(vegeta_icon)
vegeta_hp = pygame.image.load('Images/Resources/vegeta_hp.png')
vegeta_hp=pygame.transform.flip(vegeta_hp,True,False)
vegeta_stay = pygame.image.load('Images/Move_Char/dbz_vegeta_stay.001.png')
vegeta_stay = pygame.transform.scale2x(vegeta_stay)
vegeta_bomb = pygame.image.load('Images/Attack_Bomb/dbz_vegeta_bomb.009.png')
vegeta_bomb = pygame.transform.scale(vegeta_bomb,(180,170))
vegeta_shoot = pygame.image.load('Images/Vegeta/dbz_vegeta_shoot.005.png')
vegeta_shoot = pygame.transform.scale2x(vegeta_shoot)

#1.Vegeta Coordinates
xVegeta = 380 
yVegeta = 200

#2.Controlling Vegeta
vegetaLeft = vegetaRight = False
vegetaDirection = RIGHT

#3.Vegeta Size
vegetaWidth, vegetaHeight = vegeta_stay.get_size()

#4.Vegeta Attack Bool
vegeta_atk=False

#5.Vegeta Bomb Coordinates
xVegetaBomb,yVegetaBomb = xVegeta-10,yVegeta-10

#6.Vegeta Shoot Coordinates
xVegetaShoot,yVegetaShoot = xVegeta-10,yVegeta+10

#7.Vegeta HP
vegeta_hp_Rate=250
