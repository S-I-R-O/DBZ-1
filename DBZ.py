#IMPORTING MODULES
import pygame
from pygame.locals import *
import sys
import time
import pyganim
from animations import *
from goku import *
from vegeta import *
from menu import *
import os


def single_match():
    
        
    try:
        import pygame
        from pygame.locals import *
        import sys
        import time
        import pyganim
        from animations import *
        from goku import *
        from vegeta import *
        
        

        pygame.init()                  


        
        WALKRATE = 15

        GameLoop=True

        gameClock = pygame.time.Clock()

        #SETTING UP THE WINDOW
        WINDOWWIDTH = 800
        WINDOWHEIGHT = 400
        window = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
        
                                         
        pygame.display.set_caption('DBZ')


        #Background
        BG = pygame.image.load('Images/Arena/BG005.png')
        BGM=pygame.mixer.Sound("Audio/BGM.wav")

        hp_box=pygame.image.load('Images/Resources/hp_box.png')

        
        collide_goku=False
        collide_vegeta=False
        #------------------------------

        goku_dead = False
        
        goku_borrow_time=xGoku
        vegeta_borrow_time=xVegeta

        vegeta_wins=0
        goku_wins=0
        

        goku_block=False
        vegeta_block=False

        #Audio files
        goku_aud_bomb=pygame.mixer.Sound("Audio/goku_bomb.wav")
        goku_aud_shoot=pygame.mixer.Sound("Audio/goku_shoot.wav")
        goku_aud_charge=pygame.mixer.Sound("Audio/goku_charge.wav")
        goku_aud_block=pygame.mixer.Sound("Audio/goku_block.wav")
        

        goku_aud_prepunch=pygame.mixer.Sound("Audio/goku_prepunch.wav")
        goku_aud_prekick=pygame.mixer.Sound("Audio/goku_prekick.wav")
        goku_aud_punch=pygame.mixer.Sound("Audio/goku_punch.wav")
        goku_aud_kick=pygame.mixer.Sound("Audio/goku_kick.wav")

        vegeta_aud_bomb=pygame.mixer.Sound("Audio/vegeta_bomb.wav")
        vegeta_aud_shoot=pygame.mixer.Sound("Audio/vegeta_shoot.wav")
        
        vegeta_aud_prepunch=pygame.mixer.Sound("Audio/vegeta_prepunch.wav")
        vegeta_aud_prekick=pygame.mixer.Sound("Audio/vegeta_prekick.wav")
        vegeta_aud_punch=pygame.mixer.Sound("Audio/vegeta_punch.wav")
        vegeta_aud_kick=pygame.mixer.Sound("Audio/vegeta_kick.wav")
        vegeta_aud_block=pygame.mixer.Sound("Audio/vegeta_block.wav")
       
        
                                    
        #BGM.play()
        
            #Game begins!!!!!
        
        while GameLoop:
            #Displaying some const. images
            window.blit(BG,[0,0])       
            window.blit(goku_icon,[20,0])
            window.blit(vegeta_icon,[WINDOWWIDTH-280,5])
            window.blit(hp_box,[WINDOWWIDTH-280-100,40])
            
            window.blit(hp_box,[150,40])

               
                

        #Event Handling Loop
            for event in pygame.event.get(): 

                if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
                    pygame.quit()
                    sys.exit()
                    
                elif event.type == KEYDOWN:
                    if event.key == K_a:
                        gokuLeft = True
                        gokuRight = False
                        gokuDirection = LEFT

                    elif event.key == K_d:
                        gokuRight = True
                        gokuLeft = False
                        gokuDirection = RIGHT

                    elif event.key == K_LEFT:
                        vegetaLeft = True
                        vegetaRight = False
                        vegetaDirection = LEFT 

                    elif event.key == K_RIGHT:
                        vegetaRight = True
                        vegetaLeft = False
                        vegetaDirection = RIGHT

        ###########################################################################################
                    elif event.key == K_r:
                        Attack_Bomb['dbz_goku_bomb'].play()
                        goku_aud_bomb.play()
                        goku_atk='bomb'

                    elif event.key == K_e:
                        Attack_Goku['dbz_goku_charge'].play()
                        goku_aud_charge.play()
                        goku_atk='charge'

                    elif event.key == K_q:
                        Attack_Goku['dbz_goku_punch'].play()
                        Hit_Goku['dbz_goku_ring'].play()
                        goku_aud_prepunch.play()
                        goku_atk='punch'

                    elif event.key == K_w:
                        Attack_Goku['dbz_goku_kick'].play()
                        Hit_Goku['dbz_goku_ring'].play()
                        goku_aud_prekick.play()
                        goku_atk='kick'

                    elif event.key == K_x:
                        Attack_Goku['dbz_goku_block'].play()
                        goku_aud_block.play()
                        goku_atk='block'
                        

                    elif event.key == K_s:
                        Attack_Goku['dbz_goku_shoot'].play()
                        Hit_Goku['dbz_goku_smoke'].play()
                        goku_aud_shoot.play()
                        goku_atk='shoot'

                    elif event.key == K_j:
                        Hit_Goku['dbz_goku_win'].play()
                        

        ###########################################################################################
                    elif event.key==K_RCTRL:
                        Attack_Bomb['dbz_vegeta_blast'].play()
                        vegeta_aud_bomb.play()
                        vegeta_atk='bomb'
                        
                    elif event.key==K_END:
                        Attack_Vegeta['dbz_vegeta_block'].play()
                        vegeta_aud_block.play()
                        vegeta_atk='block'
                        
                    elif event.key==K_PAGEDOWN:
                        Attack_Vegeta['dbz_vegeta_punch'].play()
                        Hit_Vegeta['dbz_vegeta_ring'].play()
                        vegeta_aud_prepunch.play()
                        vegeta_atk='punch'

                    elif event.key==K_PAGEUP:
                        Attack_Vegeta['dbz_vegeta_kick'].play()
                        Hit_Vegeta['dbz_vegeta_ring'].play()
                        vegeta_aud_prekick.play()
                        vegeta_atk='kick'
                    
                    elif event.key==K_RETURN:
                        Attack_Vegeta['dbz_vegeta_shoot'].play()
                        Hit_Vegeta['dbz_vegeta_smoke'].play()
                        vegeta_aud_shoot.play()
                        vegeta_atk='shoot'

                    elif event.key==K_HOME:
                        Attack_Vegeta['dbz_vegeta_charge'].play()
                        vegeta_atk='charge'

                    elif event.key==K_KP8:
                        Hit_Vegeta['dbz_vegeta_win'].play()
                        

                    
                        
                    
        ###################################################################################################


                if event.type == KEYUP:

                    if event.key == K_a:
                        gokuLeft = False
                        
                    elif event.key == K_d:
                        gokuRight = False

                    elif event.key == K_LEFT:
                        vegetaLeft = False

                    elif event.key == K_RIGHT:
                        vegetaRight = False
                    

                    

        ###########################################################################################                
            #Choosing Animation to be displayed for GOKU
              
            if gokuLeft or gokuRight:
                
                Move_Char['dbz_goku_zoop'].play()
                Move_Char['dbz_goku_flyback'].play()
               
                if gokuDirection == LEFT:
                    Move_Char['dbz_goku_flyback'].blit(window, (xGoku, yGoku))
                elif gokuDirection == RIGHT:
                    Move_Char['dbz_goku_zoop'].blit(window, (xGoku, yGoku))

                # Moving the Character
                
                gokuRate = WALKRATE

                if gokuLeft:
                    xGoku -= gokuRate
                    xGokuShoot -= gokuRate
                    xGokuBomb -= gokuRate
                    
                if gokuRight:
                    xGoku += gokuRate
                    xGokuShoot += gokuRate
                    xGokuBomb += gokuRate


            elif goku_atk == 'bomb':

                #Playing Animation
                Attack_Bomb['dbz_goku_bomb'].blit(window, (xGoku,yGoku))
                window.blit(goku_bomb,(xGokuBomb,yGokuBomb))
                xGokuBomb += 30
                if xGokuBomb > WINDOWWIDTH:
                    xGokuBomb = xGoku+20
                    
                    goku_atk = False

                #Detecting Collision
                if xVegeta-100<xGokuBomb<xVegeta:
                    Hit_Goku['dbz_goku_impact'].play()
                    collide_vegeta=True
                    
                    if vegeta_block!=True:
                        vegeta_hp_Rate -= 5
                    else:
                        vegeta_hp_Rate -= 1
                        
                    vegeta_block=False    
                    try:
                        vegeta_hp = pygame.transform.scale(vegeta_hp,(vegeta_hp_Rate,21))
                    except:
                        
                        print "goku wins"
                        goku_wins+=1
                        GameLoop=False
                if collide_vegeta:
                    Hit_Goku['dbz_goku_impact'].blit(window,(xVegeta,yVegeta))
                    


            elif goku_atk == 'charge':
                Attack_Goku['dbz_goku_charge'].blit(window, (xGoku,yGoku))
                goku_borrow_time += 30
                if goku_borrow_time > WINDOWWIDTH:
                    goku_borrow_time = xGoku
                    
                    goku_atk = False
                if xVegeta-30<goku_borrow_time<xVegeta:
                    
                    try:
                       goku_hp = pygame.transform.scale(goku_hp,(goku_hp_Rate,21))
                    except:
                        pygame.quit()
                        print "goku wins"
                    goku_hp_Rate += 4
                    
               
                
                
                
            elif goku_atk == 'kick':

                Attack_Goku['dbz_goku_kick'].blit(window, (xGoku,yGoku))
                goku_borrow_time += 40
                if goku_borrow_time > WINDOWWIDTH:
                    goku_borrow_time = xGoku
                    
                    goku_atk = False

            
                if abs((xVegeta-xGoku))<80:
                    Hit_Goku['dbz_goku_ring'].blit(window,(xVegeta,yVegeta))
                    goku_aud_kick.play()
                    
                    if vegeta_block!=True:
                        vegeta_hp_Rate -= 1
                        
                    vegeta_block=False    
                    try:
                        vegeta_hp = pygame.transform.scale(vegeta_hp,(vegeta_hp_Rate,21))
                    except:
                        pygame.quit()
                        print "goku wins"
                        goku_wins+=1

               
                    
                    
                    
                
                
            elif goku_atk == 'punch':
                Attack_Goku['dbz_goku_punch'].blit(window, (xGoku,yGoku))
                goku_borrow_time += 40 
                if goku_borrow_time > WINDOWWIDTH:
                    goku_borrow_time = xGoku
                    
                    goku_atk = False
                
            

                
                if abs((xVegeta-xGoku))<80:
                    Hit_Goku['dbz_goku_ring'].blit(window,(xVegeta,yVegeta))
                    goku_aud_punch.play()
                    if vegeta_block!=True:
                        vegeta_hp_Rate -= 1
                        
                    vegeta_block=False    
                    try:
                        vegeta_hp = pygame.transform.scale(vegeta_hp,(vegeta_hp_Rate,21))
                    except:
                        pygame.quit()
                        print "goku wins"
                        goku_wins+=1
                


            elif goku_atk == 'block':
                Attack_Goku['dbz_goku_block'].blit(window, (xGoku,yGoku))
                goku_block=True
                goku_borrow_time += 40
                if goku_borrow_time > WINDOWWIDTH:
                    goku_borrow_time = xGoku
                    
                    
                    goku_atk = False
                

            elif goku_atk == 'shoot':

                #Playing Animation
                Attack_Goku['dbz_goku_shoot'].blit(window, (xGoku,yGoku))
                window.blit(goku_shoot,(xGokuShoot,yGokuShoot))
                xGokuShoot += 40
                if xGokuShoot > WINDOWWIDTH:
                    xGokuShoot = xGoku+20
                    
                    goku_atk = False

                #Detecting Collision
                if xVegeta-80<xGokuShoot<xVegeta:
                    collide_vegeta=True
                    
                    if vegeta_block!=True:
                        vegeta_hp_Rate -= 3
                        
                    vegeta_block=False    
                    try:
                        vegeta_hp = pygame.transform.scale(vegeta_hp,(vegeta_hp_Rate,21))
                    except:
                        pygame.quit()
                        print "goku wins"
                        goku_wins+=1

                if collide_vegeta:
                    Hit_Goku['dbz_goku_smoke'].blit(window,(xVegeta,yVegeta))
                    

            
                
                    
                    
                

            else:
                
                Move_Char['dbz_goku_zoop'].stop()
                Move_Char['dbz_goku_flyback'].stop()
                
                window.blit(goku_stay,(xGoku,yGoku))
                

                

        ###########################################################################################
             #------------------------------   
            #Choosing Animation to be displayed for VEGETA
            if vegetaLeft or vegetaRight:
                
                Move_Char['dbz_vegeta_zoop'].play()
                Move_Char['dbz_vegeta_flyback'].play()

                if vegetaDirection == RIGHT:
                    Move_Char['dbz_vegeta_flyback'].blit(window, (xVegeta, yVegeta))
                elif vegetaDirection == LEFT:
                    Move_Char['dbz_vegeta_zoop'].blit(window, (xVegeta, yVegeta))
                
                vegetaRate = WALKRATE

                if vegetaLeft:
                    xVegeta -= vegetaRate
                    xVegetaShoot -= vegetaRate
                    xVegetaBomb -= vegetaRate
                if vegetaRight:
                    xVegeta += vegetaRate
                    xVegetaShoot += vegetaRate
                    xVegetaBomb += vegetaRate

            elif vegeta_atk == 'bomb':

                Attack_Bomb['dbz_vegeta_blast'].blit(window, (xVegeta,yVegeta))        
                window.blit(vegeta_bomb,(xVegetaBomb,yVegetaBomb))
                xVegetaBomb -= 30
                if xVegetaBomb < 0:
                    xVegetaBomb = xVegeta-20
                    vegeta_atk = False

                if xGoku<xVegetaBomb<xGoku+300:
                    
                    Hit_Vegeta['dbz_vegeta_impact'].play()
                    collide_goku=True
                    
                    if goku_block!=True:
                        goku_hp_Rate -= 5
                    else:
                        goku_hp_Rate -= 1
                        
                    goku_block=False                       
                    try:
                        goku_hp = pygame.transform.scale(goku_hp,(goku_hp_Rate,21))
                    except:
                        print "vegeta wins"
                        vegeta_wins+=1
                        goku_dead=True
                        
                        
                if collide_goku:
                    Hit_Vegeta['dbz_vegeta_impact'].blit(window,(xGoku,yGoku))
                    
                    
                    
                    

            elif vegeta_atk == 'charge':
                Attack_Vegeta['dbz_vegeta_charge'].blit(window, (xVegeta,yVegeta))
                vegeta_borrow_time -= 30
                if vegeta_borrow_time < 0:
                    vegeta_borrow_time = xVegeta
                    
                    vegeta_atk = False
                if xGoku+30>vegeta_borrow_time>xGoku:
                    
                    try:
                        vegeta_hp = pygame.transform.scale(vegeta_hp,(vegeta_hp_Rate,21))
                    except:
                        pygame.quit()
                        print "vegeta wins"
                        
                    vegeta_hp_Rate += 4
                    
            elif vegeta_atk == 'kick':
                Attack_Vegeta['dbz_vegeta_kick'].blit(window, (xVegeta,yVegeta))        
                
                vegeta_borrow_time -= 40
                if vegeta_borrow_time < 0:
                    vegeta_borrow_time = xVegeta
                    vegeta_atk = False

                
                if abs((xVegeta-xGoku))<80:
                    Hit_Vegeta['dbz_vegeta_ring'].blit(window,(xGoku,yGoku))
                    if goku_block!=True:
                        goku_hp_Rate -= 1
                        
                    goku_block=False    
                    try:
                        goku_hp = pygame.transform.scale(goku_hp,(goku_hp_Rate,21))
                    except:
                        pygame.quit()
                        print "vegeta wins"
                        vegeta_wins+=1
                    

            elif vegeta_atk == 'punch':
                Attack_Vegeta['dbz_vegeta_punch'].blit(window, (xVegeta,yVegeta))        
                
                vegeta_borrow_time -= 40
                if vegeta_borrow_time < 0:
                    vegeta_borrow_time = xVegeta
                    vegeta_atk = False

                
                if abs((xVegeta-xGoku))<80:
                    Hit_Vegeta['dbz_vegeta_ring'].blit(window,(xGoku,yGoku))
                    if goku_block!=True:
                        goku_hp_Rate -= 1
                        
                    goku_block=False
                    try:
                        goku_hp = pygame.transform.scale(goku_hp,(goku_hp_Rate,21))
                    except:
                        pygame.quit()
                        print "vegeta wins"
                        vegeta_wins+=1

            elif vegeta_atk == 'block':
                Attack_Vegeta['dbz_vegeta_block'].blit(window, (xVegeta,yVegeta))
                vegeta_block=True
                vegeta_borrow_time -= 40
                if vegeta_borrow_time < 0:
                    vegeta_borrow_time = xVegeta
                    
                    
                    vegeta_atk = False
                    
                    

            elif vegeta_atk == 'shoot':

                Attack_Vegeta['dbz_vegeta_shoot'].blit(window, (xVegeta,yVegeta))        
                window.blit(vegeta_shoot,(xVegetaShoot,yVegetaShoot))
                xVegetaShoot -= 50
                if xVegetaShoot< 0:
                    xVegetaShoot = xVegeta-10
                    vegeta_atk = False

                if xGoku<xVegetaShoot<xGoku+50:
                    collide_goku=True
                    if goku_block!=True:
                        goku_hp_Rate -=3
                        
                    goku_block=False
                    try:
                        goku_hp = pygame.transform.scale(goku_hp,(goku_hp_Rate,21))
                    except:
                        pygame.quit()
                        print "vegeta wins"
                        vegeta_wins+=1
                        
                if collide_goku:
                    Hit_Vegeta['dbz_vegeta_smoke'].blit(window,(xGoku,yGoku-10))
            

            
                    
            else:
                
                Move_Char['dbz_vegeta_zoop'].stop()
                Move_Char['dbz_vegeta_flyback'].stop()
                
                window.blit(vegeta_stay,(xVegeta,yVegeta))      
            
        ###########################################################################################
            window.blit(goku_hp,[156,43])

            
            window.blit(vegeta_hp,[WINDOWWIDTH-378,43])

            
            #Imaginary boundary of the window
            if xGoku < 0:
                xGoku = 0
            if xGoku > WINDOWWIDTH - gokuWidth:
                xGoku = WINDOWWIDTH - gokuWidth

            if xVegeta < 0:
                xVegeta = 0
            if xVegeta > WINDOWWIDTH - vegetaWidth:
                xVegeta = WINDOWWIDTH - vegetaWidth

            if goku_dead:
                Hit_Vegeta['dbz_vegeta_win'].play()
                goku_dead=False
                        
            Hit_Vegeta['dbz_vegeta_win'].blit(window,(xVegeta-55,yVegeta))
            
            
            
                
            
                
            gameClock.tick(24)
            pygame.display.update()
            
    except:
        global vegeta_wins
        global goku_wins
        
            






        

