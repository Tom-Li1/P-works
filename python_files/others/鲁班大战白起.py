# class Aunt():
# 	def __init__(self,name,age):
# 		self.name = name
# 		self.age = age
# 	def make_cappuccino(self):
# 		print(f"{self.name} will make a cup of cappuccino for you.")

# amy = Aunt('Amy',50)
# amy.make_cappuccino()
# print(amy.age)
from random import randint
class Hero():
	def __init__(self,name,hp=100,ad=20):
		self.name = name
		self.hp	= hp
		self.ad = ad
	def attack(self,enemy):
		enemy.hp -= self.ad+randint(0,10)
	def show_hp(self):
		print(f'The HP of {self.name} is {self.hp}')
		if self.is_alive()==False:
			print(f'{self.name} is dead.')
	def is_alive(self):
		if self.hp>0:
			return True
		else:
			return False

luban = Hero('Lu Ban',hp=300,ad=50) 
baiqi = Hero('Bai Qi',hp=500,ad=20)
game_over = False
gameround = 0
while(game_over==False):
	gameround += 1
	if gameround%2 == 1:
		luban.attack(baiqi)
		if baiqi.is_alive()==False:
			game_over = True
		baiqi.show_hp()
	else:
		baiqi.attack(luban)
		if luban.is_alive()==False:
			game_over = True
		luban.show_hp()