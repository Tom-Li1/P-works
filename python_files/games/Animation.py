import pygame, sys, time
from pygame.locals import *

pygame.init()

WINDOWWIDTH = 800
WINDOWHEIGHT = 1000
windowSurface = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT), 0, 32)
pygame.display.set_caption('Animation')

DOWNLEFT = 'downleft'
DOWNRIGHT = 'downright'
UPLEFT = 'upleft'
UPRIGHT = 'upright'

MOVESPEED = 4

WHITE = (255, 255, 255)
RED = (225, 0, 0)
GREEN = (0, 225, 0)
BLUE = (0, 0, 225)

b1 = {'rect':pygame.Rect(300, 80, 50, 100), 'color':RED, 'dir':UPRIGHT}
b2 = {'rect':pygame.Rect(200, 200, 20, 20), 'color':GREEN, 'dir':UPLEFT}
b3 = {'rect':pygame.Rect(100, 150, 60, 60), 'color':BLUE, 'dir':DOWNLEFT}
b4 = {'rect':pygame.Rect(150, 300, 60, 60), 'color':RED, 'dir':DOWNLEFT}
b5 = {'rect':pygame.Rect(500, 150, 60, 60), 'color':GREEN, 'dir':DOWNLEFT}
b6 = {'rect':pygame.Rect(700, 470, 60, 60), 'color':BLUE, 'dir':DOWNLEFT}
b7 = {'rect':pygame.Rect(450, 290, 60, 60), 'color':RED, 'dir':DOWNLEFT}
b8 = {'rect':pygame.Rect(550, 400, 60, 60), 'color':GREEN, 'dir':DOWNLEFT}
b9 = {'rect':pygame.Rect(340, 700, 60, 60), 'color':BLUE, 'dir':DOWNLEFT}
b10 = {'rect':pygame.Rect(280, 620, 60, 60), 'color':RED, 'dir':DOWNLEFT}

boxes = [b1, b2, b3, b4, b5, b6, b7, b8, b9, b10]
mainClock = pygame.time.Clock()

while True:
	for event in pygame.event.get():
		if event.type == QUIT:
			pygame.quit()
			sys.exit()

	windowSurface.fill(WHITE)

	for b in boxes:
		if b['dir'] == DOWNLEFT:
			b['rect'].left -= MOVESPEED
			b['rect'].top += MOVESPEED
		if b['dir'] == DOWNRIGHT:
			b['rect'].left += MOVESPEED
			b['rect'].top += MOVESPEED
		if b['dir'] == UPLEFT:
			b['rect'].left -= MOVESPEED
			b['rect'].top -= MOVESPEED
		if b['dir'] == UPRIGHT:
			b['rect'].left += MOVESPEED
			b['rect'].top -= MOVESPEED

		if b['rect'].top < 0:
			if b['dir'] == UPLEFT:
				b['dir'] = DOWNLEFT
			if b['dir'] == UPRIGHT:
				b['dir'] = DOWNRIGHT
		if b['rect'].bottom > WINDOWHEIGHT:
			if b['dir'] == DOWNLEFT:
				b['dir'] = UPLEFT
			if b['dir'] == DOWNRIGHT:
				b['dir'] = UPRIGHT
		if b['rect'].left < 0:
			if b['dir'] == DOWNLEFT:
					b['dir'] = DOWNRIGHT
			if b['dir'] == UPLEFT:
					b['dir'] = UPRIGHT
		if b['rect'].right > WINDOWWIDTH:
			if b['dir'] == DOWNRIGHT:
					b['dir'] = DOWNLEFT
			if b['dir'] == UPRIGHT:
					b['dir'] = UPLEFT

		pygame.draw.rect(windowSurface, b['color'], b['rect'])

	pygame.display.update()
	mainClock.tick(60)
	