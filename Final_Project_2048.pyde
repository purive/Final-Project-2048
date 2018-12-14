#This is the code for the final project: Game 2048

#  For the final project, I developed the code for the game 2048. 
#The code used processing program and no other external files or programs were used to create the code. 
#Therefore, there is no need to download anything but just run the code on processing. 

import math

class Tile: 
    
    def __init__(self, row, col, value = 0):
        self.row = row
        self.col = col
        self.value = value
        self.merged = False
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
    
    def move_tiles(self, direction):
        if direction == "up":
            self.move_up()
        elif direction == "down":
            self.move_down()
        elif direction == "right":
            self.move_right()
        elif direction == "left":
            self.move_left()
        self.reset()
    
    def move_up(self):
        has_moved = False
        for row in range(1, 4):
            for col in range(4):
                t2 = self.tiles[(row, col)]
                if t2.value != 0:
                    r = row
                    while r > 0 and self.tiles[(r - 1, col)].value == 0:
                        has_moved = True
                        r = r - 1
                    self.swap(self.tiles[(r, col)], t2)
                    if r != 0:
                        t2 = self.tiles[(r, col)]
                        t1 = self.tiles[(r - 1, col)]
                        if t2.value == t1.value:
                            #If two tiles have same values, merge
                            self.merge(t1, t2)
                            has_moved = True
                            t1.merged = True
        if has_moved:
             r, c, v = self.params_for_new_tile()
             self.tiles[(r, c)].value = v
    def move_down(self):
        has_moved = False
        for row in [2, 1, 0]:
            for col in range(4):
                t2 = self.tiles[(row, col)]
                if t2.value != 0:
                    r = row
                    while r < 3 and self.tiles[(r + 1, col)].value == 0:
                        has_moved = True
                        r = r + 1
                    self.swap(self.tiles[(r, col)], t2)
                    if r != 3:
                        t2 = self.tiles[(r, col)]
                        t1 = self.tiles[(r + 1, col)]
                        if t2.value == t1.value:
                            #If two tiles have same values, merge
                            self.merge(t1, t2)
                            has_moved = True
                            t1.merged = True
        if has_moved:
            r, c, v = self.params_for_new_tile()
            self.tiles[(r, c)].value = v
    def move_right(self):
        has_moved = False
        for col in [2, 1, 0]:
            for row in range(4):
                t2 = self.tiles[(row, col)]
                if t2.value != 0:
                    c = col 
                    while c < 3 and self.tiles[(row, c + 1)].value == 0:
                        has_moved = True
                        c = c + 1
                    self.swap(self.tiles[(row, c)], t2)
                    if c != 3:
                        t2 = self.tiles[(row, c)]
                        t1 = self.tiles[(row, c + 1)]
                        if t2.value == t1.value:
                            #If two tiles have same values, merge
                            self.merge(t1, t2)
                            has_moved = True
                            t1.merged = True
        if has_moved:
            r, c, v = self.params_for_new_tile()
            self.tiles[(r, c)].value = v

    def move_left(self):
        has_moved = False
        for col in range(1, 4):
            for row in range(4):
                t2 = self.tiles[(row, col)]
                if t2.value != 0:
                    c = col 
                    while c > 0 and self.tiles[(row, c - 1)].value == 0:
                        has_moved = True
                        c = c - 1
                    self.swap(self.tiles[(row, c)], t2)
                    if c != 0:
                        t2 = self.tiles[(row, c)]
                        t1 = self.tiles[(row, c - 1)]
                        if t2.value == t1.value:
                            #If two tiles have same values, merge
                            self.merge(t1, t2)
                            has_moved = True
                            t1.merged = True
        if has_moved:
            r, c, v = self.params_for_new_tile()
            self.tiles[(r, c)].value = v
    def swap(self, t1, t2):
        temp = t1.value
        t1.value = t2.value
        t2.value = temp
    def reset(self):
        for row in range(4):
            for col in range(4):
                self.tiles[(row, col)].merged = False
    #Merges Tile t2 into Tile t1
    def merge(self, t1, t2):
        # Double the value for t1, remove t2, and increment score (and high score if applicable)
        if not t1.merged:
            t1.value *= 2
            t2.value = 0
            self.tile_count -= 1
            self.score += t1.value
            if self.score > self.highscore:
                self.highscore += t1.value
    
    def has_lost(self):
        if self.tile_count == 16:
            return self.is_immovable()
        else:
            return False
    
    def is_immovable(self):
        rc_add = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        for r1 in range(4):
            for c1 in range(4):
                for pair in rc_add:
                    r2, c2 = r1 + pair[0], c1 + pair[1]
                    if (r2 >= 0 and r2 < 4 and c2 >= 0 and c2 <4) and self.tiles[(r1, c1)].value == self.tiles[(r2, c2)].value:
                        return False
        return True
    
    def display(self):
        self.display_score()
        for k in self.tiles:
            t = self.tiles[k]
            t.display()
        if self.has_lost():
            fill(242, 213, 121)
            stroke(80)
            strokeCap(ROUND)
            strokeWeight(4)
            rect(75, 230, 600, 350, 15)
            textFont(createFont("UD Digi Kyokasho NP-B", 18))
            textAlign(CENTER, CENTER)
            textSize(40)
            fill(0)
            text("GAME OVER", 75 + 300, 290)
            fill(80)
            text("Good Job!!\nYour score is {}\nPress r to retry".format(self.score), 75 + 300, 230 + 205)
    def display_score(self):
        #First display the logo
        fill(241, 213, 7)
        noStroke()
        rect(50, 25, 150, 140, 15)
        fill(255)
        textFont(createFont("UD Digi Kyokasho NP-B", 18))
        textAlign(CENTER, CENTER)
        textSize(50)
        text("2048", 125, 90)
        #Next, display player's score and high score
        fill(171, 169, 163)
        rect(375, 15, 320, 74, 15)
        rect(375, 95, 320, 74, 15)
        fill(0)
        textAlign(LEFT, TOP)
        textSize(18)
        text("Score: ", 385, 40)
        text("High Score: ", 385, 120)
        textAlign(RIGHT, BOTTOM)
        textSize(45)
        text(str(self.score), 665, 80)
        text(str(self.highscore), 665, 160)
    
    def restart(self):
        self.size = 4
        self.tile_count = 0
        self.score = 0
        self.tiles = {}
        self.initialize_board()
        background(239, 234, 214)
        fill(171, 169, 163)
        noStroke()
        rect(50, 175, 650, 650, 15)
    
    

game = Board_2048()
print("Welcome to Simon's 2048 Game! \nPress r to restart the game any time")

def setup():
    size (750,850)
    background(239, 234, 214)
    fill(171, 169, 163)
    noStroke()
    rect(50, 175, 650, 650, 15)
    
def draw():
    game.display()

def keyReleased():
    if not game.has_lost():
        if key == CODED:
            if keyCode == UP:
                game.move_tiles("up")
            elif keyCode == DOWN:
                game.move_tiles("down")
            elif keyCode == RIGHT:
                game.move_tiles("right")
            elif keyCode == LEFT:
                game.move_tiles("left")
    if key == 'r':
        game.restart()
        delay(500)
                
    
