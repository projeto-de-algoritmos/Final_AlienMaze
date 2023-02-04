from coin import Coin
import constants as con
import pygame
from algorithms import aStar

class Player:
	def __init__(self, surface, cells):
		self.surface = surface
		self.cells = cells
		self.x = 8
		self.y = 17
		self.points = 0

	def draw(self):
		# Desenhando o player
		self.surface.fill(con.RED, pygame.Rect(self.x * con.TILESIZE, self.y * con.TILESIZE, con.TILESIZE, con.TILESIZE))

	def getItem(self):
		items = self.cells.matrix[self.x][self.y].items
		if len(items):
			i = 0
			for item in items:
				if isinstance(item, Coin):
					item.cell = None
					items = items[:i] + items[i+1:]
				i += 1
			self.points += 1


	def move(self, event, cells):
		# print(self.x, self.y)
		if event.key == pygame.K_w:
			if cells.getCell(self.x, self.y - 1).type in 'gs':
				self.y -= 1
		elif event.key == pygame.K_a:
			if cells.getCell(self.x - 1, self.y).type in 'gs':
				self.x -= 1
		elif event.key == pygame.K_s:
			if cells.getCell(self.x, self.y + 1).type in 'gs':
				self.y += 1
		elif event.key == pygame.K_d:
			if cells.getCell(self.x + 1, self.y).type in 'gs':
				self.x += 1