import pygame
from pygame.locals import *
import sys
import pyganim

pygame.init()

class Window(object):

	def __init__(self,width=800,height=400,caption="The Window"):
		self.width = width
		self.height = height
		self.window = pygame.display.set_mode((self.width,self.height))
		pygame.display.set_caption(caption)
		self.bg_image = pygame.image.load("Images/Resources/bg_default.jpg")
		self.bg_image = pygame.transform.scale(self.bg_image,(self.width,self.height))
		

	def setBackground(self,img):
		self.bg_image = pygame.image.load(img)
		self.bg_image = pygame.transform.scale(self.bg_image,(self.width,self.height))


class Player(object):

	def __init__(self,name='Char',pos=[0,0]):
		self.x = pos[0]
		self.y = pos[1]

		self.name = name

		self.state={'charge':True,'punch':False,'kick':False}

		self.anim = Animation()

	def getTrueKey(self):
		
		for k in self.state:
			if(self.state[k]):
				return k

	def setTrueKey(self,key):
		self.state[self.getTrueKey()]=False
		self.state[key] = True

	def playAnim(self):
		self.anim.anim_set[self.getTrueKey()].play()
		print('p')



class Animation(object):

	def __init__(self):

		self.anim_set={}
		
	def addAnim(self,animKey,animChar):

		imagesAndDurations = [('Images\chars\%s\Attacks\%s.%s.png' % (animChar,animKey, str(num).rjust(3, '0')),0.1) for num in range(1,5)]
		self.anim_set[animKey] = pyganim.PygAnimation(imagesAndDurations,loop=False)
		#Conductor=pyganim.PygConductor(self.anim_set)
		#Conductor=Conductor.scale2x()




class DBZ(object):

	def __init__(self):

		self.gameScreen = Window(caption="Dragon Ball Z")
		self.p1 = Player('Goku',[30,50])
		self.p2 = Player('Vegeta',[650,50])

	def update(self):

		self.gameScreen.setBackground('Images/Resources/bg_img.jpeg')
		self.p1.anim.addAnim('charge',self.p1.name)
		self.p1.anim.addAnim('punch',self.p1.name)
		self.p1.anim.addAnim('kick',self.p1.name)

		self.p2.anim.addAnim('charge',self.p2.name)
		self.p2.anim.addAnim('punch',self.p2.name)
		self.p2.anim.addAnim('kick',self.p2.name)


		#i = pygame.image.load('chr.png')
		#ix=0
		while True:
                        


			self.gameScreen.window.blit(self.gameScreen.bg_image,[0,0])
			self.p1.playAnim()
			self.p2.playAnim()
			for event in pygame.event.get():
				if event.type==QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
					pygame.quit()
					sys.exit()

				elif event.type == KEYDOWN:

					if event.key == K_a:
						self.p1.x-=50
						#ix-=50

					elif event.key == K_d:
						self.p1.x+=50
						#ix+=50

					elif event.key == K_RIGHT:
						self.p2.x+=50
						
					elif event.key == K_LEFT:
						self.p2.x-=50
						
					elif event.key == K_t:
						self.p1.setTrueKey('punch')

					elif event.key == K_r:
						self.p1.setTrueKey('kick')

					elif event.key == K_p:
						self.p2.setTrueKey('punch')

					elif event.key == K_o:
						self.p2.setTrueKey('kick')				

			#self.gameScreen.window.blit(i,[ix,0])

			self.p1.anim.anim_set[self.p1.getTrueKey()].blit(self.gameScreen.window,[self.p1.x,self.p1.y])
			self.p2.anim.anim_set[self.p2.getTrueKey()].blit(self.gameScreen.window,[self.p2.x,self.p2.y])
			pygame.display.flip()


Game = DBZ()
Game.update()


























