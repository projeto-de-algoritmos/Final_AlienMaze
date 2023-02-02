from map import Cells
import pygame
import constants as con
import os
from map import *
from player import Player

class Game:
	def __init__(self):
		pygame.init()
		self.clock = pygame.time.Clock()
		pygame.display.set_caption(con.TITLE)
		self.surface = pygame.display.set_mode((con.WINDOW_WIDTH, con.WINDOW_HEIGHT))
		self.BG_COLOR = con.BLACK
		self.keep_looping = True
		self.cells = Cells(self.surface)
		self.player = Player(self.surface)

	def main(self):
		while self.keep_looping:
			self.draw()
			self.events()
			self.update()

	def events(self):
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				self.keep_looping = False
			elif event.type == pygame.KEYDOWN:
				if event.key == pygame.K_ESCAPE:
					self.keep_looping = False
				elif event.key == pygame.K_w:
					self.player.cur_y -= 1
				elif event.key == pygame.K_a:
					self.player.cur_x -= 1
				elif event.key == pygame.K_s:
					self.player.cur_y += 1
				elif event.key == pygame.K_d:
					self.player.cur_x += 1
			

	def update(self):
		pass

	def draw(self):
		self.surface.fill(self.BG_COLOR)
		self.cells.draw()
		self.player.draw()
		pygame.display.update()