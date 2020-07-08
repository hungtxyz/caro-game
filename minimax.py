
from get_moves import possible_moves
from eval_func import evaluation
from eval_func2 import evaluation as eval2
import math
    

def minimax(board, depth, alpha, beta, isAiTurn, y, x):
    if isAiTurn:
        board[y][x] = 'b'
    else:
        board[y][x] = 'r'

    if depth==0:
        if isAiTurn:
            return evaluation(board,'b','r',y,x)
            # return eval2(board)
        else:
            return evaluation(board,'r','b',y,x)
            # return eval2(board)
    
    if not isAiTurn:
        best = -math.inf
    else:
        best = math.inf
    moves = possible_moves(board)
    for y1, x1 in moves: 
        score = minimax(board, depth-1, alpha,beta, not isAiTurn,y1,x1)
        if not isAiTurn:
            best = max(score, best)
        else:
            best = min(score, best)
        if not isAiTurn:
            alpha = max(alpha, best)
        else:
            beta = min(beta, best)
        if alpha>=beta:
            break
    board[y][x] = ' '
    return best



def best_move(board, turn):
    '''
    trả lại nước đi tốt nhất tính được
    '''
    if turn == 'b':
        anti = 'r'
    else:
        anti = 'b'
        
    movecol = (0,0)
    maxscorecol = -math.inf
    moves = possible_moves(board)

    for move in moves:
        y,x = move

        scorecol=minimax(board, 0,-math.inf, math.inf,True,y,x)
        print(scorecol)
        if scorecol > maxscorecol:
            maxscorecol = scorecol
            movecol = move
    return movecol