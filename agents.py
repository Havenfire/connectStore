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
        return f'{self.__class__.__name__}({self.char})'


class Copycat(Agent):
    def take_turn(self, board):
        for x in range(SIZE_X):
            for y in range(SIZE_Y - 1, 0, -1):
                if board[y][x] not in [CHAR_EMPTY, self.char] and board[y - 1][x] == CHAR_EMPTY:
                    return x
        return super().take_turn(board)


class HeuristicAgent(Agent):
    def take_turn(self, board):
        other_players = set(board.chars) - set(self.char)

        scores = [0] * SIZE_X
        for i in range(SIZE_X):
            if board[0][i] != CHAR_EMPTY:
                scores[i] = -1000
                continue
            my_board = board.copy()
            my_board.place_piece(i, self.char)
            if my_board.check_win() == self.char:
                scores[i] += 100

            for other_char in other_players:
                other_board = board.copy()
                other_board.place_piece(i, other_char)
                if other_board.check_win() == other_char:
                    scores[i] += 50

        return argmax(scores)


class Human(Agent):
    def take_turn(self, board):
        col = int(input(f'What column do you want to play [{self.char}] on? ')) - 1
        while board[0][col] != CHAR_EMPTY:
            col = int(input(f'Column {col} already full, please choose another: '))
        return col


class Gamer(Agent):
    def take_turn(self, board):
        for i in range(1, SIZE_X):
            board.place_piece(i, self.char)
        return 0

class See3PO(Agent):
    def take_turn(self, board):
        for col in range(SIZE_X):
            if(board[0][col] == CHAR_EMPTY):
                t_board = board.copy()
                t_board.place_piece(col, self.char)
                if t_board.check_win() != None:
                    
                    return col
            if(board[0][col] == CHAR_EMPTY):
                t_board = board.copy()
                t_board.place_piece(col, CHAR_0)
                if t_board.check_win() != None:
                    
                    return col
        return super().take_turn(board)
    


class MidLover(Agent):
    def take_turn(self, board):
        prio = [3, 2, 4, 1, 5, 0, 6]
        for col in prio:
            if board[0][col] != CHAR_EMPTY:
                return col


class CenterLover:
    def __init__(self, char):
        self.char = char

    def take_turn(self, board):
        prio = self.createPrio

        for i in range(SIZE_X):
            board
            

    def createPrio():
        prio = [SIZE_X][SIZE_Y]
        x_vals = [1, 2, 3, 4, 3, 2, 1]
        y_vals = [1, 2, 3, 3, 2, 1]

        for i in range[0, SIZE_X]:
            for j in range[0, SIZE_Y]:
                prio[i][j] = x_vals[i] * y_vals[j]
        return prio



    def __repr__(self):
        return f'Agent({self.char})'