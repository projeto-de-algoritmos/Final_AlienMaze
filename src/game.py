from map import Cells
import pygame
import constants as con
import os
from map import *
from player import Player
from enemy import Enemy
from algorithms import aStar

class Game:
	def __init__(self):
		pygame.init()
		self.clock = pygame.time.Clock()
		pygame.display.set_caption(con.TITLE)
		self.surface = pygame.display.set_mode((con.WINDOW_WIDTH, con.WINDOW_HEIGHT))
		self.BG_COLOR = con.BLACK
		self.keep_looping = True
		self.cells = Cells(self.surface)
		self.player = Player(self.surface, self.cells)
		self.enemy = Enemy(16, 14, self.surface, self.cells, self.player)

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
				if event.key == pygame.K_RETURN:
					self.cells.matrix[16][14].setType('p')
				else:
					# self.cells.printMap()
					self.player.move(event, self.cells)
			
	def update(self):
		if (pygame.time.get_ticks() % 300) == 0:
			self.enemy.moveTowardsPlayer('astar')

	def draw(self):
		self.surface.fill(self.BG_COLOR)
		self.cells.draw()
		self.player.draw()
		self.enemy.draw()

		# Testando limites
		pygame.draw.rect(self.surface, con.YELLOW, self.cells.matrix[0][0])
		pygame.draw.rect(self.surface, con.YELLOW, self.cells.matrix[19][19])

		# self.surface.fill(con.BLUE, pygame.Rect(17 * con.TILESIZE, 4 * con.TILESIZE, con.TILESIZE, con.TILESIZE))
		pygame.display.update()