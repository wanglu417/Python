class Tiles():
    '''A class for the Black and White tiles'''

    def __init__(self, x, y):
        '''Initiates the x and y coordinate of the tiles'''
        self.x = x
        self.y = y
        self.W = 255
        self.B = 0
        self.SIZE = 85

    def black_tile(self):
        '''Draws the black tile'''
        fill(self.B)
        ellipse(self.x, self.y, self.SIZE, self.SIZE)

    def white_tile(self):
        '''Draws the white tile'''
        fill(self.W)
        ellipse(self.x, self.y, self.SIZE, self.SIZE)
