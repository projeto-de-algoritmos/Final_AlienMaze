from pandas import *
from game import *
import constants as con
import pygame

class Cells:
    def __init__(self, screen):
        self.screen = screen
        self.inner = []
        self.current_cell = None
        self._load_data()

    def _load_data(self):
        xlsx = ExcelFile("map.xlsx")
        global cells
        cells = xlsx.parse(xlsx.sheet_names[0]).to_dict()

        x, y, id = 0, 0, 0
        self.inner = []
        for column in cells:
            y =	0
            for cell in cells[column]:
                new_cell = Cell(id, x, y, cells[column][cell])
                self.inner.append(new_cell)
                id += 1
                y += 1
            x += 1

    def draw(self):
        if len(self.inner) == 0:
            raise ValueError("No cells to display.")
        for elem in self.inner:
            self.screen.fill(elem.color, elem.rect)
            # pygame.draw.rect(self.screen, con.BLACK, elem.rect, 1) # Malha Quadriculada

class Cell:
    def __init__(self, id, x, y, type):
        self.id = id
        self.x = int(x)
        self.y = int(y)
        self.type = type

        img = {
            'd': con.BROWN
            , 's': con.GRAY
            , 'g': con.GREEN
        }
        self.color = img[type]

        self.rect = pygame.Rect(self.x * con.TILESIZE, self.y * con.TILESIZE, con.TILESIZE, con.TILESIZE)
        
