import pygame, sys
from pygame.locals import *

class Spirit():
	def __init__(self, spiritImage, windowSurface):
		self.spiritImage = spiritImage
		self.spiritRect = spiritImage.get_rect()
		self.windowSurface = windowSurface
		self.windowSurfaceRect = self.windowSurface.get_rect()

		self.spiritRect.center = self.windowSurfaceRect.center

		self.moveUp = False
		self.moveDown = False
		self.moveRight = False
		self.moveLeft = False

	def moveSpirit(self):
		if self.moveUp and self.spiritRect.top > self.windowSurfaceRect.top:
			self.spiritRect.centery -= 3
		if self.moveDown and self.spiritRect.bottom < self.windowSurfaceRect.bottom:
			self.spiritRect.centery += 3
		if self.moveRight and self.spiritRect.right < self.windowSurfaceRect.right:
			self.spiritRect.centerx += 3
		if self.moveLeft and self.spiritRect.left > self.windowSurfaceRect.left:
			self.spiritRect.centerx -= 3

	def blitSpirit(self):
		windowSurface.blit(self.spiritImage, self.spiritRect)

def checkEvents(spirit):
	for event in pygame.event.get():
		if event.type == QUIT:
			pygame.quit()
			sys.exit()
		if event.type == KEYDOWN:
			checkKeydownEvents(event, spirit)
		if event.type == KEYUP:
			checkKeyupEvents(event, spirit)

def checkKeydownEvents(event, spirit):
	if event.key == K_w:
		spirit.moveUp = True
	elif event.key == K_s:
		spirit.moveDown = True
	elif event.key == K_a:
		spirit.moveLeft = True
	elif event.key == K_d:
		spirit.moveRight = True

def checkKeyupEvents(event, spirit):
	if event.key == K_w:
		spirit.moveUp = False
	elif event.key == K_s:
		spirit.moveDown = False
	elif event.key == K_a:
		spirit.moveLeft = False
	elif event.key == K_d:
		spirit.moveRight = False

def updateScreen(windowSurface, spirit):
	windowSurface.fill((255, 255, 255))
	spirit.moveSpirit()
	spirit.blitSpirit()
	pygame.display.flip()

windowSurface = pygame.display.set_mode((500, 500), 0, 32)
pygame.display.set_caption("Movement of Spirit")
spiritImage = pygame.image.load('gameCharacter.png')
spiritImage = pygame.transform.scale(spiritImage, (60, 80))

spirit = Spirit(spiritImage, windowSurface)
mianClock = pygame.time.Clock()

while True:
	checkEvents(spirit)
	updateScreen(windowSurface, spirit)
	mianClock.tick(60)