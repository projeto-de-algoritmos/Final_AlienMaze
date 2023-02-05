import pygame
from coin import Coin
import constants as con
from algorithms import aStar, manhattanDistance

class Enemy:
	def __init__(self, x, y, surface, cells, player, color, type):
		self.x = x
		self.y = y
		self.cur_pos = (x,y)
		self.surface = surface
		self.cells = cells
		self.player = player
		self.closestCoins = ()
		self.showPath = False
		self.color = color
		self.points = 0
		self.speed = 300
		self.last_movement = pygame.time.get_ticks()
		self.type = type
        
	def draw(self):
		# Inimigo
		pygame.draw.rect(self.surface, self.color, self.cells.matrix[self.x][self.y])

		# Caminho do player até o inimigo
		path = list(reversed(self.aStarDistance(self.cur_pos,'player')))
		if len(path) > 1 and self.showPath and self.type == 'player':
			for cell in path:
				pygame.draw.circle(self.surface, con.ORANGE, cell.rect.center, 5)

		# Caminho do inimigo até a moeda
		path = list(reversed(self.aStarDistance(self.cur_pos,'coin')))
		if len(path) > 1 and self.showPath and self.type == 'coin':
			for cell in path:
				pygame.draw.circle(self.surface, con.SILVER, cell.rect.center, 5)

	def getItem(self):
		items = self.cells.matrix[self.x][self.y].items
		if len(items) > 0:
			for item in items:
				if isinstance(item, Coin):
					item.cell = None
					items.remove(item)
			self.points += 1
	
	def moveTowardsPlayer(self, algorithmType):
		if algorithmType == 'astar':
			path = list(reversed(self.aStarDistance(self.cur_pos,'player')))
			if len(path) > 1:
				self.x, self.y = path[1].x, path[1].y
				self.cur_pos = (self.x, self.y)
		self.last_movement = pygame.time.get_ticks()
	
	def aStarDistance(self, end, objective):
		if objective == 'player':
			solution = aStar((self.player.x, self.player.y), end, self.cells)
			return solution
		else:
			if len(self.closestCoins) > 0: # Se acabaram as moedas, fique parado
				solution = aStar((self.closestCoins[0][0], self.closestCoins[0][1]), end, self.cells)
			return solution if len(self.closestCoins) > 0 else []

	def moveTowardsCoin(self, algorithmType, closestCoins):
		if algorithmType == 'astar':
			self.closestCoins = closestCoins

			if len(self.closestCoins) > 1: # Se só tem uma moeda, é atrás dela que vamos

				if manhattanDistance((self.x, self.y), self.closestCoins[1]) < manhattanDistance((self.x, self.y), self.closestCoins[0]): # Do par de moedas mais próxima, ir atrás da que está mais perto do inimigo
					self.closestCoins = (self.closestCoins[1], self.closestCoins[0])

			path = list(reversed(self.aStarDistance(self.cur_pos,'coin')))
			if len(path) > 1: # Se só tem uma moeda, é atrás dela que vamos
				self.x, self.y = path[1].x, path[1].y
				self.cur_pos = (self.x, self.y)
			self.last_movement = pygame.time.get_ticks()