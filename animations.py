import pygame
from pygame.locals import *
import sys
import time
import pyganim

#-------------------------------------------------------------------------------------------------------------------------------
#ANIMATIONS - Mechanism: Nested Lists containing file names in a Dictionary
#1.Moving Goku/Vegeta
Move_Chars = 'dbz_goku_flyback dbz_goku_zoop dbz_vegeta_flyback dbz_vegeta_zoop '.split()
Move_Char = {}
for Char in Move_Chars:
    imagesAndDurations = [('Images\Move_Char\%s.%s.png' % (Char, str(num).rjust(3, '0')), 0.1) for num in range(1,5)]
    Move_Char[Char] = pyganim.PygAnimation(imagesAndDurations)

Move_Char_Conductor=pyganim.PygConductor(Move_Char)
Move_Char_Conductor=Move_Char_Conductor.scale2x()


#2.Bomb Animations
Attack_Bombs = 'dbz_goku_bomb dbz_vegeta_blast'.split()
Attack_Bomb = {}
for Bomb in Attack_Bombs:
    imagesAndDurations = [('Images\Attack_Bomb\%s.%s.png' % (Bomb, str(num).rjust(3, '0')), 0.1) for num in range(1,9)]
    Attack_Bomb[Bomb] = pyganim.PygAnimation(imagesAndDurations,loop=False)

Attack_Bomb_Conductor=pyganim.PygConductor(Attack_Bomb)
Attack_Bomb_Conductor=Attack_Bomb_Conductor.scale2x()


#3.1.Attack Vegeta
Attack_Vegetas = 'dbz_vegeta_shoot dbz_vegeta_kick dbz_vegeta_punch dbz_vegeta_block  dbz_vegeta_charge'.split()
Attack_Vegeta = {}
for Vegeta in Attack_Vegetas:
    imagesAndDurations = [('Images\Vegeta\%s.%s.png' % (Vegeta, str(num).rjust(3, '0')), 0.1) for num in range(1,5)]
    Attack_Vegeta[Vegeta] = pyganim.PygAnimation(imagesAndDurations,loop=False)

Attack_Vegeta_Conductor=pyganim.PygConductor(Attack_Vegeta)
Attack_Vegeta_Conductor=Attack_Vegeta_Conductor.scale2x()

#3.2.Hit Vegeta
Hit_Vegetas = 'dbz_vegeta_ring dbz_vegeta_smoke dbz_vegeta_impact dbz_vegeta_win'.split()
Hit_Vegeta = {}
for Vegeta in Hit_Vegetas:
    imagesAndDurations = [('Images\Vegeta_Hits\%s.%s.png' % (Vegeta, str(num).rjust(3, '0')),0.1) for num in range(1,5)]
    Hit_Vegeta[Vegeta] = pyganim.PygAnimation(imagesAndDurations,loop=False)

Hit_Vegeta_Conductor=pyganim.PygConductor(Hit_Vegeta)
Hit_Vegeta_Conductor=Hit_Vegeta_Conductor.scale2x()


#4.1.Attack Goku
Attack_Gokus = 'dbz_goku_charge dbz_goku_punch dbz_goku_kick dbz_goku_block dbz_goku_shoot'.split()
Attack_Goku = {}
for Goku in Attack_Gokus:
    imagesAndDurations = [('Images\Goku\%s.%s.png' % (Goku, str(num).rjust(3, '0')),0.1) for num in range(1,5)]
    Attack_Goku[Goku] = pyganim.PygAnimation(imagesAndDurations,loop=False)

Attack_Goku_Conductor=pyganim.PygConductor(Attack_Goku)
Attack_Goku_Conductor=Attack_Goku_Conductor.scale2x()

#4.2.Hit Goku
Hit_Gokus = 'dbz_goku_smoke dbz_goku_win dbz_goku_impact dbz_goku_ring'.split()
Hit_Goku = {}
for Goku in Hit_Gokus:
    imagesAndDurations = [('Images\Goku_Hits\%s.%s.png' % (Goku, str(num).rjust(3, '0')),0.1) for num in range(1,5)]
    Hit_Goku[Goku] = pyganim.PygAnimation(imagesAndDurations,loop=False)

Hit_Goku_Conductor=pyganim.PygConductor(Hit_Goku)
Hit_Goku_Conductor=Hit_Goku_Conductor.scale2x()






    



