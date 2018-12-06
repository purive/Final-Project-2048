#This is the code for the final project: Game 2048

import math

class Tile: 
    
    def __init__(self, row, col, value = 0):
        self.row = row
        self.col = col
        self.value = value
        self.color_list = [(239, 234, 214), (239, 234, 214), (223, 174, 125), (247, 181, 149),
                           (238, 117, 111), (253,  81,  62), (252, 239, 150), (251, 233, 104),
                           (250, 226,  61), (248, 218,  12), (241, 213,   7), (  0,   0,   0)]
    
    def color_index(self):
        return int(math.log(self.value, 2)) -1 if self.value < 4096 else 11
    
    def rowcol_to_loc(self, row, col):
        return 60 + 160 * col, 185 + 160 * row
    
    def display(self):
        x, y = self.rowcol_to_loc(self.row, self.col)
        if self.value == 0:
            # Display empty tile
            fill(201, 199, 193)
            noStroke()
            rect(x, y, 150, 150, 15)
        else:
            # Display tile in the correct position
            index = self.color_index()
            c = self.color_list[index]
            r, g, b = c[0], c[1], c[2]
            fill(r, g, b)
            noStroke()
            rect(x, y, 150, 150, 15)
            # Display number of the tile
            if index < 2:
                fill(0, 0, 0)
            else:
                fill(255, 255, 255)
            numstr = str(self.value)
            strlen = len(numstr)
            textFont(createFont("UD Digi Kyokasho NP-B", 18))
            textAlign(CENTER, CENTER)
            tsize = 30 - 3 * (strlen - 6) if strlen > 5 else 40
            textSize(tsize)
            text(numstr, x + 75, y + 75)
            

class Board_2048: 
    
    def __init__(self):
        self.size = 4
        self.tile_count = 0
        self.score = 0
        self.highscore = 0
        self.tiles = {}
        self.initialize_board()
    
    def initialize_board(self):
        for r in range(4):
            for c in range(4):
                self.tiles[(r, c)] = Tile(r, c)
        for i in range(2):
            r, c, v = self.params_for_new_tile(2)
            self.tiles[(r, c)].value = v
    
    def params_for_new_tile(self, val = -1):
        self.tile_count += 1
        row, col = int(random(self.size)), int(random(self.size))
        while self.tiles[(row, col)].value != 0:
            row, col = int(random(self.size)), int(random(self.size))
        chance = random (8)
        # value is 2 with 87.5% chance or 4 with 12.5% chance
        value = val if val != -1 else (2 if chance <7 else 4)
        return row, col, value
    
    def display(self):
        for k in self.tiles:
            t = self.tiles[k]
            t.display()

game = Board_2048()

def setup():
    size (750,850)
    background(239, 234, 214)
    fill(171, 169, 163)
    noStroke()
    rect(50, 175, 650, 650, 15)
    
def draw():
    game.display()
