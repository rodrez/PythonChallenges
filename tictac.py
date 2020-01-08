# Display Board
# Use input of user and convert to X or O
# Placing the marker
# Check if player won
# Check if space is empty
# Choose which player goes first
# Check if board is full
# Have the player select the position
# Game Logic
# Replay option
from random import randint

test_board = ["#", "O", "", "O", "X", "O", "X", "O", "X", "O"]


# Displaying the game board

def display_board(board):
    print(board[7], ' | ', board[8], ' | ', board[9])
    print('-------------')
    print(board[4], ' | ', board[5], ' | ', board[6])
    print('-------------')
    print(board[1], ' | ', board[2], ' | ', board[3])


# display_board(test_board)


# Have the player select a marker

def choose_marker():
    """
   OUTPUT: (player1_marker, player2_marker)
    """

    marker = ''

    while not (marker == "X" or marker == "O"):
        marker = input("Player 1 choose your marker. Please enter X or O.\n").upper()
        if marker != "X" and marker != "O":
            print('That is not an available option.\n')
    if marker == 'X':
        return ('X', 'O')
    else:
        return ('O', 'X')


# player1_marker, player2_marker = choose_marker()


# Place a marker on the board
def place_marker(board, marker, position):
    board[position] = marker


place_marker(test_board, "$", 8)


# display_board() Uncomment to test the place marker function

# Check is a player won the game
def win_check(board, marker):
    return (
            board[7] == marker and board[8] == marker and board[9] == marker or  # Top row
            board[4] == marker and board[5] == marker and board[6] == marker or  # Middle row
            board[1] == marker and board[2] == marker and board[3] == marker or  # Bottom row
            board[7] == marker and board[4] == marker and board[1] == marker or  # Left column
            board[8] == marker and board[5] == marker and board[2] == marker or  # Middle column
            board[9] == marker and board[6] == marker and board[3] == marker or  # Right column
            board[1] == marker and board[5] == marker and board[9] == marker or  # Diagonal
            board[7] == marker and board[5] == marker and board[3] == marker  # Diagonal
    )


# Prints true or false if a player won
# print(win_check(test_board, 'O'))


def space_check(board, position):
    return board[position] == ' '


def choose_first_player():
    flip = randint(1, 2)
    if flip == 1:
        return 'Player 1'
    else:
        return "Player 2"


choose_first_player()


# Checks if there is an empty space in the board
def full_board_check(board):
    for i in range(1, 10):
        if space_check(board, i):
            return False
    return True


full_board_check(test_board)


# Ask the player to select a position in the board
def choose_position(board):
    choice = 0

    while choice not in [1, 2, 3, 4, 5, 6, 7, 8, 9] or not space_check(board, choice):
        choice = int(input('Choose a position [1-9]. \n'))
    return choice


def replay():
    return input('Do you want to play again? Enter Yes or No: ').lower().startswith('y')


# While loop to to keep running the game
print('Welcome to the Tic Tac Toe Game!')

while True:
    # Play the game
    # Set up the game(board, who's first, choose marker)
    the_board = [' '] * 10

    player1_marker, player2_marker = choose_marker()
    print(f'Player 1 marker is {player1_marker} and player 2 marker is {player2_marker}. Good Luck, have fun!')

    turn = choose_first_player()
    print(turn + ' goes first!')

    play_game = input('Would you like to start a game? Enter Yes or No: \n').upper()

    if play_game[0] == 'Y':
        game_on = True
    else:
        game_on = False

    # GamePlay
    while game_on:
        # Player 1 turn?
        if turn == 'Player 1':

            print('Player 1 turn')
            # Show the board
            display_board(the_board)
            # Choose a position
            the_position = choose_position(the_board)
            # Place the marker on the position
            place_marker(the_board, player1_marker, the_position)
            # Check if they won

            if win_check(the_board, player1_marker):
                display_board(the_board)
                print('Player 1 has won the game')
                game_on = False
                # Or check if there is a tie
            else:
                if full_board_check(the_board):
                    display_board(the_board)
                    print('The game is a tie!')
                    game_on = False
                # No tie and no win? Then next player turn.
                else:
                    turn = 'Player 2'


        else:
            print('Player 2 turn.')
            # Show the board
            display_board(the_board)
            # Choose a position
            the_position = choose_position(the_board)
            # Place the marker on the position
            place_marker(the_board, player2_marker, the_position)
            # Check if they won

            if win_check(the_board, player2_marker):
                display_board(the_board)
                print('Player 2 has won the game')
                game_on = False
                # Or check if there is a tie
            else:
                if full_board_check(the_board):
                    display_board(the_board)
                    print('The game is a tie!')
                    game_on = False
                # No tie and no win? Then next player turn.
                else:
                    turn = 'Player 1'

    if not replay():
        break
# TODO fix player turn notification output
