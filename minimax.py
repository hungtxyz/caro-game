
from get_moves import possible_moves
from eval_func import evaluation
from eval_func2 import evaluation as eval2
import math
import time

def best_move(board, turn):
    '''
    trả lại nước đi tốt nhất tính được
    '''
    if turn == 'b':
        anti = 'r'
    else:
        anti = 'b'
    start_time = time.time()
    movecol = (0,0)
    maxscorecol = -math.inf
    moves = possible_moves(board)
    print('-'*20)
    for move in moves:
        y,x = move

        scorecol=minimax(board,y,x, 2, False, -math.inf, math.inf)
        print(scorecol)
        if scorecol > maxscorecol:
            maxscorecol = scorecol
            movecol = move
    end_time = time.time()
    print('total run-time: %f s' % ((end_time - start_time)))
    return movecol


def minimax(board, y, x, depth, isMax, alpha, beta):
    if not isMax:
        board[y][x] = 'b'
    else:
        board[y][x] = 'r' 
    if depth==0:
        if isMax:
            return evaluation(board, 'r', 'b', y, x)
        else:
            return evaluation(board, 'b', 'r', y, x)
    if isMax:
        best_score = -math.inf
        moves = possible_moves(board)
        for i, j in moves:
            score = minimax(board, i, j, depth-1, not isMax, alpha, beta)
            best_score = max(score, best_score)
            alpha = max(alpha, best_score)
            if alpha>=beta:
                break
        board[y][x] = ' '
        return best_score
    else:
        best_score = math.inf
        moves = possible_moves(board)
        for i, j in moves:
            score = minimax(board, i, j, depth-1, not isMax, alpha, beta)
            best_score = min(-score, best_score)
            beta = min(beta, best_score)
            if alpha>=beta:
                break
        board[y][x] = ' '
        return best_score
    

    

