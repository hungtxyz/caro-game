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
    for i in range(len(board)):
        streak = 0
        count = 0
        for j in range(len(board[i])-4):
            if board[i][j] != ' ' and not start:
                start = True
                current = board[i][j]
                if current == 'b':
                    anti = 'r'
                else :
                    anti = 'b'
                j+=1
            if start:
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
                        score+=streak*streak-5
                    elif current == 'r':
                        score-=streak*streak
                    current = anti
                    streak = 0
                    count = 0
                    if current == 'b':
                        anti = 'r'
                    else :
                        anti = 'b'
    return score