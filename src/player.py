import constants as con
import pygame
from algorithms import aStar

class Player:
	def __init__(self, surface, cells):
		self.surface = surface
		self.cells = cells
		self.cur_x = 8
		self.cur_y = 17

	def draw(self):
		# Desenhando o player
		self.surface.fill(con.RED, pygame.Rect(self.cur_x * con.TILESIZE, self.cur_y * con.TILESIZE, con.TILESIZE, con.TILESIZE))

		# Ponto para testar o A*
		point = (16,14)
		pygame.draw.rect(self.surface, con.PURPLE, self.cells.matrix[point[0]][point[1]])
		for i in self.aStarDistance(point):
			pygame.draw.circle(self.surface, con.ORANGE, i.rect.center, 5)

	def move(self, event, cells):
		# print(self.cur_x, self.cur_y)
		if event.key == pygame.K_w:
			if cells.getCell(self.cur_x, self.cur_y - 1).type in 'gs':
				self.cur_y -= 1
		elif event.key == pygame.K_a:
			if cells.getCell(self.cur_x - 1, self.cur_y).type in 'gs':
				self.cur_x -= 1
		elif event.key == pygame.K_s:
			if cells.getCell(self.cur_x, self.cur_y + 1).type in 'gs':
				self.cur_y += 1
		elif event.key == pygame.K_d:
			if cells.getCell(self.cur_x + 1, self.cur_y).type in 'gs':
				self.cur_x += 1

	def aStarDistance(self, end):
		solution = aStar((self.cur_x, self.cur_y), end, self.cells)
		return solution