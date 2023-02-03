import pygame
import constants as con
from algorithms import aStar

class Enemy:
	def __init__(self, x, y, surface, cells, player):
		self.x = x
		self.y = y
		self.cur_pos = (x,y)
		self.surface = surface
		self.cells = cells
		self.player = player
		self.showPath = False
        
	def draw(self):
		# Ponto para testar o A*
		pygame.draw.rect(self.surface, con.PURPLE, self.cells.matrix[self.x][self.y])
		path = list(reversed(self.aStarDistance(self.cur_pos)))
		if len(path) > 1 and self.showPath:
			for cell in path:
				pygame.draw.circle(self.surface, con.ORANGE, cell.rect.center, 5)
	
	def moveTowardsPlayer(self, algorithmType):
		if algorithmType == 'astar':
			path = list(reversed(self.aStarDistance(self.cur_pos)))
			if len(path) > 1:
				self.x, self.y = path[1].x, path[1].y
				self.cur_pos = (self.x, self.y)
	
	def aStarDistance(self, end):
		solution = aStar((self.player.cur_x, self.player.cur_y), end, self.cells)
		return solution