import random

from constants import *
from utils import *

class Agent:
    def __init__(self, char):
        self.char = char

    def take_turn(self, board):
        col = random.randrange(SIZE_X)
        while board[0][col] != CHAR_EMPTY:
            col = random.randrange(SIZE_X)
        return col

    def __repr__(self):
        return f'Agent({self.char})'

class See3PO:
    def __init__(self, char):
        self.char = char

    def take_turn(self, board):
        
        for col in range[SIZE_X]:
            if(board[0][col] != CHAR_EMPTY):
                if check_win != None:
                    return col

        col = random.randrange(SIZE_X)
        while board[0][col] != CHAR_EMPTY:
            col = random.randrange(SIZE_X)
        return col


    def __repr__(self):
        return f'Agent({self.char})'
    


class MidLover:
    def __init__(self, char):
        self.char = char

    def take_turn(self, board):
        prio = [3, 2, 4, 1, 5, 0, 6]
        for col in prio:
            if board[0][col] != CHAR_EMPTY:
                return col

    def __repr__(self):
        return f'Agent({self.char})'


class CenterLover:
    def __init__(self, char):
        self.char = char




    def __repr__(self):
        return f'Agent({self.char})'