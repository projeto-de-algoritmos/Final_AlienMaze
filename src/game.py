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
        self.surface = pygame.display.set_mode(
            (con.WINDOW_WIDTH, con.WINDOW_HEIGHT))
        self.BG_COLOR = con.BLACK
        self.keep_looping = True
        self.cells = Cells(self.surface)
        self.player = Player(self.surface, self.cells)
        self.enemy = Enemy(16, 14, self.surface, self.cells, self.player)
        self.gameover = False

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
                if event.key == pygame.K_r:
                    self.keep_looping = False
                    jogo = Game()
                    jogo.main()
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
        self.gameOver()

    def draw(self):
        if (self.gameover == False):
            self.surface.fill(self.BG_COLOR)
            self.cells.draw()
            self.player.draw()
            self.enemy.draw()

        # Testando limites
        pygame.draw.rect(self.surface, con.YELLOW, self.cells.matrix[0][0])
        pygame.draw.rect(self.surface, con.YELLOW, self.cells.matrix[19][19])

        # self.surface.fill(con.BLUE, pygame.Rect(17 * con.TILESIZE, 4 * con.TILESIZE, con.TILESIZE, con.TILESIZE))
        pygame.display.update()

    # def game_over_screen():
    # 	bg2 = pygame.image.load('images/gameover.png').convert_alpha()
    # 	bg2 = pygame.transform.scale(bg2, (1300, 800))
    # 	screen.blit(bg2, (0, 0))
    # 	pygame.display.flip()
    # 	waiting = True
    # 	while waiting:
    # 		for event in pygame.event.get():
    # 			if event.type == pygame.QUIT:
    # 				pygame.quit()
    # 			key = pygame.key.get_pressed()
    # 			if key[pygame.K_r]:
    # 				waiting = False

    def gameOver(self):
        if (self.enemy.x == self.player.cur_x and self.enemy.y == self.player.cur_y):
            self.gameover = True
            print(self.gameover)
            gameOverScreen = pygame.image.load(
                'src/images/gameover.png').convert_alpha()
            gameOverScreen = pygame.transform.scale(
                gameOverScreen, (con.WINDOW_WIDTH, con.WINDOW_HEIGHT))
            self.surface.blit(gameOverScreen, (0, 0))
