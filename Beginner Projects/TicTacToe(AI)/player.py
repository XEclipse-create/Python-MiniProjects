import math
import random
class Player:
    def __init__(self, letter):
        self.letter = letter
    
    def get_move(self,game):
        pass


class RandomComputerPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    
    def get_move(self, game):
        square = random.choice(game.available())
        return square

class HumanPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)
    
    def get_move(self, game):
        valid_square = False
        value = None
        while not valid_square:
            square = input(self.letter + '\'s turn. Input move(0-9):')

            try:
                value =int(square)
                if value not in game.available():
                    raise ValueError
                valid_square = True
            except ValueError:
                print('Invalid Square')
    
        return value 

class GenComputerPlayer(Player):
    def __init__(self,letter):
        super().__init__(letter)


    def get_move(self,game):
        if(len(game.available())==9):
            square = random.choice(game.available())
        else:
            square = self.maxi(game,self.letter)['position']
        
        return square
    
    def maxi(self,state,player):
        max_player = self.letter
        other_player  = 'O' if player=='X' else 'X'

        if state.current_winner == other_player:
            return {'position':None, 'score': 1* (state.empty()+1) if other_player == max_player else -1*(state.empty()+1)}

        elif not state.empty_squares():
            return {'position': None, 'score':0}
    
        if player==max_player:
            best = {'position':None, 'score':-math.inf}
        else:
            best = {'position':None, 'score':math.inf}
        
        for moves in state.available():
            state.make_move(moves, player)
            sim = self.maxi(state,other_player)

            print(sim)
            state.board[moves]= ' '
            state.current_winner = None
            sim['position'] = moves

            if player==max_player:
                if sim['score']>best['score']:
                    best =sim
            else:
                if best['score']>sim['score']:
                    best = sim
        return best

    
