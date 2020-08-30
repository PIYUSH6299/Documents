def display_board(board):
    # clear_output()    
    print(" " + board[1] + " | " + board[2] + " | " + board[3])
    print('-----------')
    print(" " + board[4] + " | " + board[5] + " | " + board[6])
    print('-----------')
    print(" " + board[7] + " | " + board[8] + " | " + board[9])


test_board = [' ']*10


def player_input():


    global player1_marker
    global player2_marker
    marker = ' '

    while marker != 'X' and marker != 'O':

    
        marker = input('Player 1 : Choose X or O :').upper()

    if marker == 'X':

        player1_marker = 'X'
        player2_marker = 'O'

    else:

        player1_marker = 'O'
        player2_marker = 'X'
    
    return (player1_marker, player2_marker)
    
print(player_input())



def place_marker(board,marker,position):
    
    board[position] = marker


place_marker(test_board,'$',8)
display_board(test_board)


def win_check(board,mark):


    return ((board[1] == mark and board[2] == mark and board[3] == mark) or
            (board[4] == mark and board[5] == mark and board[6] == mark) or
            (board[7] == mark and board[8] == mark and board[9] == mark) or
            (board[1] == mark and board[4] == mark and board[7] == mark) or
            (board[2] == mark and board[5] == mark and board[8] == mark) or
            (board[3] == mark and board[7] == mark and board[9] == mark) or 
            (board[1] == mark and board[5] == mark and board[9] == mark) or
            (board[3] == mark and board[5] == mark and board[7] == mark))


display_board(test_board)
print(win_check(test_board,'X'))



import random

def choose_first():

    flip = random.randint(0,1)

    if flip == 0:
        return 'Player 1'
    else:
        return 'Player 2'




def space_check(board,position):

    return board[position] == ' '



def full_board_check(board):

    for i in range(1,10):
        if space_check(board,i):
            return False
    
    return True



def player_choice(board):

    position = 0 

    while position not in [1,2,3,4,5,6,7,8,9] or not space_check(board,position):
        position = int(input('Choose a Position : (1-9) :'))

    return position



def replay():

    choise = input("Play again? Enter Yes or No : ")

    return choise == 'Yes'


print('Welcome to Tic Tac Toe')

while True:

  

    the_board = [' ']*10
    print(player_input())

    turn = choose_first()
    print(turn + 'Will go First')

    play_game = input('Ready to play? y or n? ')

    if play_game == 'y':
        game_on = True 
    else:
        game_on = False
    ## GAME PLAY 

    while game_on:

        if turn == 'Player 1':

            # show the board
            print(display_board(the_board))
            # choose the position
            position = player_choice(the_board)
            print(position)
            # place the marker on the position
            print(place_marker(the_board,player1_marker,position))

            # check if they won
            if win_check(the_board, player1_marker):
                print(display_board(the_board))
                print('Player 1 Has WON!!!')
                game_on = False
            else:
                if full_board_check(the_board):
                    print(display_board(the_board))
                    print('TIE GAME!!!')
                    break
                else:
                    turn = 'Player 2'

    
        else:
            display_board(the_board)
        
            position = player_choice(the_board)
            
            place_marker(the_board,player2_marker,position)

            
            if win_check(the_board, player2_marker):
                display_board(the_board)
                print('Player 2 Has WON!!!')
                game_on = False
            else:
                if full_board_check(the_board):
                    display_board(the_board)
                    print('TIE GAME!!!')
                    break
                else:
                    turn = 'Player 1'

    if not replay():
        break
    