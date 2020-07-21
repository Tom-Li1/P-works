import pygame

pygame.init()
screen = pygame.display.set_mode((300, 300), 0, 32)
pygame.display.set_caption('Key Events')

while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
		elif event.type == pygame.KEYDOWN:
			print(event.key, ' DOWN')
		elif event.type == pygame.KEYUP:
			print(event.key, ' UP')

	screen.fill((230, 230, 230))