def tournament(matches):
    
    for i in range(1,matches+1):
        single_match()
        
    
    if vegeta_wins > goku_wins:
        print "Vegeta is the winner of the tournament"
        rematch=raw_input("Do you want a rematch (Y/N)")
        if rematch=="Y" or rematch=="y":
            mainmenu()
        if rematch=="N" or rematch=="n":
            print "Game over"
    elif vegeta_wins==goku_wins:
        print "Draw"
        rematch=raw_input("Do you want a rematch (Y/N)")
        if rematch=="Y" or rematch=="y":
            mainmenu()
        if rematch=="N" or rematch=="n":
            print "Game over"
    elif vegeta_wins < goku_wins:
        print "Goku is the winner of the tournament"
        rematch=raw_input("Do you want a rematch (Y/N)")
        if rematch=="Y" or rematch=="y":
            mainmenu()
        if rematch=="N" or rematch=="n":
            print "Game over"
        

def mainmenu():
    
        
    
    pygame.init()
    WINDOWWIDTH = 800
    WINDOWHEIGHT = 400
    window = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
    main_BG = pygame.image.load('Images/Resources/main_menu.png')

    window.blit(main_BG, (0, 0))
    pygame.display.flip()

    menu = cMenu(40, 500, 40, 8, 'vertical', 100, window,
                   [('Single match',1,None),
                    ('Tournament',2,None),
                    ('Credits', 3,None),
                    ('Readme',5,None),
                    ('Exit',4,None)])
    menu.set_unselected_color((100,0,0))
    
       
    menu.set_center(True, True)
     
    menu.set_alignment('center', 'center')
       
    state = 0
    prev_state = 1
     
    rect_list = []

      
    pygame.event.set_blocked(pygame.MOUSEMOTION)

    while 1:
        if prev_state != state:
            
            pygame.event.post(pygame.event.Event(EVENT_CHANGE_STATE, key = 0))
            prev_state = state

          
        e = pygame.event.wait()

        if e.type == pygame.KEYDOWN or e.type == EVENT_CHANGE_STATE:
            if state == 0:
                rect_list, state = menu.update(e, state)
            elif state == 1:
                single_match()
                state = 0
            elif state == 2:
                pygame.quit()
                matches=input("Enter number of matches")
                
                tournament(matches)
                state = 0
            elif state == 3:
                pygame.quit()
                print """-----------------------------------------------------------------
                            DRAGON BALL Z GAME


                        DEVELOPED BY: Rohith and Sivaneshwar @ Siro games


                        
                        All rights reserved


-------------- ----------------------------------------------------------------------"""
                state = 0
            elif state == 5:
                    pygame.quit()
                    os.startfile("READ_ME.txt")
                    state = 0
            else:
                print 'Exit!'
                pygame.quit()
                sys.exit()
       
        if e.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        
        pygame.display.update(rect_list)
    


        
vegeta_wins=0
goku_wins=0
mainmenu()

            
            
    
        



