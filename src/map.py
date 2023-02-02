from pandas import *
from game import *
import constants as con
import pygame

class Cells:
    def __init__(self, screen):
        self.screen = screen
        self.inner = []
        self.matrix = []
        self.current_cell = None
        self._load_data()

    def _load_data(self):
        xlsx = ExcelFile("./src/map.xlsx")
        global cells
        cells = xlsx.parse(xlsx.sheet_names[0]).to_dict()
        # for c in cells:
        #     print(cells[c])

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

        # Colocando na matriz
        for x in range(con.TILES_HORIZONTAL - 1):
            col = []
            for y in range(con.TILES_VERTICAL - 1):
                col.append(self.getCell(x, y))
            self.matrix.append(col)

    def draw(self):
        if len(self.inner) == 0:
            raise ValueError("No cells to display.")
        for elem in self.inner:
            self.screen.fill(elem.color, elem.rect)
            # pygame.draw.rect(self.screen, con.BLACK, elem.rect, 1) # Malha Quadriculada

    def printMap(self):
        for y in range(0, con.TILES_VERTICAL - 1):
            for x in range(0, con.TILES_HORIZONTAL - 1):
                print(self.matrix[x][y].type, '', end='')
            print('')
        print('\n\n')

    def getCell(self, x, y):
        id = (((x) * (con.TILES_VERTICAL)) + (y % con.TILES_VERTICAL))
        return self.inner[id]

class Cell:
    def __init__(self, id, x, y, type):
        self.id = id
        self.x = int(x)
        self.y = int(y)
        self.type = type

        global img
        img = {
            'd': con.BROWN
            , 's': con.GRAY
            , 'g': con.GREEN
            , 'p': con.PURPLE
        }
        self.color = img[type]

        self.rect = pygame.Rect(self.x * con.TILESIZE, self.y * con.TILESIZE, con.TILESIZE, con.TILESIZE)

    def setType(self, newType):
        self.type = newType
        self.color = img[newType]