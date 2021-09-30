from user_move import UserMove
from board import Board
WHITE = -1
BLACK = 1


def test_constructor():
    '''Test the constructor'''
    u = UserMove()
    assert u.legal is False
    assert len(u.direction) == 8
    assert u.flip == []


def test_check_legal():
    '''Test the check_legal mothed'''
    u = UserMove()
    b = Board()
    assert u.check_legal(b, WHITE) is True
    assert u.check_legal(b, BLACK) is True


def test_user_move():
    '''Test the user_move method'''
    u = UserMove()
    b = Board()
    b.x = 2
    b.y = 2
    u.user_move(b)
    assert u.legal is False
