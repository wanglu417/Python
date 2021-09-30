from tiles import Tiles
from board import Board

DIRECTIONS = 8
BLACK = -1
WHITE = 1
NEXT_NEXT = 2
BOARDSIZE = 8


class UserMove():
    '''A class for user's move'''

    def __init__(self):
        self.direction = ((-1, -1), (-1, 0), (-1, 1), (0, -1),
                          (0, 1), (1, -1), (1, 0), (1, 1))
        self.legal = False
        self.flip = []

    def check_legal(self, board, player):
        '''
        Check if there is any legal move remaining
        player can be BLACK (user) or WHITE (AI)
        '''
        for i in range(BOARDSIZE):
            for j in range(BOARDSIZE):
                if board.exist_tiles(i, j):
                    continue
                else:
                    for k in self.direction:
                        if i+k[
                            0] >= 0 and i+k[0
                                            ] < BOARDSIZE and j+k[
                                                1] >= 0 and j+k[
                                1] < BOARDSIZE and board.board[
                                    i+k[0]][j+k[1]
                                            ] == player:
                            for l in range(NEXT_NEXT, BOARDSIZE):
                                if i+l*k[
                                    0] >= 0 and i+l*k[
                                        0] < BOARDSIZE and j+l*k[
                                            1] >= 0 and j+l*k[
                                                1] < BOARDSIZE:
                                    if board.board[
                                        i+l*k[0]][j+l*k[1]
                                                  ] == player:
                                        continue
                                    elif board.board[i+l*k[0]][j+l*k[1]] == 0:
                                        break
                                    else:
                                        return True
        return False

    def user_move(self, board):
        '''Define user's move'''
        # If the square is occupied, do nothing, and repeat user_move
        if board.exist_tiles(board.x, board.y):
            pass
        # If the square is not occupied
        # determine whether this is a legal move
        else:
            for i in self.direction:
                # a list that stores positions of squares
                # that possibly lie between two BLACK tiles
                self.temp = list(self.flip)
                if board.x+i[
                    0] >= 0 and board.x+i[
                    0] <= BOARDSIZE - 1 and board.y+i[
                        1] >= 0 and board.y+i[
                            1] <= BOARDSIZE - 1 and board.board[
                            board.x+i[0]
                ][board.y+i[1]] == WHITE:
                    self.temp.append([board.x+i[0], board.y+i[1]])
                    for j in range(NEXT_NEXT, BOARDSIZE):
                        if board.x+j*i[
                            0] >= 0 and board.x+j*i[
                                0] <= BOARDSIZE - 1 and board.y+j*i[
                                    1] >= 0 and board.y+j*i[
                                        1] <= BOARDSIZE - 1:
                            if board.board[
                                board.x+j*i[0]][board.y+j*i[1]
                                                ] == WHITE:
                                self.temp.append(
                                    [board.x+j*i[0], board.y+j*i[1]]
                                )
                                continue
                            elif board.board[
                                board.x+j*i[0]][board.y+j*i[1]
                                                ] == 0:
                                break
                            else:
                                # Mark the position under investigation legal
                                self.legal = True
                                self.flip = list(self.temp)
                else:
                    continue
            # If the current position is a legal move
            # place a BLACK tile, switch to AI
            if self.legal:
                board.add_tile(board.x, board.y, WHITE)
                for i in self.flip:
                    board.add_tile(i[0], i[1], WHITE)
                board.count += 1
                board.flag = BLACK
                print("AI's turn.")
