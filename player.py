import constants as con
import pygame

class Player:
	def __init__(self, surface):
		self.surface = surface
		self.inner = []
		self.cur_x = 8
		self.cur_y = 17

	def draw(self):
		self.surface.fill(con.RED, pygame.Rect(self.cur_x * con.TILESIZE, self.cur_y * con.TILESIZE, con.TILESIZE, con.TILESIZE))