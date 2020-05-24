import pygame, sys
from pygame.locals import *
from bullet import Bullet

def check_keydown_events(event, ai_settings, screen, ship, bullets):
	if event.key == K_RIGHT:
		ship.moving_right = True
	elif event.key == K_LEFT:
		ship.moving_left = True
	elif event.key == K_SPACE:
		new_bullet = Bullet(ai_settings, screen, ship)
		bullets.add(new_bullet)

def check_keyup_events(event, ship):
	if event.key == K_RIGHT:
		ship.moving_right = False
	elif event.key == K_LEFT:
		ship.moving_left = False

def check_events(ai_settings, screen, ship, bullets):
	for event in pygame.event.get():
		if event.type == QUIT:
			pygame.quit()
			sys.exit()

		elif event.type == KEYDOWN:
			check_keydown_events(event, ai_settings, screen, ship, bullets)

		elif event.type == KEYUP:
			check_keyup_events(event, ship)
		
def update_screen(ai_settings, screen, ship, bullets):
	screen.fill(ai_settings.bg_color)
	for bullet in bullets.sprites():
		bullet.draw_bullet()
	ship.blitme()
	pygame.display.flip()