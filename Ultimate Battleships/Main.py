
# Ultimate Battleships

def print_ships_to_be_placed():
    print("Ships to be placed:", end=" ")
    if FILE_OUTPUT_FLAG:
        f.write("Ships to be placed: ")


# elem expected to be a single list element of a primitive type.
def print_single_element(elem):
    print(str(elem), end=" ")
    if FILE_OUTPUT_FLAG:
        f.write(str(elem) + " ")


def print_empty_line():
    print()
    if FILE_OUTPUT_FLAG:
        f.write("\n")


# n expected to be str or int.
def print_player_turn_to_place(n):
    print("It is Player {}'s turn to place their ships.".format(n))
    if FILE_OUTPUT_FLAG:
        f.write("It is Player {}'s turn to place their ships.\n".format(n))


def print_to_place_ships():
    print("Enter a name, coordinates and orientation to place a ship (Example: Carrier 1 5 h) :", end=" ")
    if FILE_OUTPUT_FLAG:
        f.write("Enter a name, coordinates and orientation to place a ship (Example: Carrier 1 5 h) : \n")
        # There is a \n because we want the board to start printing on the next line.


def print_incorrect_input_format():
    print("Input is in incorrect format, please try again.")
    if FILE_OUTPUT_FLAG:
        f.write("Input is in incorrect format, please try again.\n")


def print_incorrect_coordinates():
    print("Incorrect coordinates given, please try again.")
    if FILE_OUTPUT_FLAG:
        f.write("Incorrect coordinates given, please try again.\n")


def print_incorrect_ship_name():
    print("Incorrect ship name given, please try again.")
    if FILE_OUTPUT_FLAG:
        f.write("Incorrect ship name given, please try again.\n")


def print_incorrect_orientation():
    print("Incorrect orientation given, please try again.")
    if FILE_OUTPUT_FLAG:
        f.write("Incorrect orientation given, please try again.\n")


# ship expected to be str.
def print_ship_is_already_placed(ship):
    print(ship, "is already placed, please try again.")
    if FILE_OUTPUT_FLAG:
        f.write(ship + " is already placed, please try again.\n")


# ship expected to be str.
def print_ship_cannot_be_placed_outside(ship):
    print(ship, "cannot be placed outside the board, please try again.")
    if FILE_OUTPUT_FLAG:
        f.write(ship + " cannot be placed outside the board, please try again.\n")


# ship expected to be str.
def print_ship_cannot_be_placed_occupied(ship):
    print(ship, "cannot be placed to an already occupied space, please try again.")
    if FILE_OUTPUT_FLAG:
        f.write(ship + " cannot be placed to an already occupied space, please try again.\n")


def print_confirm_placement():
    print("Confirm placement Y/N :", end=" ")
    if FILE_OUTPUT_FLAG:
        f.write("Confirm placement Y/N : \n")


# n expected to be str or int.
def print_player_turn_to_strike(n):
    print("It is Player {}'s turn to strike.".format(n))
    if FILE_OUTPUT_FLAG:
        f.write("It is Player {}'s turn to strike.\n".format(n))


def print_choose_target_coordinates():
    print("Choose target coordinates :", end=" ")
    if FILE_OUTPUT_FLAG:
        f.write("Choose target coordinates : ")


def print_miss():
    print("Miss.")
    if FILE_OUTPUT_FLAG:
        f.write("Miss.\n")


# n expected to be str or int.
def print_type_done_to_yield(n):
    print("Type done to yield your turn to player {} :".format(n), end=" ")
    if FILE_OUTPUT_FLAG:
        f.write("Type done to yield your turn to player {} : \n".format(n))


def print_tile_already_struck():
    print("That tile has already been struck. Choose another target.")
    if FILE_OUTPUT_FLAG:
        f.write("That tile has already been struck. Choose another target.\n")


def print_hit():
    print("Hit!")
    if FILE_OUTPUT_FLAG:
        f.write("Hit!\n")


# n expected to be str or int.
def print_player_won(n):
    print("Player {} has won!".format(n))
    if FILE_OUTPUT_FLAG:
        f.write("Player {} has won!\n".format(n))


def print_thanks_for_playing():
    print("Thanks for playing.")
    if FILE_OUTPUT_FLAG:
        f.write("Thanks for playing.\n")


