import pygame
from ai_agent import *
# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
BACKGROUND = (63, 210, 247)
GREEN = (0, 255, 0)

# This sets the square_width and square_height of each grid location
square_width = 40
square_height = 40
square_width = 40
square_height = 40
play_size = 15
window_width = square_width * play_size + play_size + 1 + 200
window_height = square_height * play_size + play_size + 1

# This sets the margin between each cell
MARGIN = 1

# Create a 2 dimensional array. A two dimensional
# array is simply a list of lists.

def create_new_board():
    board = []
    for row in range(play_size):
        # Add an empty array that will hold each cell
        # in this row
        board.append([])
        for column in range(play_size):
            board[row].append(' ')  # Append a cell
    return board


# Initialize pygame
pygame.init()

# Draw the board game
def draw_board(play_size, grid):
    draw_menu()

    for row in range(play_size):
        for column in range(play_size):
            color = WHITE
            if grid[row][column] == 'r':
                color = RED
                pygame.draw.rect(screen, WHITE, [(MARGIN + square_width) * column + MARGIN,
                                             (MARGIN + square_height) * row + MARGIN, square_width, square_height])
                pygame.draw.circle(screen, color, [int((MARGIN + square_width) * column + MARGIN+square_width/2),
                                             int((MARGIN + square_height) * row + MARGIN+square_height/2)],13)
            elif grid[row][column] == 'b':
                color = BLUE
                pygame.draw.rect(screen, WHITE, [(MARGIN + square_width) * column + MARGIN,
                                             (MARGIN + square_height) * row + MARGIN, square_width, square_height])
                pygame.draw.circle(screen, color, [int((MARGIN + square_width) * column + MARGIN+square_width/2),
                                             int((MARGIN + square_height) * row + MARGIN+square_height/2)],13)
            else:
                pygame.draw.rect(screen, color, [(MARGIN + square_width) * column + MARGIN,
                                             (MARGIN + square_height) * row + MARGIN, square_width, square_height])
def draw_status(status, win_row):
    font = pygame.font.SysFont("comicsansms", 30)

    lose = font.render("You lose", True, RED)
    win = font.render("You win",True, RED)
    draw = font.render("Draw", True, RED)
    if status!=8:
        if status == -1:
            screen.blit(win,((MARGIN + square_width) * play_size + MARGIN + 40, 350))
        elif status == 1:
            screen.blit(lose,((MARGIN + square_width) * play_size + MARGIN + 40, 350))
        ##
        y_d, x_d = win_row[0][0], win_row[0][1]
        row, column = win_row[1][0], win_row[1][1]
        y_s, x_s = (square_height+MARGIN)*row+20, (square_width+MARGIN)*column+20
        y_e, x_e =  (square_height+MARGIN)*(row+4*y_d)+20, (square_width+MARGIN)*(column+4*x_d)+20
        pygame.draw.line(screen, BLACK, (x_s,y_s),(x_e, y_e),3)
        ##
    if status == 8:
        screen.blit(draw,((MARGIN + square_width) * play_size + MARGIN + 60, 350))
    
def draw_menu():
    font = pygame.font.SysFont("comicsansms", 20)
    # restart
    restart = font.render("Restart", True, (0, 128, 0))
    pygame.draw.rect(screen, (196, 144, 214), [(MARGIN + square_width) * play_size + MARGIN + 50, 50, 100, 60])
    screen.blit(restart,((MARGIN + square_width) * play_size + MARGIN + 65, 60))
    # Under
    restart = font.render("Under", True, (0, 128, 0))
    pygame.draw.rect(screen, (196, 144, 214), [(MARGIN + square_width) * play_size + MARGIN + 50, 150, 100, 60])
    screen.blit(restart,((MARGIN + square_width) * play_size + MARGIN + 70, 160))

    #help
    help_ = font.render("Help", True, (0, 128, 0))
    pygame.draw.rect(screen, (196, 144, 214), [(MARGIN + square_width) * play_size + MARGIN + 50, 250, 100, 60])
    screen.blit(help_,((MARGIN + square_width) * play_size + MARGIN + 77, 260))



# Set the square_height and square_width of the screen
WINDOW_SIZE = [window_width, window_height]
screen = pygame.display.set_mode(WINDOW_SIZE)

# Set title of screen
pygame.display.set_caption("Caro Game")

# Loop until the user clicks the close button.

loop = True

# Used to manage how fast the screen updates
clock = pygame.time.Clock()
tem_x = 0
tem_y = 0
player_turn = True
# -------- Main Program Loop -----------
# =================================================================#
board = create_new_board()
move_history = []
end = False
while loop:
    for event in pygame.event.get():  # User did something
        if event.type == pygame.QUIT:  # If user clicked close
            loop = False  # Flag that we are done so we exit this loop
        else:
            if event.type == pygame.MOUSEBUTTONDOWN  :  # player_turn
                # User clicks the mouse. Get the position
                
                pos = pygame.mouse.get_pos()
                if (MARGIN + square_width) * play_size + MARGIN + 50 < pos[0] <(MARGIN + square_width) * play_size + MARGIN + 50+100  and 50 <pos[1]<50 +60:
                    board = create_new_board()
                    end = False
                    player_turn = True
                elif (MARGIN + square_width) * play_size + MARGIN + 50 < pos[0] <(MARGIN + square_width) * play_size + MARGIN + 50+100  and 50 <pos[1]<150 +60:
                    if (move_history):
                        y, x = move_history.pop()
                        board[y][x] = ' '
                        y, x = move_history.pop()
                        board[y][x] = ' '
                        end = False
                elif (MARGIN + square_width) * play_size + MARGIN + 50 < pos[0] <(MARGIN + square_width) * play_size + MARGIN + 50+100  and 50 <pos[1]<250 +60  and not end:
                    move = best_move(board, 'r')
                    board[move[0]][move[1]] = 'r'
                    move_history.append([move[0],move[1]])
                    k, win_row = game_status(board,play_size)
                    if k == -1:
                        end = True
                    player_turn = False
                if pos[0]<window_width-210 and pos[1]<window_height and not end and player_turn:
                    # Change the x/y screen coordinates to grid coordinates
                    column = pos[0] // (square_width + MARGIN)
                    row = pos[1] // (square_height + MARGIN)
                    # Set that location to one
                    if board[row][column] == ' ':
                        board[row][column] = 'r'
                        move_history.append([row,column])
                        k, win_row = game_status(board, play_size)
                        if k == -1:
                            end = True
                        player_turn = False

            elif (not player_turn) and loop and not end:  # bot turn
                move = best_move(board, 'b')
                board[move[0]][move[1]] = 'b'
                move_history.append([move[0],move[1]])
                k, win_row = game_status(board,play_size)
                if k == 1:
                    end = True
                player_turn = True

    # Set the screen background

    screen.fill(BACKGROUND)
    # Draw the grid
    draw_board(play_size, board)
    k, win_row = game_status(board, play_size)
    if k == -1:
        draw_status(-1, win_row)
    elif k == 1:
        draw_status(1, win_row)
    elif k == 8:
        draw_status(8, [])
        end =True
    
    # Limit to 60 frames per second
    clock.tick(60)

    # Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

# Be IDLE friendly. If you forget this line, the program will 'hang'
# on exit.
pygame.quit()

