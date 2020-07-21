import pygame
from pygame.locals import *

class Player():
	def __init__(self, image, i_width, i_height, windowSurface):
		self.image = pygame.image.load(image)
		self.image = pygame.transform.scale(self.image, (i_width, i_height))
		self.rect = self.image.get_rect()
		self.windowSurface = windowSurface
		self.windowSurfaceRect = windowSurface.get_rect()

		self.rect.centery = self.windowSurfaceRect.centery
		self.rect.left = self.windowSurfaceRect.left

		self.shoot = False

		self.moveUp = False
		self.moveDown = False

	def move(self):
		if self.moveUp and self.rect.top > self.windowSurfaceRect.top:
			self.rect.centery -= 5
		if self.moveDown and self.rect.bottom < self.windowSurfaceRect.bottom:
			self.rect.centery += 5

	def blit(self):
		windowSurface.blit(self.image, self.rect)

class Bullet():
	def __init__(self, player, windowSurface):
		self.windowSurface = windowSurface
		self.rect = pygame.Rect(player.rect.right, player.rect.centery, 20, 10)
		self.color = (0, 0, 0)
		self.speed = 10

	def move(self):
		self.rect.centerx += self.speed

	def draw(self):
		pygame.draw.rect(self.windowSurface, self.color, self.rect)

def check_events(player, bullets):
	for event in pygame.event.get():
		if event.type == QUIT:
			pygame.quit()
		if event.type == KEYDOWN:
			if event.key == K_w:
				player.moveUp = True
			elif event.key == K_s:
				player.moveDown = True
			elif event.key == K_SPACE:
				player.shoot = True
		if event.type == KEYUP:
			if event.key == K_w:
				player.moveUp = False
			elif event.key == K_s:
				player.moveDown = False
			elif event.key == K_SPACE:
				player.shoot = False

def update_player(player):
	player.move()
	player.blit()

def update_bullets(player, frameCount, bullets, windowSurfaceRect):
	if player.shoot and (frameCount % 10 == 0):
		new_bullet = Bullet(player, windowSurface)
		bullets.append(new_bullet)

	for bullet in bullets[:]:
		bullet.move()
		if bullet.rect.left >= windowSurfaceRect.right:
			bullets.remove(bullet)
		else:
			bullet.draw()

def update_window(player, frameCount, bullets, windowSurface, windowSurfaceRect):
	windowSurface.fill((255, 255, 255))
	update_player(player)
	update_bullets(player, frameCount, bullets, windowSurfaceRect)
	pygame.display.flip()

pygame.init()
mainClock = pygame.time.Clock()
windowSurface = pygame.display.set_mode((1000, 500), 0, 32)
windowSurfaceRect = windowSurface.get_rect()
pygame.display.set_caption('Shoot On Left')
player = Player(image = 'gameCharacter.png', i_width = 50, i_height = 80, windowSurface = windowSurface)

bullets = []
frameCount = 0
while True:
	check_events(player, bullets)
	update_window(player, frameCount, bullets, windowSurface, windowSurfaceRect)
	if frameCount != 60:
		frameCount += 1
	else:
		frameCount = 1
	mainClock.tick(60)