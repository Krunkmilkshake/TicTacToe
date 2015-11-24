__author__ = 'zacharymelby'

# Global list to represent the board, initialized to all blank spaces
BOARD = ['', '', '', '', '', '', '', '', '']

# Chars to represent the board locations numbering (i.e., the values
# the user will enter to specify their play)
LOCATION_LIST = [1, 2, 3, 4, 5, 6, 7, 8, 9]


def welcomeMessage():
    '''
    This non-returning function will display the greeting to the user
    '''
    print('')
    print('This program will allow two players to play the game of tic-tac-toe.')
    print("Player 1 has 'X', and player 2 has 'O'.")

def displayBoard(BOARD):
    '''
    This non-returning function will loop through the borad and display all the
    current moves in a grid
    '''
    # for loop to step through the game board
    for i in range(len(BOARD)):
        # If no play has been made at 'i' location, print a dash
        if BOARD[i] == '':
            print(' - ', end='')
        # Else print the appropriate value
        else:
            print('', BOARD[i], '', end='')
        # Print empty string and new line to display the board as a 3x3 array
        if i == 2:
            print('')
        if i == 5:
            print('')
    print('')




def getMove(BOARD, LOACTIONS, player):
    '''
    This funciton will take in the board, a list of valid moves, and the current player.
    It will get the move from the current player and add their move to the board.
    This will not return anything, just modify the game board.
    '''
    # stuff here
    print('')
    displayBoard(BOARD)
    # Show what number user should input to complete their move
    print('Using the board positions shown below...\n')
    print(' 1  2  3 \n 4  5  6 \n 7  8  9 \n')
    print(player[0], end='')
    move = int(input(', enter your move: '))
    while move not in LOACTIONS:
        print('You entered an invalid move, please retry')
        print(player[0], end='')
        move = int(input(', enter your move: '))
    BOARD[LOACTIONS.index(move)] = player[1]




def win(board, player):
    """
    This function will check the board for all possible wining 
    scenarios and return True if those conditions are met, ortherwise
    it will return False.

    """
    # Check rows
    if board[0] == player[1] and  board[1] == player[1] and board[2] == player[1]:
        return True
    elif board[3] == player[1] and board[4] ==  player[1] and board[5] == player[1]:
        return True
    elif board[6] == player[1] and board[7] == player[1] and  board[8] == player[1]:
        return True

    # Check Columns
    elif board[0] == player[1] and board[3] == player[1] and board[6] == player[1]:
        return True
    elif board[1] == player[1] and board[4] == player[1] and board[7] == player[1]:
        return True
    elif board[2] == player[1] and board[5] == player[1] and board[8] == player[1]:
        return True

    # Check diag
    elif board[0] == player[1] and board[4] == player[1] and  board[8] == player[1]:
        return True
    elif board[2] == player[1] and board[4] == player[1] and board[6] == player[1]:
        return True
    else:
        return False



def tieGame(BOARD):
    #if win(BOARD, player) == False:

    if '' in BOARD:
        return False
    else:
        return True



def main():

    # Display the welcoming message and get player 1 and 2
    welcomeMessage()
    name1 = input('Enter the name of payer 1: ')
    player1 = (name1, 'X')
    name2 = input('Enter the name of player 2: ')
    player2 = (name2, 'O')
    print(player1[0], "you start. You are playing 'X'")

    last_player = ''
    gameover = False
    tie = False
    # Start game loop


    while gameover == False and tie == False:
        getMove(BOARD, LOCATION_LIST, player1)
        last_player = player1[0]
        gameover = win(BOARD, player1)
        if gameover == False:
            print('gameover = ', gameover)
            tie = tieGame(BOARD)
            if tie == False:
                print('tie = ', tie)
                getMove(BOARD, LOCATION_LIST, player2)
                last_player = player2[0]
                gameover = win(BOARD, player2)
                print('gameover = ', gameover)
                if gameover == False:
                    tie = tieGame(BOARD)
                    print('tie = ', tie)

    # show final state of board
    displayBoard(BOARD)

    # if game is won
    if gameover == True:
        print(last_player, end='')
        print(', you win!')

    # if game is a tie
    elif tie == True:
        print('Game ends in a tie, everyone is a winner!')
main()
