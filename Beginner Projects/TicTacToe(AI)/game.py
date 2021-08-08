from player import HumanPlayer,RandomComputerPlayer,GenComputerPlayer
import time
import math

class TicTacToe:
    def __init__(self):
        self.board = self.make_board()
        self.current_winner = None
    
    @staticmethod
    def make_board():
        return[' 'for _ in range(9)]

    def print_board(self):
        for row in [self.board[i*3:(i+1)*3] for i in range(3)]:
            print('| ' + ' | '.join(row) + ' |')

    @staticmethod
    def print_nums():
        number_board = [[str(i) for i in range(j*3,(j+1)*3)] for j in range(3)]
        for row in number_board:
            print('| ' + ' | '.join(row) + ' |')

    def available(self):
        return [i for i,x in enumerate(self.board) if x==" "]


    def empty_squares(self):
        return ' ' in self.board

    def empty(self):
        return self.board.count(' ')

    def make_move(self,square,letter):
        if self.board[square]==' ':
            self.board[square]= letter
            if self.winner(square,letter):
                self.current_winner = letter
            return True
        return False

    def winner(self,square,letter):
        row_index = math.floor(square/3)
        row = self.board[row_index*3 : (row_index+1)*3]
        if all([point == letter for point in row]):
            return True
        
        col_index = square%3
        col = [self.board[col_index+i*3] for i in range(3)]
        if all([point==letter for point in col]):
            return True
        
        if square%2==0:
            dia1 = [self.board[i] for i in [0,4,8]]
            if all([point==letter for point in dia1]):
                return True
            
            dia2 = [self.board[i] for i in [2,4,6]]
            if all([point==letter for point in dia2]):
                return True
        return False



def play(x_play, o_play, game, print_game =True):
    if print_game:
        game.print_nums()
    
    letter = 'X'

    while game.empty():
        if letter =='O':
            square = o_play.get_move(game)
        else:
            square  = x_play.get_move(game)
        
        if game.make_move(square,letter):
            if print_game:
                print(letter + ' makes a move to square {square}')
                game.print_board()
                print('')

            if game.current_winner:
                if print_game:
                    print(letter+' wins!')
                return letter

            letter ='O' if letter=='X' else 'X'

        time.sleep(0.8)
    if print_game:
        print('It\'s a tie!')
        
if __name__ == '__main__':
    x_play = HumanPlayer('X')
    o_play = GenComputerPlayer('O')
    t = TicTacToe()
    play(x_play,o_play,t,print_game=True)