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
		self.bg_image = ''
		pygame.display.set_caption(caption)

	def setBackground(self,default="bg_default.jpg"):
		self.bg_image = pygame.image.load(default)
		self.bg_image = pygame.transform.scale(self.bg_image,(self.width,self.height))



class Player(object):

	def __init__(self):
		self.x = 0
		self.y = 0
		self.image = pygame.image.load("stay.001.png")

		self.state={'punch':False}

		self.animation = Animation()

	def playAnim(self):

		for k in self.state:
			if(k):
				self.animation.anim_set[k].play()

	def stopAnim(self):

		for k in self.state:
			if(k):
				self.animation.anim_set[k].stop()


	def endAnim(self):
		if (self.animation.borrow>800):
			for k in self.state:
				if(k):
					self.state[k]=False
					self.animation.borrow = 0

class Animation(object):

	def __init__(self):

		self.anim_set ={}
		self.anim_keys = []
		self.borrow = 0

	def addAnim(self,animKey):

		self.anim_keys.append(animKey)
		for key in self.anim_keys:
			imagesAndDurations = [('Images\Attacks\%s.%s.png' % (key, str(num).rjust(3, '0')),0.1) for num in range(1,5)]
			self.anim_set[key] = pyganim.PygAnimation(imagesAndDurations,loop=False)




class DBZ(Window):

	def __init__(self):
		Window.__init__(self,caption="Dragon Ball Z")
		self.player = Player()
		self.player.y = self.height - self.player.image.get_height()


	def Bound(self):
		if(self.player.x<0):
			self.player.x=0

	def update(self):

		self.setBackground('bg_img.jpeg')
		self.player.animation.addAnim('punch')
		self.player.animation.addAnim('kick')
		
        
		while True:

			self.window.blit(self.bg_image,[0,0])

			for event in pygame.event.get():
				if event.type==QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
					pygame.quit()
					sys.exit()

				elif event.type == KEYDOWN:

					if event.key == K_a:
						self.player.x-=50

					elif event.key == K_d:
						self.player.x+=50

					elif event.key == K_t:
						self.player.state['punch']=True
						#self.player.state['kick']=False

					elif event.key == K_r:
						self.player.state['kick']=True
						#self.player.state['punch']=False

					elif event.key == K_y:
						
						
						self.player.stopAnim()				

			self.player.playAnim()				
			for k in self.player.state:
				
				if(self.player.state[k]):
					self.player.animation.borrow+=40		
					self.player.animation.anim_set[k].blit(self.window,[self.player.x+100,self.player.y])
				self.player.endAnim()

			self.Bound()
			self.window.blit(self.player.image,[self.player.x,self.player.y])				
			pygame.display.update()


Game = DBZ()
Game.update()
