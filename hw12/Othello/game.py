from board import Board


class Game:
    '''A class controls the whole game process'''

    def __init__(self):
        '''Initialize the game charactor'''
        self.board = Board()
        self.highest_score = 0
        self.highest_name = ''
        self.rest = list()

    def result(self, name):
        '''Handle the score for both parties'''
        print('Your score: ' + str(self.board.count_black))
        print('AI score: ' + str(self.board.count_white))
        '''find the player with the highest score'''
        if self.board.count_black > self.highest_score:
            self.highest_score = self.board.count_black
            self.highest_name = name
        '''save information about players and their scores'''
        self.rest.append([name, self.board.count_black])

    def record(self):
        '''Save game record to file'''
        f = open('scores.txt', 'w')
        '''the player with the highest score is saved first'''
        f.write(self.highest_name+' '+str(self.highest_score)+'\n')
        for i in self.rest:
            if i[0] != self.highest_name or i[1] != self.highest_score:
                f.write(i[0]+' '+str(i[1])+'\n')
