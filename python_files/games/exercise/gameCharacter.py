import pygame, sys
from pygame.locals import *

class GameCharacter():
	def __init__(self, windowSurface, image):
		self.windowSurface = windowSurface
		self.image = image
		self.imageRect = image.get_rect()
		self.windowSurfaceRect = windowSurface.get_rect()

	def blitImage(self):
		self.imageRect.centerx = self.windowSurfaceRect.centerx
		self.imageRect.centery = self.windowSurfaceRect.centery
		self.windowSurface.blit(self.image, self.imageRect)

def check_events():
	for e in pygame.event.get():
		if e.type == QUIT:
			pygame.quit()
			sts.exit()

image = pygame.image.load('gameCharacter.png')
windowSurface = pygame.display.set_mode((500, 500), 0, 32)
pygame.display.set_caption('Game Character')
gameCharacter = GameCharacter(windowSurface, image)

while True:
	check_events()
	windowSurface.fill((255, 255, 255))
	gameCharacter.blitImage()
	pygame.display.update()