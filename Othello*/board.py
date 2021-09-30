from tiles import Tiles

SQUARE_SIZE = 100
COLUMN_NUM = 8
ROW_NUM = 8
WIDTH = SQUARE_SIZE * COLUMN_NUM
HEIGHT = SQUARE_SIZE * ROW_NUM
BLACK = -1
WHITE = 1
HALF_OF_SQUARE = 0.5


class Board():
    '''A class for the board'''

    def __init__(self):
        '''Iitialize the playing board'''
        self.board = [[0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0, 0], [
                          0, 0, 0, WHITE, BLACK, 0, 0, 0],
                      [0, 0, 0, BLACK, WHITE, 0, 0, 0], [
                          0, 0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0]]
        self.tile1 = Tiles(WIDTH/2 - SQUARE_SIZE/2, HEIGHT/2-SQUARE_SIZE/2)
        self.tile2 = Tiles(WIDTH/2 + SQUARE_SIZE/2, HEIGHT/2-SQUARE_SIZE/2)
        self.tile3 = Tiles(WIDTH/2 + SQUARE_SIZE/2, HEIGHT/2+SQUARE_SIZE/2)
        self.tile4 = Tiles(WIDTH/2 - SQUARE_SIZE/2, HEIGHT/2+SQUARE_SIZE/2)
        self.flag = WHITE
        self.count_black = 0
        self.count_white = 0
        self.count = 4 #count the total tiles on the board

    def draw_four_tiles(self):
        '''Draws the middle four tiles'''
        self.tile1.white_tile()
        self.tile2.black_tile()
        self.tile3.white_tile()
        self.tile4.black_tile()

    def coordinate(self, x, y):
        '''Row/columm of tile under investigation'''
        self.x = x/SQUARE_SIZE
        self.y = y/SQUARE_SIZE

    def exist_tiles(self, x, y):
        '''When a tile exists already, nothing happens'''
        if self.board[x][y] == 0:
            return False
        else:
            return True

    def add_tile(self, x, y, flag):
        '''Add additional tiles to the board'''
        '''When the previous tile is black, draw white'''
        '''When the previous tile is white, drw black'''
        if flag == BLACK:
            self.board[x][y] = WHITE
            self.newtile = Tiles(SQUARE_SIZE*(x+ HALF_OF_SQUARE), SQUARE_SIZE*(y+HALF_OF_SQUARE))
            self.newtile.white_tile()
        else:
            self.board[x][y] = BLACK
            self.newtile = Tiles(SQUARE_SIZE*(x+HALF_OF_SQUARE), SQUARE_SIZE*(y+HALF_OF_SQUARE))
            self.newtile.black_tile()
