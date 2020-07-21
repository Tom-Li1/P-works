import pygame, sys, copy
from pygame.locals import *

class RainDrop(pygame.sprite.Sprite):
	def __init__(self, settings):
		super(RainDrop, self).__init__()
		self.image = pygame.image.load('gameCharacter.png')
		self.image = pygame.transform.scale(self.image, (settings['raindrop_width'], settings['raindrop_height']))
		self.rect = self.image.get_rect()
		self.rect.bottom = 0
		self.settings = settings

	def update(self):
		self.rect.y += settings['draw_speed']

def creat_fleet(settings, raindrops):
	available_space_x = settings['window_width'] - (2 * settings['raindrop_width'])
	raindrop_number_x = int(available_space_x / (2 * settings['raindrop_width']))
	for raindrop_number in range(raindrop_number_x):
		raindrop = RainDrop(settings)
		raindrop.rect.x = settings['raindrop_width'] + 2 * settings['raindrop_width'] * raindrop_number
		raindrops.add(raindrop)

def delete_out_fleet(settings, raindrops):
	for raindrop in copy.copy(raindrops.sprites()):
		if raindrop.rect.top == settings['window_height']:
			raindrops.remove(raindrop)

def check_events(settings, raindrops):
	for event in pygame.event.get():
		if event.type == QUIT:
			pygame.quit()
			sys.exit()
		if event.type == COUNT:
			creat_fleet(settings, raindrops)

def update_window(settings, window, raindrops, mianClock):
	window.fill(settings['window_bg_color'])
	raindrops.update()
	raindrops.draw(window)
	pygame.display.flip()
	mianClock.tick(settings['FPS'])

settings = {
	'window_width':1600,
	'window_height':800,
	'window_bg_color':(255, 255, 255),
	'raindrop_width':100,
	'raindrop_height':160,
	'FPS':60,
	'draw_speed':10
}

pygame.init()

# 自定义计时事件
COUNT = pygame.USEREVENT + 1

# 每隔1秒发送一次自定义事件
pygame.time.set_timer(COUNT,1000)

window = pygame.display.set_mode((settings['window_width'], settings['window_height']), 0, 32)
pygame.display.set_caption('Raindrops')
mianClock = pygame.time.Clock()
raindrops = pygame.sprite.Group()
creat_fleet(settings, raindrops)

while True:
	check_events(settings, raindrops)
	delete_out_fleet(settings, raindrops)
	update_window(settings, window, raindrops, mianClock)