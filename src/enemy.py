import pygame
import constants as con
from algorithms import aStar

class Enemy:
	def __init__(self, x, y, surface, cells, player,color):
		self.x = x
		self.y = y
		self.cur_pos = (x,y)
		self.surface = surface
		self.cells = cells
		self.player = player
		self.closestCoins = ()
		self.showPath = False
		self.color = color
        
	def draw(self):
		# Ponto para testar o A*
		pygame.draw.rect(self.surface, self.color, self.cells.matrix[self.x][self.y])
		path = list(reversed(self.aStarDistance(self.cur_pos,'player')))
		if len(path) > 1 and self.showPath:
			for cell in path:
				pygame.draw.circle(self.surface, con.ORANGE, cell.rect.center, 5)
	
	def moveTowardsPlayer(self, algorithmType):
		if algorithmType == 'astar':
			path = list(reversed(self.aStarDistance(self.cur_pos,'player')))
			if len(path) > 1:
				self.x, self.y = path[1].x, path[1].y
				self.cur_pos = (self.x, self.y)
	
	def aStarDistance(self, end, objective):
		if objective == 'player':
			solution = aStar((self.player.x, self.player.y), end, self.cells)
			return solution
		else:
			solution = aStar((self.closestCoins[0][0], self.closestCoins[0][1]), end, self.cells)
			return solution

	def moveTowardsCoin(self, algorithmType,closestCoins):
		self.closestCoins = closestCoins
		if algorithmType == 'astar':
			path = list(reversed(self.aStarDistance(self.cur_pos,'coin')))
			if len(path) > 1:
				self.x, self.y = path[1].x, path[1].y
				self.cur_pos = (self.x, self.y)