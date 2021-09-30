import random
from tiles import Tiles
from user_move import UserMove
from AI_move import AIMove
from game import Game
from board import Board


WHITE = 1
BLACK = -1
SQUARE_SIZE = 100
BOARDSIZE = 8
WIDTH = 800
HEIGHT = 800
game = Game()


def setup():
    '''Set up the checkerboard'''
    size(WIDTH, HEIGHT)
    background(0, 100, 0)
    strokeWeight(3)
    # Draws vertical lines
    for i in range(1, HEIGHT):
        line(i*SQUARE_SIZE, 0, i*SQUARE_SIZE, HEIGHT)
    # Draws horizontal lines
    for j in range(1, WIDTH):
        line(0, j*SQUARE_SIZE, WIDTH, j*SQUARE_SIZE)
    game.board.draw_four_tiles()


def input(message=''):
    '''Input message for the user'''
    from javax.swing import JOptionPane
    return JOptionPane.showInputDialog(frame, message)


def draw():
    '''Alternate between user and AI'''
    if game.board.flag == WHITE:  # Determine if it's user's turn
        userMove = UserMove()
        # Check if user has legal move. If so, user moves.
        if userMove.check_legal(game.board, WHITE):
            # user plays
            if mousePressed:
                game.board.coordinate(mouseX, mouseY)
                userMove.user_move(game.board)
        else:
            print("User has no legal move! AI's turn.")
            # If user has no legal move, switch to AI
            if userMove.check_legal(game.board, BLACK):
                game.board.flag = BLACK
            else:  # If AI has no legal move, game over and start counting
                print("AI has no legal move, either! Game over.")
                for i in game.board.board:
                    for j in i:
                        if j == BLACK:
                            game.board.count_black += 1
                        elif j == WHITE:
                            game.board.count_white += 1
                name = input('enter your name')
                if name:
                    print('hi ' + name)
                elif name == '':
                    print('[empty string]')
                else:
                    print(name)  # Canceled dialog will print None
                game.result(name)
                # Determine whether there is another player
                continue_game = input('continue? (Y/N)')
                if continue_game == 'Y':
                    game.board = Board()
                    setup()
                elif continue_game == 'N':
                    game.record()
                    exit()
                else:
                    print('I do not understand. Game ends.')
                    game.record()
                    exit()

    else:  # AI's turn
        aiMove = AIMove()
        # Check if AI has legal move
        # If so, AI places a WHITE tile in a random legal position
        if aiMove.check_legal(game.board, BLACK):
            game.board.x = random.randint(0, BOARDSIZE-1)
            game.board.y = random.randint(0, BOARDSIZE-1)
            aiMove.computer_move(game.board)
        else:  # If AI has no legal move, switch to user
            print("AI has no legal move! User's turn.")
            # If AI has legal move, AI plays
            if aiMove.check_legal(game.board, WHITE):
                game.board.flag = WHITE
            else:  # If AI has no legal move, end the game
                print("User has no legal move, either! Game over.")
                for i in game.board.board:
                    for j in i:
                        if j == BLACK:
                            game.board.count_black += 1
                        elif j == WHITE:
                            game.board.count_white += 1
                name = input('enter your name')
                if name:
                    print('hi ' + name)
                elif name == '':
                    print('[empty string]')
                else:
                    print(name)  # Canceled dialog will print None
                game.result(name)
                # Determine whether there is another player
                continue_game = input('continue? (Y/N)')
                if continue_game == 'Y' or continue_game == 'y':
                    game.board = Board()
                    setup()
                elif continue_game == 'N' or continue_game == 'n':
                    game.record()
                    exit()
                else:
                    print('I do not understand. Game ends.')
                    game.record()
                    exit()
