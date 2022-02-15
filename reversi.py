###
### Author: Amimul Ehsan  Zoha
### Course: CS110
### Description: This program implements a simplistic form of the
### reversi game in 1D. There are two users which play this game and
### through different functions, the program determines who wins or a tie
### Along with the print outputs of the game, a graphical representation
### of the game is displayed with every move.
###

from graphics import graphics

# Some constants to be used throughout the code
# The literals 'X' and 'O' and ' ' should not be used elsewhere
WHITE = 'O'
BLACK = 'X'
EMPTY = ' '

def is_move_acceptable(board, turn, pos):
    '''
    This function checks if the user input location for the move
    is acceptable. Returns True if it acceptable otherwise false.
    board: a list  representing the 1 by 12 board
    turn: a string representing current player(either WHITE OR BLACK)'s turn
    pos:an int representing 1 based position of the requested move of the player
    '''
    #if statements to check if the requested move position is within the range of the game.
    if pos-1 >=len(board) or pos-1 < 0:
        return False
    if board[pos-1]!=EMPTY:
        return False
    #returns true if the input position is acceptable for the game.
    return True



def move(board, turn, pos):
    '''
    This function places the piece at the given location and flips
    the pieces according to the rule of the game by iterating through the
    board after each move.
    board: a list  representing the 1 by 12 board
    turn: a string representing current player(either WHITE OR BLACK)'s turn
    pos:an int representing 1 based position of the requested move of the player
    '''
    #As pos is 1 based, index variable is created because board is a 0 based list
    index = pos-1
    board[index]= get_opposite_turn(turn)
    #beginning variable is created to keep track from where the check starts
    beginning= index
    # while loop that iterates through the left side of the beginning variable index in
    #the list.The valid positionis checked so that the index does not go out of bounds
    while beginning>=0 and board[beginning]== get_opposite_turn(turn):
        beginning -=1
    if board[beginning]==EMPTY or beginning == -1:
        beginning = index
    else:
        beginning +=1
    end= index
    # while loop that iterates through the left side of the beginning variable index in
    # the list.The valid position is checked so that the index does not go out of bounds
    while end<len(board) and board[end]== get_opposite_turn(turn):
        end +=1
    if end>=len(board) or board[end] == EMPTY:
        end = index
    else:
        end -=1
    #while loop that flips the turn according to the rule of reversi game.
    while beginning<=end or board[end]==EMPTY:
        board[beginning]=turn
        beginning+=1
    board[index]=turn



def get_move(turn):
    '''
    This function asks the user for an input value for
    the move and returns the number coverting to an int
    turn: a string representing current player(either WHITE OR BLACK)'s turn
    '''
    position = input(str(turn) + ' choose your move:\n')
    #while loop to ask the user repeatedly for a new move if an invalid move is made.
    while not position.isnumeric():
        position=input(turn + ' choose your move:\n')
    return int(position)


def is_over(board):
    '''
    This function determines if the game is over or not by checking if all the
    slots in the board list is filled by user moves.
    returns True is game is over and False if not.
    board: a list  representing the 1 by 12 board
    '''
    i = 0
    #while loop that iterates until all the slots of the board are filled up by user moves
    while i < len(board):
        if board[i]== EMPTY:
            return False
        i+=1
    return True


def get_opposite_turn(turn):
    '''
    This function takes the turn parameter and returns the
    opposite turn.
    turn: a string representing current player(either WHITE OR BLACK)'s turn
    '''
    if turn == BLACK:
        return WHITE
    if turn == WHITE:
        return BLACK


def print_board(board):
    '''
    This function prints out the board for the
    game moves to be displayed in the output.
    board: board: a list  representing the 1 by 12 board
    '''
    print('+' + '-' * 23 + '+')
    i=0
    output='|'
    #while loop that iterated through the board list and
    #places the moves by grabbing from the list.
    while i<len(board):
        output+=str(board[i]) + '|'
        i+=1
    print(output)
    print('+' + '-' * 23 + '+')

def draw_board(board, gui):
    '''
    This funtion displays the board and the updates of the game
    after a move is done by the users in a graphical canvas using graphics module
    board: a list  representing the 1 by 12 board
    gui: A graphics object. Drawing in this canvas
    '''
    #gui.clear is used to clear the previous frame
    gui.clear()
    #gui.text is used to display the Game title REVERSI
    gui.text(230, 30, 'REVERSI', 'black', 35)
    #gui.rectangle is used to display the game board
    gui.rectangle(50,120,615,50,'SeaGreen2')
    i=100
    #while loop which creates each slots of the board using lines
    while i< 630:
        gui.line(i,120,i,170,'blue',3)
        i+=51
    #while loop that iterates through the baord list to draw the WHITE or BLACK
    #move in the designated box. Coordinates have been calculated mathematically.
    i = 0
    while i<len(board):
        if board[i]==WHITE:
            gui.text((i+1)*52.5,125,'O','blue', 25)
        elif board[i]==BLACK:
            gui.text((i+1)*52.5,125,'X','blue', 25)
        i+=1
    gui.update_frame(30)

def who_is_winner(board):
    '''
    This function determines which user is the winner by counting each type of
    player moves in the board list. Returns the winner and returns tie if there
    is a tie
    board: a list  representing the 1 by 12 board
    '''
    #variables assigned to count
    black_counter=0
    white_counter=0
    i=0
    #while loop while that iterates through the board in order to keep count of
    #each players own move.
    while i < len(board):
        if board[i] == WHITE:
            white_counter+=1
        elif board[i] == BLACK:
            black_counter+=1
        i+=1
    #if statement to determine the winner or a tie
    if white_counter > black_counter:
        return 'WHITE WINS'
    if black_counter> white_counter:
        return 'BLACK WINS'
    if black_counter==white_counter:
        return 'THERE WAS A TIE'

def main():
    print('WELCOME TO REVERSI')

    gui = graphics(700, 200, 'reversi')

    # Initialize an empty list with 12 slots
    board = [EMPTY] * 12
    # State of whether or not the game is over
    over = False
    # Starting turn (should alternate as gome goes on)
    turn = BLACK

    # Print out the initial board
    print_board(board)
    draw_board(board, gui)

    # Repeatedly process turns until the game should end (every slot filled)
    while not over:
        place_to_move = get_move(turn)
        while not is_move_acceptable(board, turn, place_to_move):
            place_to_move = get_move(turn)
        move(board, turn, place_to_move)

        print_board(board)
        draw_board(board, gui)

        over = is_over(board)
        turn = get_opposite_turn(turn)
    #print statements to display the result and end of the game
    print('GAME OVER')
    print(who_is_winner(board))

main()