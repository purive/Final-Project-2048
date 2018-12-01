#This is the code for the final project: Game 2048

import math

class Tile: 
    
    def __init__(self, row, col, value = 0):
        self.__row = row
        self.__col = col
        self.value = value

class Board_2048: 
    
    def __init__(self):
        self.__size = 4
        self.__tile_count = 0
        self.__score = 0
        self.__highscore = 0
        self.__tiles = {}
        self.__initialize_board()
    
    def __initialize_board(self):
        for r in range(4):
            for c in range(4):
                self.__tiles[(r, c)] = Tile(r, c)
            for i in range(2):
                r, c, v = self.__params_for_new_tile(2)
                self.__tiles[(r, c)].value = v
    
    def __params_for_new_tile(self, val = -1):
        self.__tile_count += 1
        row, col = int(random(self.__size)), int(random(self.__size))
        while self.__tiles[(row, col)].value != 0:
            row, col = int(random(self.__size)), int(random(self.__size))
        chance = random (8)
        # value is 2 with 87.5% chance or 4 with 12.5% chance
        value = val if val != -1 else (2 if chance <7 else 4)
        return row, col, value



def setup():
    size (750,850)
    background(239, 234, 214)
    fill(171, 169, 163)
    noStroke()
    rect(50, 175, 650, 650, 15)
    
def draw():
    pass
