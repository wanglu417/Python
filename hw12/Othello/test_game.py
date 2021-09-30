from game import Game
from board import Board


def test_constrcutor():
    '''Test the constructor'''
    g = Game()
    b = Board()
    assert g.highest_score == 0
    assert g.highest_name == ''
    assert g.rest == []
