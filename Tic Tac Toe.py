"""PROMPT"""
# define a print board (check)
# define a player move (check)
# define what is victory (check)
# define what a draw is (check)
# Create a While Loop (check)
# -----------------------------------------------------------------------------------------------------------------
dictionary = {'1': '1', '2': '2', '3': '3', '4': '4', '5': '5', '6': '6', '7': '7', '8': '8', '9': '9', }
# dictionary to use for the function below


def print_board(board):
    print(board['1'] + "|" + board['2'] + "|" + board['3'])
    print(board['4'] + "|" + board['5'] + "|" + board['6'])
    print(board['7'] + "|" + board['8'] + "|" + board['9'])
# defining board

# -----------------------------------------------------------------------------------------------------------------


player_turn = "O"   # variable for the player's turn
draw_counter = 0    # variable for move counter
while True:
    def player_move():
        print_board(dictionary)    # printing the board
        move = input("It's " + player_turn + "'s turn, pick a spot: ")  # user input
        if int(move) >= 1 and int(move) <= 10:  # checking if number is valid
            if dictionary[move] == move:
                dictionary[move] = player_turn  # putting the user input on the board
            else:
                print("Spot is taking, try a valid spot.")
                player_move()
        else:
            print("Error, Pick a number from 1 - 9")
            player_move()
    draw_counter += 1   # This will determine the number of moves that happened so far
    # below checks the win conditions
    if dictionary['1'] == dictionary['2'] == dictionary['3']:
        print_board(dictionary)
        print("GG! " + player_turn + " Won!")
        break
    elif dictionary['4'] == dictionary['5'] == dictionary['6']:
        print_board(dictionary)
        print("GG! " + player_turn + " Won!")
        break
    elif dictionary['7'] == dictionary['8'] == dictionary['9']:
        print_board(dictionary)
        print("GG! " + player_turn + " Won!")
        break
    elif dictionary['1'] == dictionary['2'] == dictionary['3']:
        print_board(dictionary)
        print("GG! " + player_turn + " Won!")
        break
    elif dictionary['1'] == dictionary['4'] == dictionary['7']:
        print_board(dictionary)
        print("GG! " + player_turn + " Won!")
        break
    elif dictionary['2'] == dictionary['5'] == dictionary['8']:
        print_board(dictionary)
        print("GG! " + player_turn + " Won!")
        break
    elif dictionary['3'] == dictionary['6'] == dictionary['9']:
        print_board(dictionary)
        print("GG! " + player_turn + " Won!")
        break
    elif dictionary['1'] == dictionary['5'] == dictionary['9']:
        print_board(dictionary)
        print("GG! " + player_turn + " Won!")
        break
    elif dictionary['3'] == dictionary['5'] == dictionary['7']:
        print_board(dictionary)
        print("GG! " + player_turn + " Won!")
        break
    elif draw_counter == 10:    # move counter reached max of 10 moves resulting in a draw
        print_board(dictionary)
        print("Draw")
        break
    # the if statement below gives opponent turn
    if player_turn == "O":
        player_turn = "X"
    else:
        player_turn = "O"
    player_move()   # restart loop
