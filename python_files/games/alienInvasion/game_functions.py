import pygame, sys
from pygame.locals import *

def check_events():
	for event in pygame.event.get():
		if event.type == QUIT:
			pygame.quit()
			sys.exit()

def update_screen(ai_settings, screen, ship):
	screen.fill(ai_settings.bg_color)
	ship.blitme()
	pygame.display.flip()