import pygame, sys
from pygame.locals import *

pygame.init()
windowSurface = pygame.display.set_mode((500, 500), 0, 32)
pygame.display.set_caption('Blue Sky')

while True:
	for event in pygame.event.get():
		if event.type == QUIT:
			pygame.quit()
			sys.exit()

	windowSurface.fill((0, 0, 100))
	pygame.display.update()

