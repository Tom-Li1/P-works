import pygame, sys, random
from pygame.locals import *

class Settings():
	def __init__(self):
		self.window_width = 1200
		self.window_height = 800
		self.window_bg_color = (255, 255, 255)

		self.player_width = 80
		self.player_height = 100
		
		self.goal_width = 80
		self.goal_height = 100
		self.goal_move_direction = 1 # 1 = down, -1 = up

		self.bullet_width = 30
		self.bullet_height = 15

		self.button_width = 200
		self.button_height = 50

		self.miss_limit = 10000000
		self.fps = 60

	def initSettings(self):
		self.player_speed = 5
		self.goal_speed = 5
		self.bullet_speed = 16

	def increaseSpeed(self):
		if self.player_speed <= 10:
			self.player_speed += random.randint(1, 3)

		self.goal_speed += 1
		self.bullet_speed += random.randint(1, 3)



class GameStats():
	def __init__(self, settings):
		self.settings = settings
		self.game_active = False
		self.miss_number = 0
		self.goal_hit = 0

	def resetGame(self):
		self.miss_number = 0
		self.game_active = True
		self.goal_hit = 0

class Goal():
	def __init__(self, settings, window_surface):
		self.settings = settings
		self.settings.goal_move_direction = random.choice([1, -1]) 

		self.window_surface = window_surface
		self.window_surface_rect = window_surface.get_rect()

		self.image = pygame.image.load('gameCharacter.png')
		self.image = pygame.transform.scale(self.image, (settings.goal_width, settings.goal_height))

		self.rect = self.image.get_rect()
		self.rect.right = self.window_surface_rect.right
		self.rect.top =  random.randint(0, settings.window_height - settings.goal_height)

	def update(self):
		self.rect.centery += settings.goal_speed * settings.goal_move_direction

	def check_edge(self):
		if self.rect.top <= self.window_surface_rect.top:
			self.settings.goal_move_direction = 1
		elif self.rect.bottom >= self.window_surface_rect.bottom:
			self.settings.goal_move_direction = -1

	def blitGoal(self):
		window_surface.blit(self.image, self.rect)

class Player():
	def __init__(self, settings, window_surface):
		self.settings = settings

		self.window_surface = window_surface
		self.window_surface_rect = window_surface.get_rect()

		self.image = pygame.image.load('gameCharacter.png')
		self.image = pygame.transform.scale(self.image, (settings.player_width, settings.player_height))

		self.rect = self.image.get_rect()
		self.rect.left = self.window_surface_rect.left
		self.rect.centery = self.window_surface_rect.centery

		self.moveUp = False
		self.moveDown = False

	def update(self):
		if self.moveUp and self.rect.top >= self.window_surface_rect.top:
			self.rect.centery -= self.settings.player_speed
		if self.moveDown and self.rect.bottom <= self.window_surface_rect.bottom:
			self.rect.centery += self.settings.player_speed

	def blitPlayer(self):
		window_surface.blit(self.image, self.rect)

class Bullet(pygame.sprite.Sprite):
	def __init__(self, settings, window_surface, player):
		super(Bullet, self).__init__()
		self.settings = settings
		self.window_surface = window_surface
		self.player = player

		self.rect = pygame.Rect(0, 0, settings.bullet_width, settings.bullet_height)
		self.rect.centery = player.rect.centery
		self.rect.right = player.rect.right

	def update(self):
		self.rect.right += self.settings.bullet_speed

	def drawBullet(self):
		pygame.draw.rect(self.window_surface, (0, 0, 0), self.rect)

class Button():
	def __init__(self, settings, window_surface, msg):
		self.settings = settings

		self.window_surface = window_surface
		self.window_surface_rect = window_surface.get_rect()

		self.msg = msg
		self.font = pygame.font.SysFont(None, 48)

		self.rect = pygame.Rect(0, 0, settings.button_width, settings.button_height)
		self.rect.center = self.window_surface_rect.center

		self.prep(msg)

	def prep(self, msg):
		self.msg_image = self.font.render(msg, True, (255, 255, 255), (0, 0, 0))
		self.msg_rect = self.msg_image.get_rect()
		self.msg_rect.center = self.rect.center

	def drawButton(self):
		self.window_surface.fill((0, 0, 0), self.rect)
		self.window_surface.blit(self.msg_image, self.msg_rect)



def checkKeyDownEvent(event, settings, window_surface, player, bullets):
	if event.key == K_q:
		pygame.quit()
		sys.exit()
	elif event.key == K_UP:
		player.moveUp = True
	elif event.key == K_DOWN:
		player.moveDown = True
	elif event.key == K_SPACE:
		bullets.add(Bullet(settings, window_surface, player))

def checkKeyUpEvent(event, player):
	if event.key == K_UP:
		player.moveUp = False
	elif event.key == K_DOWN:
		player.moveDown = False


def checkEvent(settings, window_surface, player, bullets, button, game_stats):
	for event in pygame.event.get():
		if event.type == QUIT:
			pygame.quit()
			sys.exit()
		elif event.type == KEYDOWN:
			checkKeyDownEvent(event, settings, window_surface, player, bullets)
		elif event.type == KEYUP:
			checkKeyUpEvent(event, player)
		elif event.type == MOUSEBUTTONDOWN:
			mouse_x, mouse_y = pygame.mouse.get_pos()
			if not game_stats.game_active and button.rect.collidepoint(mouse_x, mouse_y):
				startGame(game_stats, bullets, goal, player, settings)

def updateBullets(bullets, game_stats, goal, settings):
	bullets.update()
	for bullet in bullets.copy():
		if bullet.rect.left > settings.window_width:
			bullets.remove(bullet)
			game_stats.miss_number += 1
			if game_stats.miss_number > settings.miss_limit:
				game_stats.game_active = False

	if pygame.sprite.spritecollide(goal, bullets, True):
		game_stats.goal_hit += 1
		settings.increaseSpeed()


def updateScreen(settings, window_surface, player, goal, bullets, game_stats, button, font):
	window_surface.fill(settings.window_bg_color)
	player.blitPlayer()
	goal.blitGoal()
	for bullet in bullets:
		bullet.drawBullet()

	if not game_stats.game_active:
		button.drawButton()

	drawText('Score: ' + str(game_stats.goal_hit), font, window_surface, 0, 0)

	pygame.display.update()

def startGame(game_stats, bullets, goal, player, settings):
	game_stats.resetGame()
	settings.initSettings()
	bullets.empty()
	player.rect.centery = settings.window_height // 2
	settings.goal_move_direction = random.choice([1, -1])
	goal.rect.top =  random.randint(0, settings.window_height - settings.goal_height)

def drawText(text, font, surface, x, y):
	textobj = font.render(text, 1, (0, 0, 0))
	textrect = textobj.get_rect()
	textrect.topleft = (x, y)
	surface.blit(textobj, textrect)

pygame.init()
settings = Settings()
settings.initSettings()
window_surface = pygame.display.set_mode((settings.window_width, settings.window_height), 0, 32)
pygame.display.set_caption('Shotting Practice')
game_stats = GameStats(settings)
player = Player(settings, window_surface)
goal = Goal(settings, window_surface)
bullets = pygame.sprite.Group()
button = Button(settings, window_surface, 'Play')
main_clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 48)

#game_stats.resetGame()
while True:
	checkEvent(settings, window_surface, player, bullets, button, game_stats)

	if game_stats.game_active:
		player.update()
		goal.update()
		goal.check_edge()
		updateBullets(bullets, game_stats, goal, settings)

	updateScreen(settings, window_surface, player, goal, bullets, game_stats, button, font)
	main_clock.tick(settings.fps)