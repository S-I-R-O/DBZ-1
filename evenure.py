import sys, pygame, random
from menu_lib import *
from credit import credit

class Player(pygame.sprite.Sprite):
	def __init__(self, *groups):
		super(Player, self).__init__(*groups)
		self.image = pygame.image.load('resources/catcher_left.png')
		self.rect = self.image.get_rect()
		self.rect.bottom = 452
		self.rect.left = 320

	def update(self):
		key = pygame.key.get_pressed()
		if key[pygame.K_LEFT]:
			self.rect.x -= 20
			self.image = pygame.image.load('resources/catcher_left.png')
			pygame.display.flip()
		if key[pygame.K_RIGHT]:
			self.rect.x += 20
			self.image = pygame.image.load('resources/catcher_right.png')
			pygame.display.flip()
		if self.rect.left < 0:
			self.rect.left = 0
		elif self.rect.right > 640:
			self.rect.right = 640

class Apple(object):
	def __init__(self):
		self.image = pygame.image.load('resources/apple.png')
		self.rect=self.image.get_rect()
		self.rect.top=0
		self.rect.left=0

	def draw(self, surface):
		surface.blit(self.image, (self.rect.left, self.rect.top))

	def update(self):
		if self.rect.top==0:
			self.rect.top += 18
			self.rect.left=random.randint(10, 630)
			global apple_count
			apple_count+=1
		elif self.rect.top!=0 and self.rect.top<480:
			self.rect.top+=18
		elif self.rect.top>=480:
			self.rect.top=0
def Gameover():
	clock = pygame.time.Clock()
	pygame.mixer.music.load('resources/gameover.mp3')
	pygame.mixer.music.play(-1, 0.0)
	pygame.mixer.music.set_volume(1)
	screen = pygame.display.set_mode((640, 480))
	s=pygame.Surface((640,480), pygame.SRCALPHA)
	bg = pygame.image.load('resources/gameover.jpeg')
	bg2 = pygame.image.load('resources/red.png')
	angry = pygame.image.load('resources/catcher_angry.png')
	angry = pygame.transform.scale(angry, (300, 300))
	dp=1

	while 1:
		clock.tick(5)

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				screen.fill((0,0,0))
				pygame.display.flip()
				pygame.mixer.music.stop()
				Mainmenu()
			if event.type == pygame.KEYDOWN and event.key != pygame.K_LEFT and event.key != pygame.K_RIGHT:
				screen.fill((0,0,0))
				pygame.display.flip()
				pygame.mixer.music.stop()
				Mainmenu()

		s.fill((255,0,0,128))
		screen.blit(s, (0,0))
		gameover=pygame.font.Font("resources/captureit.ttf", 50).render("GAME OVER!", 2, (255,255,255))
		screen.blit(bg, (0,0))
		screen.blit(bg2, (0,0))
		screen.blit(angry, (120,10))
		anykey=myfont.render("Press any key to return to main menu", 1, (255,255,255))
		screen.blit(anykey, (120,250))
		if dp==1:
			dp=0
			screen.blit(gameover, (180,190))
		elif dp==0:
			dp=1
		pygame.display.flip()

def Gamewin():
	clock = pygame.time.Clock()
	pygame.mixer.music.load('resources/win.mp3')
	pygame.mixer.music.play(-1, 0.0)
	pygame.mixer.music.set_volume(1)
	screen = pygame.display.set_mode((640, 480))
	s=pygame.Surface((640,480), pygame.SRCALPHA)
	bg = pygame.image.load('resources/gameover.jpeg')
	bg2 = pygame.image.load('resources/green.png')
	dp=1

	while 1:
		clock.tick(5)

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				screen.fill((0,0,0))
				pygame.display.flip()
				pygame.mixer.music.stop()
				Mainmenu()
			if event.type == pygame.KEYDOWN and event.key != pygame.K_LEFT and event.key != pygame.K_RIGHT:
				screen.fill((0,0,0))
				pygame.display.flip()
				pygame.mixer.music.stop()
				Mainmenu()

		s.fill((255,0,0,128))
		screen.blit(s, (0,0))
		gamewin=pygame.font.Font("resources/captureit.ttf", 50).render("You Win!", 2, (255,255,255))
		screen.blit(bg, (0,0))
		screen.blit(bg2, (0,0))
		anykey=myfont.render("Press any key to return to main menu", 1, (255,255,255))
		screen.blit(anykey, (120,250))
		if dp==1:
			dp=0
			screen.blit(gamewin, (210,190))
		elif dp==0:
			dp=1
		pygame.display.flip()