# my_list expected to be a 3-dimensional list, formed from two 2-dimensional lists containing the boards of each player.
def print_3d_list(my_list):
    first_d = len(my_list[0])
    for row_ind in range(first_d):
        second_d = len(my_list[0][row_ind])
        print("{:<2}".format(row_ind+1), end=' ')
        for col_ind in range(second_d):
            print(my_list[0][row_ind][col_ind], end=' ')
        print("\t\t\t", end='')
        print("{:<2}".format(row_ind+1), end=' ')
        for col_ind in range(second_d):
            print(my_list[1][row_ind][col_ind], end=' ')
        print()
    print("", end='   ')
    for row_ind in range(first_d):
        print(row_ind + 1, end=' ')
    print("\t\t", end='   ')
    for row_ind in range(first_d):
        print(row_ind + 1, end=' ')
    print("\nPlayer 1\t\t\t\t\t\tPlayer 2")
    print()

    if FILE_OUTPUT_FLAG:
        first_d = len(my_list[0])
        for row_ind in range(first_d):
            second_d = len(my_list[0][row_ind])
            f.write("{:<2} ".format(row_ind + 1))
            for col_ind in range(second_d):
                f.write(my_list[0][row_ind][col_ind] + " ")
            f.write("\t\t\t")
            f.write("{:<2} ".format(row_ind + 1))
            for col_ind in range(second_d):
                f.write(my_list[1][row_ind][col_ind] + " ")
            f.write("\n")
        f.write("   ")
        for row_ind in range(first_d):
            f.write(str(row_ind + 1) + " ")
        f.write("\t\t   ")
        for row_ind in range(first_d):
            f.write(str(row_ind + 1) + " ")
        f.write("\nPlayer 1\t\t\t\t\t\tPlayer 2\n")
        f.write("\n")


def print_rules():
    print("Welcome to Ultimate Battleships")
    print("This is a game for 2 people, to be played on two 10x10 boards.")
    print("There are 5 ships in the game:  Carrier (occupies 5 spaces), Battleship (4), Cruiser (3), Submarine (3), and Destroyer (2).")
    print("First, the ships are placed. Ships can be placed on any unoccupied space on the board. The entire ship must be on board.")
    print("Write the ship's name, followed by an x y coordinate, and the orientation (v for vertical or h for horizontal) to place the ship.")
    print("If a player is placing a ship with horizontal orientation, they need to give the leftmost coordinate.")
    print("If a player is placing a ship with vertical orientation, they need to give the uppermost coordinate.")
    print("Player 1 places first, then Player 2 places. Afterwards, players take turns (starting from Player 1) to strike and sink enemy ships by guessing their location on the board.")
    print("Guesses are again x y coordinates. Do not look at the board when it is the other player's turn.")
    print("The last player to have an unsunk ship wins.")
    print("Have fun!")
    print()

    if FILE_OUTPUT_FLAG:
        f.write("Welcome to Ultimate Battleships\n")
        f.write("This is a game for 2 people, to be played on two 10x10 boards.\n")
        f.write(
            "There are 5 ships in the game:  Carrier (occupies 5 spaces), Battleship (4), Cruiser (3), Submarine (3), and Destroyer (2).\n")
        f.write(
            "First, the ships are placed. Ships can be placed on any unoccupied space on the board. The entire ship must be on board.\n")
        f.write(
            "Write the ship's name, followed by an x y coordinate, and the orientation (v for vertical or h for horizontal) to place the ship.\n")
        f.write("If a player is placing a ship with horizontal orientation, they need to give the leftmost coordinate.\n")
        f.write("If a player is placing a ship with vertical orientation, they need to give the uppermost coordinate.\n")
        f.write(
            "Player 1 places first, then Player 2 places. Afterwards, players take turns (starting from Player 1) to strike and sink enemy ships by guessing their location on the board.\n")
        f.write("Guesses are again x y coordinates. Do not look at the board when it is the other player's turn.\n")
        f.write("The last player to have an unsunk ship wins.\n")
        f.write("Have fun!\n")
        f.write("\n")


# Create the game
board_size = 10
f = open('UltimateBattleships.txt', 'w')
FILE_OUTPUT_FLAG = True  # You can change this to True to also output to a file so that you can check your outputs with diff.

print_rules()

# Remember to use list comprehensions at all possible times.
# If we see you populate a list that could be done with list comprehensions using for loops, append/extend/insert etc. you will lose points.

