from copy import deepcopy

def evaluation(board):
    board1 = deepcopy(board)
    verScore = verticalScore(board1)
    return verScore

def verticalScore(board):
    current = ' '
    anti = ' '
    score = 0
    streak = 0
    start = False
    k = False
    score_board = [0,2,4,8,16,32,64,128,256,512,1024]
    for i in range(len(board)):
        streak = 0
        count = 0

        for j in range(len(board[i])-4):
            if start:
                k = True
            if board[i][j] != ' ' and not start:
                start = True
                current = board[i][j]
                if current == 'b':
                    anti = 'r'
                else :
                    anti = 'b'
            if start and k:
                if board[i][j] == current and count<5:
                    streak+=2
                    count+=1
                elif board[i][j] == ' 'and count<5:
                    streak+=1
                    count+=1
                elif board[i][j]== anti:
                    if count<5:
                        streak = 0
                    if current == 'b':
                        score+=score_board[streak]
                    elif current == 'r':
                        score-=score_board[streak]
                    current = anti
                    streak = 0
                    count = 0
                    if current == 'b':
                        anti = 'r'
                    else :
                        anti = 'b'
                if count == 5:
                    if current == 'b':
                        score+=streak*streak
                        streak = 0
                        count = 0
                    else :
                        score-=streak*streak*2
                        streak =0
                        count = 0
    return score