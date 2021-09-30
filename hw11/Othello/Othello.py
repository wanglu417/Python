from tiles import Tiles
from board import Board
from game_controller import GameController
from user_move import UserMove
from AI_move import AIMove
import random

WHITE = 1
BLACK = -1
SQUARE_SIZE = 100
COL_NUM = 8
ROW_NUM = 8
WIDTH = SQUARE_SIZE * COL_NUM
HEIGHT = SQUARE_SIZE * ROW_NUM
INITIAL_TILES1 = 2
INITIAL_TILES2 = 2
board = Board()


def setup():
    answer = input('enter your name')
    if answer:
        print('hi ' + answer)
    elif answer == '':
        print('[empty string]')
    else:
        print(answer)  # Canceled dialog will print None
    size(WIDTH, HEIGHT)
    background(0, 100, 0)
    strokeWeight(3)
    # Draws vertical lines
    for i in range(1, COL_NUM):
        line(i*SQUARE_SIZE, 0, i*SQUARE_SIZE, HEIGHT)
    # Draws horizontal lines
    for j in range(1, ROW_NUM):
        line(0, j*SQUARE_SIZE, WIDTH, j*SQUARE_SIZE)
    board.draw_four_tiles()


def input(message=''):
    '''Input message for the user'''
    from javax.swing import JOptionPane
    return JOptionPane.showInputDialog(frame, message)


def draw():
    # Checks if the clicked position is filled or not
    if board.count < 64:
        if board.flag == WHITE:
            if mousePressed:
                board.coordinate(mouseX, mouseY)
                userMove = UserMove()
                userMove.computer_move(board)
        else:
            board.x = random.randint(0, 7)
            board.y = random.randint(0, 7)
            aiMove = AIMove()
            aiMove.computer_move(board)
    else:
        for i in board.board:
            for j in i:
                if j == BLACK:
                    board.count_black += 1
                else:
                    board.count_white += 1
        print('Your score:', board.count_black)
        print('AI score:', board.count_white)
        f = open('scores.txt', 'rb+')
        f.write(answer, board.count_black)
