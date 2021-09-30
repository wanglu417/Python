from board import Board
from tiles import Tiles
WHITE = 1
BLACK = -1


def test_constructor():
    '''Test the constructor'''
    b = Board()
    assert b.flag == WHITE
    assert len(b.board) == 8
    assert b.board[3][3] == WHITE
    assert b.board[3][4] == BLACK
    assert b.board[4][3] == BLACK
    assert b.board[4][4] == WHITE
    assert b.count_black == 0
    assert b.count_white == 0
    assert b.count == 4


def test_coordinate():
    '''Test the coordinate method'''
    b = Board()
    b.coordinate(0, 0)
    b.x == 0
    b.y == 0