# Make sure to put comments in your code explaining your approach and the execution.

# We defined all the functions above for your use so that you can focus only on your code and not the formatting.
# You need to call them in your code to use them of course.

# If you have questions related to this homework, direct them to utku.bozdogan@boun.edu.tr please.

# Do not wait until the last day or two to start doing this homework, it requires serious effort.

try:  # The entire code is in this try block, if there ever is an error during execution, we can safely close the file.
    # DO_NOT_EDIT_ANYTHING_ABOVE_THIS_LINE

    player1_board = [['-' for i in range(board_size)] for j in range(board_size)]
    player1_hidden_board = [['-' for i in range(board_size)] for j in range(board_size)]
    player2_board = [['-' for i in range(board_size)] for j in range(board_size)]
    player2_hidden_board = [['-' for i in range(board_size)] for j in range(board_size)]
    board_for_p1 = [player1_board, player2_hidden_board]
    board_for_p2 = [player1_hidden_board, player2_board]
    # Lists of board's of players.
    # I used 2 identical board for each player so that when one player's turn I can hide other one's actual board.
    ShipLengths = {"carrier": 5, "battleship": 4, "cruiser": 3, "submarine": 3, "destroyer": 2}
    # Defined a dictionary for ship lengths.
    ShipNames = ["Carrier", "Battleship", "Cruiser", "Submarine", "Destroyer"]
    ShipNamesInitial = [i for i in ShipNames]
    # Defined ShipNamesInitial to whether check the chosen ship used or not.
    ConfirmPlacementInput = 0
    ConfirmPlacementInput2 = 0
    # Defined these two variables(one for each player) to use at the end of placement phase.
    while ConfirmPlacementInput != 'y':
        ConfirmPlacementInput = 0
        print_3d_list(board_for_p1)
        print_ships_to_be_placed()
        [print_single_element(i) for i in ShipNames]
        print_empty_line()
        print_player_turn_to_place(1)
        print_to_place_ships()
        inp_list = input().lower().strip().split()
        # This part prints the board, remaining ships, and show which player's turn it is (which is p1 in this part)
        # and then asks for input from the player and making a list from input with split() function
        # This part is the beginning of the game and placement phase for player 1.
        try:
            int(inp_list[1])
            int(inp_list[2])
        except:
            print_incorrect_input_format()
            continue
        # Checks whether the coordinates of given input are convertible to integer or not if they are not convertible
        # it prints an incorrect format error message and returns to the beginning of the loop.
        if len(inp_list) >= 4:
            inp_list = inp_list[0:4]
        else:
            print_incorrect_input_format()
            continue
        # Checks whether enough arguments provided by player 1 or not
        # if the number of arguments is bigger than or equal to 4 it takes the first 4 element of input list.
        # if the number of arguments is less than 4 it prints an incorrect format error message,
        # and returns to the beginning of the loop.
        if int(inp_list[1]) > 10 or int(inp_list[2]) > 10 or int(inp_list[1]) <= 0 or int(inp_list[2]) <= 0:
            print_incorrect_coordinates()
            continue
        # Checks whether the coordinates of given input are on the board or not.
        # If the player provides coordinates outside the board it prints incorrect coordinates error message,
        # and returns to the beginning of the loop.
        elif not inp_list[0] in [i.lower() for i in ShipNames]:
            # If the ship name provided by player 1 (which is inp_list[0])
            # is not in the ShipNames list the program goes into this block
            if not inp_list[0] in [i.lower() for i in ShipNamesInitial]:
                print_incorrect_ship_name()
                continue
            # Checks whether the ship name provided by player 1 is in initial ship names list
            # If it isn't, program prints incorrect ship name error message and returns to the beginning of the loop.
            else:
                print_ship_is_already_placed(inp_list[0].capitalize())
                continue
            # If it is, program prints corresponding ship is already placed error message,
            # and returns to the beginning of the loop.
        elif not inp_list[3] in ['h', 'v']:
            print_incorrect_orientation()
            continue
        # Checks whether the orientation input given by player 1 is valid or not.
        # If it isn't valid, program prints incorrect orientation error message,
        # and returns to the beginning of the loop.
        if inp_list[3] == 'v':
            if int(inp_list[2]) + ShipLengths[inp_list[0]] - 1 > board_size:
                print_ship_cannot_be_placed_outside([i for i in ShipNames if inp_list[0] == i.lower()][0])
                continue
        # If the orientation is vertical,
        # it checks whether the coordinates and orientation the player chose for a ship exceeds the bounds of the board.
        # If the ship chosen by player 1 exceeds the board, program prints ship cannot be placed outside error message,
        # and returns to the beginning of the loop.
        elif inp_list[3] == 'h':
            if int(inp_list[1]) + ShipLengths[inp_list[0]] - 1 > board_size:
                print_ship_cannot_be_placed_outside([i for i in ShipNames if inp_list[0] == i.lower()][0])
                continue
        # If the orientation is horizontal,
        # it checks whether the coordinates and orientation the player chose for a ship exceeds the bounds of the board.
        # If the ship chosen by player exceeds the board, program prints ship cannot be placed outside error message,
        # and returns to the beginning of the loop.
        checker = 0
        for i in range(ShipLengths[inp_list[0]]):
            if inp_list[3] == 'v':
                if board_for_p1[0][int(inp_list[2]) + i - 1][int(inp_list[1]) - 1] == '#':
                    print_ship_cannot_be_placed_occupied([i for i in ShipNames if inp_list[0] == i.lower()][0])
                    break
                else:
                    checker += 1
            elif inp_list[3] == 'h':
                if board_for_p1[0][int(inp_list[2]) - 1][int(inp_list[1]) + i - 1] == '#':
                    print_ship_cannot_be_placed_occupied([i for i in ShipNames if inp_list[0] == i.lower()][0])
                    break
                else:
                    checker += 1
        # This part is a for loop that checks one by one for each part of the ship wants to be placed
        # whether it coincides with a previously placed ship
        # when the checker variable is not equal to the length of the ship that the player 1 wants to place,
        # it means that there is another ship in the area
        # where we are trying to place the ship that the player wants to place.
        # So, in this case program prints ship cannot be placed occupied error message,
        # and returns to the beginning of the loop.
        if checker == ShipLengths[inp_list[0]]:
            for i in range(ShipLengths[inp_list[0]]):
                if inp_list[3] == 'v':
                    board_for_p1[0][int(inp_list[2]) + i - 1][int(inp_list[1]) - 1] = '#'
                elif inp_list[3] == 'h':
                    board_for_p1[0][int(inp_list[2]) - 1][int(inp_list[1]) + i - 1] = '#'
            ShipNames.remove(inp_list[0].capitalize())
        # if the above for loop ends successfully,
        # and the checker variable is equal to the length of the ship that the player 2 wants to place
        # This part prints the ship on the player's board and removes the placed ship's name from the ship names list.
        # (In my code, ship names list represents the remaining ships under the board in placement phase.)
        if ShipNames == []:
            print_3d_list(board_for_p1)
            ConfirmPlacementInput = 0
            while ConfirmPlacementInput != 'y' and ConfirmPlacementInput != 'n':
                print_confirm_placement()
                ConfirmPlacementInput = input().lower().strip()
        # When there is no remaining ships to be placed. This part asks if the player 1 sure about his placement.
        # If he is, program finishes the big while loop move on to the next player's placement phase.
        if ConfirmPlacementInput == 'n':
            ShipNames = ["Carrier", "Battleship", "Cruiser", "Submarine", "Destroyer"]
            board_for_p1[0] = [['-' for i in range(board_size)] for j in range(board_size)]
            continue
        # If he is not sure about his placement, program resets his board and ship list in order for the player to make
        # his placement again.
    ShipNames = ["Carrier", "Battleship", "Cruiser", "Submarine", "Destroyer"]
    while ConfirmPlacementInput2 != 'y':
        ConfirmPlacementInput2 = 0
        print_3d_list(board_for_p2)
        print_ships_to_be_placed()
        [print_single_element(i) for i in ShipNames]
        print_empty_line()
        print_player_turn_to_place(2)
        print_to_place_ships()
        inp_list = input().lower().strip().split()
        # This part prints the board, remaining ships, and show which player's turn it is (which is p1 in this part)
        # and then asks for input from the player and making a list from input with split() function
        # This part is the beginning of the game and placement phase for player 2.
        try:
            int(inp_list[1])
            int(inp_list[2])
        except:
            print_incorrect_input_format()
            continue
        # Checks whether the coordinates of given input are convertible to integer or not if they are not convertible
        # it prints an incorrect format error message and returns to the beginning of the loop.
        if len(inp_list) >= 4:
            inp_list = inp_list[0:4]
        else:
            print_incorrect_input_format()
            continue
        # Checks whether enough arguments provided by player 2 or not
        # if the number of arguments is bigger than or equal to 4 it takes the first 4 element of input list.
        # if the number of arguments is less than 4 it prints an incorrect format error message,
        # and returns to the beginning of the loop.
        if int(inp_list[1]) > 10 or int(inp_list[2]) > 10 or int(inp_list[1]) <= 0 or int(inp_list[2]) <= 0:
            print_incorrect_coordinates()
            continue
        # Checks whether the coordinates of given input are on the board or not.
        # If the player provides coordinates outside the board it prints incorrect coordinates error message,
        # and returns to the beginning of the loop.
        elif not inp_list[0] in [i.lower() for i in ShipNames]:
            # If the ship name provided by player 1 (which is inp_list[0])
            # is not in the ShipNames list the program goes into this block
            if not inp_list[0] in [i.lower() for i in ShipNamesInitial]:
                print_incorrect_ship_name()
                continue
            # Checks whether the ship name provided by player 1 is in initial ship names list
            # If it isn't, program prints incorrect ship name error message and returns to the beginning of the loop.
            else:
                print_ship_is_already_placed(inp_list[0].capitalize())
                continue
            # If it is, program prints corresponding ship is already placed error message,
            # and returns to the beginning of the loop.
        if not inp_list[3] in ['h', 'v']:
            print_incorrect_orientation()
            continue
        # Checks whether the orientation input given by player 2 is valid or not.
        # If it isn't valid, program prints incorrect orientation error message,
        # and returns to the beginning of the loop.
        if inp_list[3] == 'v':
            if int(inp_list[2]) + ShipLengths[inp_list[0]] - 1 > board_size:
                print_ship_cannot_be_placed_outside([i for i in ShipNames if inp_list[0] == i.lower()][0])
                continue
        # If the orientation is vertical,
        # it checks whether the coordinates and orientation the player chose for a ship exceeds the bounds of the board.
        # If the ship chosen by player 2 exceeds the board, program prints ship cannot be placed outside error message,
        # and returns to the beginning of the loop.
        elif inp_list[3] == 'h':
            if int(inp_list[1]) + ShipLengths[inp_list[0]] - 1 > board_size:
                print_ship_cannot_be_placed_outside([i for i in ShipNames if inp_list[0] == i.lower()][0])
                continue
        # If the orientation is horizontal,
        # it checks whether the coordinates and orientation the player chose for a ship exceeds the bounds of the board.
        # If the ship chosen by player 2 exceeds the board, program prints ship cannot be placed outside error message,
        # and returns to the beginning of the loop.
        checker = 0
        for i in range(ShipLengths[inp_list[0]]):
            if inp_list[3] == 'v':
                if board_for_p2[1][int(inp_list[2]) + i - 1][int(inp_list[1]) - 1] == '#':
                    print_ship_cannot_be_placed_occupied([i for i in ShipNames if inp_list[0] == i.lower()][0])
                    break
                else:
                    checker += 1
            if inp_list[3] == 'h':
                if board_for_p2[1][int(inp_list[2]) - 1][int(inp_list[1]) + i - 1] == '#':
                    print_ship_cannot_be_placed_occupied([i for i in ShipNames if inp_list[0] == i.lower()][0])
                    break
                else:
                    checker += 1
        # This part is a for loop that checks one by one for each part of the ship wants to be placed
        # whether it coincides with a previously placed ship
        # when the checker variable is not equal to the length of the ship that the player wants to place,
        # it means that there is another ship in the area
        # where we are trying to place the ship that the player 2 wants to place.
        # So, in this case program prints ship cannot be placed occupied error message,
        # and returns to the beginning of the loop.
        if checker == ShipLengths[inp_list[0]]:
            for i in range(ShipLengths[inp_list[0]]):
                if inp_list[3] == 'v':
                    board_for_p2[1][int(inp_list[2]) + i - 1][int(inp_list[1]) - 1] = '#'
                elif inp_list[3] == 'h':
                    board_for_p2[1][int(inp_list[2]) - 1][int(inp_list[1]) + i - 1] = '#'
            ShipNames.remove(inp_list[0].capitalize())
        # if the above for loop ends successfully,
        # and the checker variable is equal to the length of the ship that the player 2 wants to place
        # This part prints the ship on the player's board and removes the placed ship's name from the ship names list.
        # (In my code, ship names list represents the remaining ships under the board in placement phase.)
        if ShipNames == []:
            print_3d_list(board_for_p2)
            ConfirmPlacementInput2 = 0
            while ConfirmPlacementInput2 != 'y' and ConfirmPlacementInput2 != 'n':
                print_confirm_placement()
                ConfirmPlacementInput2 = input().lower().strip()
        # When there is no remaining ships to be placed. This part asks if the player 2 sure about his placement.
        # If he is, program finishes the big while loop move on to the battle phase.
        if ConfirmPlacementInput2 == 'n':
            ShipNames = ["Carrier", "Battleship", "Cruiser", "Submarine", "Destroyer"]
            board_for_p2[1] = [['-' for i in range(board_size)] for j in range(board_size)]
            continue
        # If he is not sure about his placement, program resets his board and ship list in order for the player to make
        # his placement again.
    BattleQueue = 0
    loop_variable1 = 0
    loop_variable2 = 0
    # BattleQueue variable for determine which player's turn it is.
    # loop_variable1 and loop_variable2 for counting player's successful hits,
    # and finishing the game when one of the players reaches 17 hits.
    while True:
        if loop_variable1 == 17:
            print_3d_list(board_for_p1)
            print_player_won(1)
            print_thanks_for_playing()
            break
        elif loop_variable2 == 17:
            print_3d_list(board_for_p2)
            print_player_won(2)
            print_thanks_for_playing()
            break
        # This if-elif block is for finishing the game when one player reached to 17 successful hit.
        # If loop_variable1 is equal to 17, program prints player 1 won thanks for playing and finishes.
        # If loop_variable2 is equal to 17, program prints player 2 won thanks for playing and finishes.
        if BattleQueue % 2 == 0:
            Queue = 1
            print_3d_list(board_for_p1)
            print_player_turn_to_strike(Queue)
            print_choose_target_coordinates()
            inp2_list = input().strip().split()
            # If the remainder of the BattleQueue with 2 is equal to 0. It indicates that it is the turn of the player 1
            # So, program prints board for p1 and takes input from player 1,
            # and convert it to a list with split() function.
            try:
                int(inp2_list[0])
                int(inp2_list[1])
            except:
                print_incorrect_input_format()
                continue
            # Checks whether the given coordinates are convertible to integer or not if they are not convertible
            # it prints an incorrect format error message and returns to the beginning of the loop.
            if len(inp2_list) >= 2:
                inp2_list = inp2_list[0:2]
            else:
                print_incorrect_input_format()
                continue
            # Checks whether enough arguments provided or not
            # if the number of arguments is bigger than or equal to 2 it takes the first 2 element of input list.
            # if the number of arguments is less than 2 it prints an incorrect format error message,
            # and returns to the beginning of the loop.
            if int(inp2_list[0]) > 10 or int(inp2_list[1]) > 10 or int(inp2_list[0]) <= 0 or int(inp2_list[1]) <= 0:
                print_incorrect_coordinates()
                continue
            # Checks whether the coordinates of given input are on the board or not.
            # If the player provides coordinates outside the board it prints incorrect coordinates error message,
            # and returns to the beginning of the loop.
            if board_for_p2[1][int(inp2_list[1]) - 1][int(inp2_list[0]) - 1] == '!' or board_for_p2[1][int(inp2_list[1]) - 1][int(inp2_list[0]) - 1] == 'O':
                print_tile_already_struck()
                continue
            # if the player accidentally chooses an already attacked tile, program prints this tile is already struck
            # error message and returns to the beginning of the loop.
            if board_for_p2[1][int(inp2_list[1]) - 1][int(inp2_list[0]) - 1] == '#':
                print_hit()
                board_for_p2[1][int(inp2_list[1]) - 1][int(inp2_list[0]) - 1] = '!'
                board_for_p1[1][int(inp2_list[1]) - 1][int(inp2_list[0]) - 1] = '!'
                loop_variable1 += 1
                continue
            # if there is a part of ship in board of player 2 on coordinates given by player 1, program prints hit,
            # changes '#' to '!' on boards of player 2 adds 1 to the loop_variable 1,
            # and goes back to the beginning to ask for new coordinates.
            elif board_for_p2[1][int(inp2_list[1]) - 1][int(inp2_list[0]) - 1] == '-':
                print_miss()
                board_for_p2[1][int(inp2_list[1]) - 1][int(inp2_list[0]) - 1] = 'O'
                board_for_p1[1][int(inp2_list[1]) - 1][int(inp2_list[0]) - 1] = 'O'
                # if there isn't a part of ship in board of player 2 on coordinates given by player 1,
                # program prints miss, changes '#' to '0' on boards of player 2
                done_input = 0
                while done_input != 'done':
                    print_type_done_to_yield(2)
                    done_input = input().strip().lower()
                if done_input == 'done':
                    BattleQueue += 1
                # If player 1 misses this while loop starts and asks for typing done to yielding turn to the next player
                # Loop ends when player 1 types done and the turn passes to the other player.
        if BattleQueue % 2 == 1:
            Queue = 2
            print_3d_list(board_for_p2)
            print_player_turn_to_strike(Queue)
            print_choose_target_coordinates()
            inp2_list = input().strip().split()
            # If the remainder of the BattleQueue with 2 is equal to 1. It indicates that it is the turn of the player 2
            # So, program prints board for p2 and takes input from player 2,
            # and convert it to a list with split() function.
            try:
                int(inp2_list[0])
                int(inp2_list[1])
            except:
                print_incorrect_input_format()
                continue
            # Checks whether the given coordinates are convertible to integer or not if they are not convertible
            # it prints an incorrect format error message and returns to the beginning of the loop.
            if len(inp2_list) >= 2:
                inp2_list = inp2_list[0:2]
            else:
                print_incorrect_input_format()
                continue
            # Checks whether enough arguments provided or not
            # if the number of arguments is bigger than or equal to 2 it takes the first 2 element of input list.
            # if the number of arguments is less than 2 it prints an incorrect format error message,
            # and returns to the beginning of the loop.
            if int(inp2_list[0]) > 10 or int(inp2_list[1]) > 10 or int(inp2_list[0]) <= 0 or int(inp2_list[1]) <= 0:
                print_incorrect_coordinates()
                continue
            # Checks whether the coordinates of given input are on the board or not.
            # If the player provides coordinates outside the board it prints incorrect coordinates error message,
            # and returns to the beginning of the loop.
            if board_for_p1[0][int(inp2_list[1]) - 1][int(inp2_list[0]) - 1] == '!' or board_for_p1[0][int(inp2_list[1]) - 1][int(inp2_list[0]) - 1] == 'O':
                print_tile_already_struck()
                continue
            # if the player accidentally chooses an already attacked tile, program prints this tile is already struck
            # error message and returns to the beginning of the loop.
            if board_for_p1[0][int(inp2_list[1]) - 1][int(inp2_list[0]) - 1] == '#':
                print_hit()
                board_for_p1[0][int(inp2_list[1]) - 1][int(inp2_list[0]) - 1] = '!'
                board_for_p2[0][int(inp2_list[1]) - 1][int(inp2_list[0]) - 1] = '!'
                loop_variable2 += 1
                continue
            # if there is a part of ship in board of player 1 on coordinates given by player 2, program prints hit,
            # changes '#' to '!' on boards of player 1 adds 1 to the loop_variable 2,
            # and goes back to the beginning to ask for new coordinates.
            elif board_for_p1[0][int(inp2_list[1]) - 1][int(inp2_list[0]) - 1] == '-':
                print_miss()
                board_for_p1[0][int(inp2_list[1]) - 1][int(inp2_list[0]) - 1] = 'O'
                board_for_p2[0][int(inp2_list[1]) - 1][int(inp2_list[0]) - 1] = 'O'
                # if there isn't a part of ship in board of player 1 on coordinates given by player 2,
                # program prints miss, changes '#' to '0' on boards of player 1.
                done_input = 0
                while done_input != 'done':
                    print_type_done_to_yield(1)
                    done_input = input().strip().lower()
                if done_input == 'done':
                    BattleQueue += 1
                # If player 2 misses this while loop starts and asks for typing done to yielding turn to the next player
                # Loop ends when player 2 types done and the turn passes to the other player.

    # DO_NOT_EDIT_ANYTHING_BELOW_THIS_LINE
except:
    f.close()

