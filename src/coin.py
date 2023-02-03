import constants as con
import random
import pygame

class Coins:
	def __init__(self, surface, cells, player, enemy):
		self.inner = []
		self.prohibited = []
		self.surface = surface
		self.cells = cells
		self.player = player
		self.enemy = enemy

		self.prohibited.append((self.player.cur_x, self.player.cur_y))
		self.prohibited.append((self.enemy.x, self.enemy.y))
		self._generate_coins()
	
	def _generate_coins(self):
		for i in range(con.COINS_AMOUNT):
			x, y = 0, 0
			while self.cells.matrix[x][y].type not in 'g':
				x, y = random.randint(0, con.TILES_VERTICAL-1), random.randint(0, con.TILES_HORIZONTAL-1)
			if (x,y) not in self.prohibited:
				coin = Coin(x,y,self.cells.matrix[x][y])
				self.inner.append(coin)
				self.cells.matrix[x][y].items.append(coin)

	def draw(self):
		for coin in self.inner:
			pygame.draw.circle(self.surface, con.DARK_RED, coin.cell.rect.center, 8)

	def removePickedCoins(self):
		for coin in self.inner:
			if coin.cell == None:
				self.inner.remove(coin)


class Coin:
	def __init__(self, x, y, cell):
		self.x = x
		self.y = y
		self.value = con.COIN_VALUE
		self.cell = cell