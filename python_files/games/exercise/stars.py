import pygame, random, sys
from pygame.locals import *

def creat_stars(settings, stars):
	star = Star()
	for x in range(settings.window_width // (5 * star.rect.width)):
		for y in range(settings.window_height // (5 * star.rect.height)):
			star = Star()
			star.rect.x = random.randint(0, settings.window_width)
			star.rect.y = random.randint(0, settings.window_height)
			stars.add(star)

def run():
	pygame.init()
	settings = Settings()
	window = pygame.display.set_mode((settings.window_width, settings.window_height), 0, 32)
	pygame.display.set_caption('Stars')

	stars = pygame.sprite.Group()
	creat_stars(settings, stars)
	
	

	while True:
		for event in pygame.event.get():
			if event.type == QUIT:
				pygame.quit()
				sys.exit()
		window.fill((255, 255, 255))
		stars.draw(window)
		pygame.display.flip()


class Settings():
	def __init__(self):
		self.window_width = 1200
		self.window_height = 600

class Star(pygame.sprite.Sprite):
	def __init__(self):
		super(Star, self).__init__()
		self.image = pygame.image.load('gameCharacter.png')
		random_number = random.randint(10, 30)
		self.image = pygame.transform.smoothscale(self.image, (random_number, random_number))
		self.rect = self.image.get_rect()

run()