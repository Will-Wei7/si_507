"""
############################## Homework TicTacTo ##############################

% Student Name: Shangqing Wei

% Student Unique Name: weishq

% Lab Section 00X: 002

% I worked with the following classmates: 

%%% Please fill in the first 4 lines of this file with the appropriate information before submitting on Canvas.
"""


# CONSTANTS
PLAYER_NAMES = ["Nobody", "X", "O"] 


# FUNCTIONS
def player_name(player_id):
    '''return the name of a player with a specified ID

    Looks up the name in the PLAYER_NAMES global list

    Parameters
    ----------
    player_id: int
        player's id, which is an index into PLAYER_NAMES

    Returns
    -------
    string
        the player's name

    '''
    return PLAYER_NAMES[player_id]


def display_board(board):
    '''display the current state of the board

    board layout:
    1 | 2 | 3
    4 | 5 | 6
    7 | 8 | 9

    Numbers are replaced by players' names once they move. 
    Iterate through the board and choose the right thing
    to display for each cell.

    Parameters
    ----------
    board: list
        the playing board

    Returns
    -------
    None
    '''

    board_to_show = "" # string that will display the board, starts empty
    for i in range(len(board)):
        if board[i] == 0: # 0 means unoccupied
            # displayed numbers are one greater than the board index
            board_to_show += str(i + 1) # display cell number
        else:
            board_to_show += player_name(board[i]) # display player's mark
        if (i + 1) % 3 == 0: # every 3 cells, start a new row
            board_to_show += "\n"
        else:
            board_to_show += " | " # within a row, divide the cells
    print()
    print(board_to_show)


def make_move(player, board):
    '''allows a player to make a move in the game

    displays who's move it is (X or O)
    prompts the user to enter a number 1-9
    validates input, repeats until valid input is entered
    checks move is valid (space is unoccupied), repeats until valid move
    is entered
    updates/modifies the board in place when a valid move is entered

    Parameters
    ----------
    player: int
        the id of the player to move (1 = X, 2 = O)

    board: list
        the board upon which to move
        the board is modified in place when a valid move is entered
    '''
    move = input(player_name(player) + "'s move: ")
    while move.isdigit() == False or int(move) not in range(1,10):
        print("Enter a number between 1 and 9.")
        move = input(player_name(player) + "'s move: ")
    move = int(move) - 1
    while board[move] != 0:
        print("That space is already occupied, try another.")
        move = input(player_name(player) + "'s move: ")
        while move.isdigit == False or int(move) not in range(1,10):
            print("Enter a number between 1 and 9.")
            move = input(player_name(player) + "'s move: ")
        move = int(move) - 1
    board[move] = player

def check_win_horizontal(board):
    '''Check for a horizontal win in the Tic Tac Toe board.

    This function scans each row of the board to determine if any player has completed
    a horizontal line. It checks if all three cells in any row are occupied by the same player.

    Parameters
    ----------
    board : list
        The current state of the game board, represented as a list of 9 integers.
        The integers are 0 (empty), 1 (player X), or 2 (player O).

    Returns
    -------
    int
        The player ID (1 or 2) of the winner if a horizontal win is detected. 
        Returns 0 if there is no horizontal win.
    '''
    if (board[0] != 0 and 
        board[0] == board[1] and 
        board[0] == board[2]):
        return board[0]
    if (board[3] != 0 and
        board[3] == board[4] and 
        board[3] == board[5]):
        return board[3]
    if (board[6] != 0 and
        board[6] == board[7] and 
        board[6] == board[8]):
        return board[6]
    return 0


def check_win_vertical(board):
    '''Check for a vertical win in the Tic Tac Toe board.

    This function examines each column of the board to determine if any player has completed
    a vertical line. It checks if all three cells in any column are occupied by the same player.

    Parameters
    ----------
    board : list
        The current state of the game board, represented as a list of 9 integers.
        The integers are 0 (empty), 1 (player X), or 2 (player O).

    Returns
    -------
    int
        The player ID (1 or 2) of the winner if a vertical win is detected. 
        Returns 0 if there is no vertical win.
    '''
    if (board[0] != 0 and 
        board[0] == board[3] and 
        board[0] == board[6]):
        return board[0]
    if (board[1] != 0 and
        board[1] == board[4] and 
        board[1] == board[7]):
        return board[1]
    if (board[2] != 0 and
        board[2] == board[5] and 
        board[2] == board[8]):
        return board[2]
    return 0


def check_win_diagonal(board):
    '''Check for a diagonal win in the Tic Tac Toe board.

    This function checks the two diagonals of the board to determine if any player has completed
    a diagonal line. It checks if all three cells in either diagonal are occupied by the same player.

    Parameters
    ----------
    board : list
        The current state of the game board, represented as a list of 9 integers.
        The integers are 0 (empty), 1 (player X), or 2 (player O).

    Returns
    -------
    int
        The player ID (1 or 2) of the winner if a diagonal win is detected. 
        Returns 0 if there is no diagonal win.
    '''
    if(board[0] != 0 and
       board[0] == board[4] and
       board[0] == board[8]):
        return board[0]
    if(board[2] != 0 and    
       board[2] == board[4] and
       board[2] == board[6]):
        return board[2]
    return 0



def check_win(board):
    '''checks a board to see if there's a winner

    delegates to functions that check horizontally, vertically, and 
    diagonally to see if there is a winner. Returns the first winner
    found in the case of multiple winners.

    Parameters
    ----------        
    board: list
        the board to check

    Returns
    -------
    int
        the player ID of the winner. 0 means no winner found.
    '''

    winner = check_win_horizontal(board)
    if (winner != 0):
        return winner
    
    winner = check_win_vertical(board)
    if (winner != 0):
        return winner
    
    return check_win_diagonal(board)


def next_player(current_player):
    '''determines who goes next

    given the current player ID, returns the player who should 
    go next

    Parameters
    ----------        
    current_player: int
        the id of the player who's turn it is now

    Returns
    -------
    int
        the id of the player to go next
    '''
    if current_player == 1:
        player = 2
    else:
        player = 1 
    return player

# MAIN PROGRAM (INDENT LEVEL 0)

# GLOBAL VARIABLES
board = [0, 0, 0,   # top row:    indices 0, 1, 2
         0, 0, 0,   # middle row: indices 3, 4, 5
         0, 0, 0]   # bottom row: indices 6, 7, 8

player = 1          # X goes first
moves_left = 9      # number of moves so far 
winner = 0          # "Nobody" is winning to start

while(moves_left > 0 and winner == 0):
    display_board(board)
    make_move(player, board)
    winner = check_win(board)
    player = next_player(player)
    moves_left -= 1
    if moves_left == 0:
        display_board(board)


print("Game over! " + PLAYER_NAMES[winner] + " wins!")


# TODO: write code to display the correct winner. 
# NOTE: where you implement this (in the while loop or outside it) is up to you to decide, 
# but your program should behave like the sample output
# NOTE: You may also find it helpful to display the board one final time to make sure 
# you are correctly identifying the winner, but you will not be graded on that. 