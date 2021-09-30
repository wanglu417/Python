from AI_move import AIMove
from board import Board
WHITE = 1
BLACK = -1


def test_constructor():
    '''Test the constructor'''
    ai = AIMove()
    assert ai.legal is False
    assert len(ai.direction) == 8
    assert ai.flip == []


def test_check_legal():
    '''Test the check_legal mothed'''
    ai = AIMove()
    b = Board()
    assert ai.check_legal(b, WHITE) is True
    assert ai.check_legal(b, BLACK) is True


def test_computer_move():
    '''Test the computer_move method'''
    ai = AIMove()
    b = Board()
    b.x = 2
    b.y = 2
    ai.computer_move(b)
    assert ai.legal is False
