import pygame, sys, random
from pygame.locals import *

class Settings():
	def __init__(self):
		self.screen_width = 1200
		self.screen_height = 800
		self.bg_color = (255, 255, 255)
		
		self.player_speed_factor = 12
		self.player_side_length = 150

		self.ball_speed_factor = 10
		self.ball_side_length = 100
		self.ball_drop_speed = 10

		self.miss_limit = 3
		self.fps = 60

class GameStats():
	def __init__(self, settings):
		self.settings = settings
		self.game_active = True
		self.reset_stats()

	def reset_stats(self):
		self.miss_left = self.settings.miss_limit
		self.game_active = True


class Player():
	def __init__(self, settings, window_surface):
		self.settings = settings
		self.window_surface = window_surface

		self.image = pygame.image.load('gameCharacter.png')
		self.image = pygame.transform.scale(self.image, (settings.player_side_length, settings.player_side_length))

		self.rect = self.image.get_rect()
		self.rect.centerx = int(settings.screen_width / 2)
		self.rect.bottom = settings.screen_height

		self.moveLeft = False
		self.moveRight = False

	def update(self):
		if self.moveLeft and self.rect.left > 0:
			self.rect.centerx -= self.settings.player_speed_factor
		if self.moveRight and self.rect.right < self.settings.screen_width:
			self.rect.centerx += self.settings.player_speed_factor

	def blitPlayer(self):
		self.window_surface.blit(self.image, self.rect)

class Ball(pygame.sprite.Sprite):
	def __init__(self, settings, window_surface):
		super(Ball, self).__init__()
		self.settings = settings

		self.image = pygame.image.load('gameCharacter.png')
		self.image = pygame.transform.scale(self.image, (settings.ball_side_length, settings.ball_side_length))

		self.rect = self.image.get_rect()
		self.rect.x = random.randint(0, settings.screen_width - settings.ball_side_length) 
		self.rect.bottom = 0

	def update(self):
		self.rect.centery += self.settings.ball_speed_factor

def drawText(text, font, surface, x, y):
	textobj = font.render(text, 1, (0, 0, 0))
	textrect = textobj.get_rect()
	textrect.center = (x, y)
	surface.blit(textobj, textrect)

def waitForPlayerToPressKey():
	while True:
		for event in pygame.event.get():
			if event.type == QUIT:
				pygame.quit()
				sys.exit()
			if event.type == KEYDOWN:
				if event.key == K_ESCAPE:
					pygame.quit()
					sys.exit()
				return

def quitGame():
	pygame.quit()
	sys.exit()

def checkKeyDownEvents(player, event):
	if event.key == K_ESCAPE:
		quitGame()
	if event.key == K_a:
		player.moveLeft = True
	if event.key == K_d:
		player.moveRight = True

def checkKeyUpEvents(player, event):
	if event.key == K_a:
		player.moveLeft = False
	if event.key == K_d:
		player.moveRight = False

def checkEvents(player):
	for event in pygame.event.get():
		if event.type == QUIT:
			quitGame()
		elif event.type == KEYDOWN:
			checkKeyDownEvents(player, event)
		elif event.type == KEYUP:
			checkKeyUpEvents(player, event)

def checkRangeOut(balls, settings, stats):
	if stats.miss_left == 0:
		stats.game_active = False

	for ball in balls.sprites():
		if ball.rect.top >= settings.screen_height:
			balls.remove(ball)
			stats.miss_left -= 1
			return True
	return False

def checkCollision(player, balls, settings, window_surface, stats):
	ball_hit_player = pygame.sprite.spritecollideany(player, balls)
	if checkRangeOut(balls, settings, stats) or ball_hit_player:
		balls.remove(ball_hit_player)
		balls.add(Ball(settings, window_surface))

def updateBalls(balls, player, settings, window_surface):
	balls.update()
	checkCollision(player, balls, settings, window_surface, stats)

def updateScreen(settings, window_surface, player, balls, mian_clock, stats):
	window_surface.fill(settings.bg_color)
	player.update()
	updateBalls(balls, player, settings, window_surface)
	balls.draw(window_surface)
	player.blitPlayer()
	pygame.display.flip()
	mian_clock.tick(settings.fps)
	
pygame.init()
settings = Settings()
stats = GameStats(settings)
font = pygame.font.SysFont(None, 48)
screen = pygame.display.set_mode((settings.screen_width, settings.screen_height), 0, 32)
pygame.display.set_caption('Catch the Ball')
mian_clock = pygame.time.Clock()

while True:
	balls = pygame.sprite.Group()
	balls.add(Ball(settings, screen))
	player = Player(settings, screen)

	while True:
		checkEvents(player)

		if stats.game_active:
			updateScreen(settings, screen, player, balls, mian_clock, stats)
		else:
			drawText('GAME OVER', font, screen, screen.get_rect().center[0], screen.get_rect().center[1])
			pygame.display.flip()
			waitForPlayerToPressKey()
			stats.reset_stats()
			del balls
			del player			
			break

			