class Game(object):
	def main(self, screen):
		clock = pygame.time.Clock()
		background = pygame.image.load('resources/background.jpg')
		background = pygame.transform.scale(background, (640, 480))
		pygame.mixer.music.load('resources/bgmusic.mp3')
		pygame.mixer.music.play(-1, 0.0)
		pygame.mixer.music.set_volume(1)
		apple_count=0
		score=0
		chances=0
		sprites = pygame.sprite.Group()
		self.player = Player(sprites)
		apple = Apple()

		while 1:
			clock.tick(30)

			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					screen.fill((0,0,0))
					pygame.display.flip()
					pygame.mixer.music.stop()
					Mainmenu()
				if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
					screen.fill((0,0,0))
					pygame.display.flip()
					pygame.mixer.music.stop()
					Mainmenu()

			sprites.update()
			apple.update()
			if self.player.rect.colliderect(apple.rect):
				score+=1
				apple.rect.top=0
			screen.fill((200, 200, 200))
			screen.blit(background, (0, 0))
			sprites.draw(screen)
			apple.draw(screen)
			target_str=myfont.render("Target: 50", 1, (0,200,0))
			screen.blit(target_str, (350, 10))
			score_txt='Score: '+str(score)
			label = myfont.render(score_txt, 1, (255,0,0))
			screen.blit(label, (500, 10))
			global apple_count
			chances=(apple_count-1)-score
			if chances==0:
				chances_str="X X X X X"
			elif chances==1:
				chances_str="X X X X"
			elif chances==2:
				chances_str="X X X"
			elif chances==3:
				chances_str="X X"
			elif chances==4:
				chances_str="X"
			elif chances>=5:
				pygame.image.save(screen, "resources/gameover.jpeg")
				pygame.mixer.music.stop()
				Gameover()
			if score>=50:
				pygame.image.save(screen, "resources/gameover.jpeg")
				pygame.mixer.music.stop()
				Gamewin()
			chances_txt=myfont.render("Life: "+chances_str, 1, (255, 255, 255))
			screen.blit(chances_txt, (50,10))
			pygame.display.flip()


def Mainmenu():
	pygame.mixer.music.load('resources/main.mp3')
	pygame.mixer.music.play(-1, 0.0)
	pygame.mixer.music.set_volume(1)
	screen = pygame.display.set_mode((640, 480),pygame.FULLSCREEN)
	bkg=pygame.image.load('resources/bkg.jpg')
	screen.blit(bkg, (0, 0))
	pygame.display.flip()
	menu = cMenu(50, 50, 20, 5, 'vertical', 300, screen,
		   [('Start Game', 1, None),
			('Credits',    2, None),
			('Exit',       3, None)])

	menu.set_center(True, True)

	menu.set_alignment('center', 'center')

	state = 0
	prev_state = 1

	rect_list = []

	pygame.event.set_blocked(pygame.MOUSEMOTION)

	while 1:
		key = pygame.key.get_pressed()
		if key[pygame.K_ESCAPE]:
			pygame.quit()
			sys.exit()

		if prev_state != state:
		 pygame.event.post(pygame.event.Event(EVENT_CHANGE_STATE, key = 0))
		 prev_state = state

		e = pygame.event.wait()

		if e.type == pygame.KEYDOWN or e.type == EVENT_CHANGE_STATE:
		 if state == 0:
			rect_list, state = menu.update(e, state)
		 elif state == 1:
			 screen = pygame.display.set_mode((640, 480))
			 pygame.mixer.music.stop()
			 Game().main(screen)
		 elif state == 2:
			 pygame.mixer.music.stop()
			 credits()
		 else:
			pygame.mixer.music.stop()
			print 'Exit!'
			pygame.quit()
			sys.exit()

		if e.type == pygame.QUIT:
		 pygame.quit()
		 sys.exit()

		pygame.display.update(rect_list)

def credits():
	clock = pygame.time.Clock()
	pygame.mixer.music.load('resources/bgmusic.mp3')
	pygame.mixer.music.play(-1, 0.0)
	pygame.mixer.music.set_volume(1)
	screen=pygame.display.set_mode((640,480))
	screen.fill((0, 0, 0))
	me=pygame.image.load("resources/me.png")
	me=pygame.transform.scale(me, (200, 200))
	screen.blit(me, (440,280))
	text = "Credits \n _ _ _ _ _ _ _ _ _ _ _ _ \n\n\n Designer /n Creator /n/n Manikiran P"
	color = 0xa0a0a000
	credit(text,pygame.font.Font("resources/captureit.ttf", 32),color)
	screen.fill((0,0,0))
	pygame.display.flip()
	Mainmenu()
	while 1:
		clock.tick(30)

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				screen.fill((0,0,0))
				pygame.display.flip()
				Mainmenu()
			if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
				screen.fill((0,0,0))
				pygame.display.flip()
				Mainmenu()

		pygame.display.flip()


if __name__ == '__main__':
	pygame.init()
	screen=pygame.display.set_mode((640,480),pygame.FULLSCREEN)
	pygame.display.set_caption("Evenure - (c) Manikiran")
	myfont = pygame.font.Font("resources/captureit.ttf", 20)
	apple_count=0
	score=0
	Mainmenu()
