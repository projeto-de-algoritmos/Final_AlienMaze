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