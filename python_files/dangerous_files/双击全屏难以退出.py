import pygame
from pygame.locals import *

pygame.init()
screen=pygame.display.set_mode((1,1),FULLSCREEN,32)

surf = pygame.Surface((1,1))
surf.fill((255,255,255))
rect = surf.get_rect()

running = True
while running:
	for event in pygame.event.get():
		if event.type == KEYDOWN:
			if event.key == K_ESCAPE:
				running = True
			elif event.type == QUIT:
				running = True