# Create a function for printing the game grid print values prints the game grid
def print_board(print_game_board):
    print("---------")
    print("|", print_game_board[0], print_game_board[1], print_game_board[2], "|")
    print("|", print_game_board[3], print_game_board[4], print_game_board[5], "|")
    print("|", print_game_board[6], print_game_board[7], print_game_board[8], "|")
    print("---------")


# Create a function for entering in the game grid coordinates and converting the string to a new list
def enter_grid_coordinates():
    grid = str(input('Enter the coordinates: '))
    grid_list = [str(x) for x in str(grid)]
    return grid_list


# Create a function to count the number of empty game cells
def empty_count(empty_count_list):
    empty_counter = 0
    for _ in empty_count_list:
        if _ == '_' or _ == ' ':
            empty_counter += 1
    return empty_counter


# Create a function to count the number of Xs in the game cells
def X_count(X_count_list):
    X_counter = 0
    for _ in X_count_list:
        if _ == 'X':
            X_counter += 1
    return X_counter


# Create a function to count the number of Os in the game cells
def O_count(O_count_list):
    O_counter = 0
    for _ in O_count_list:
        if _ == 'O':
            O_counter += 1
    return O_counter


# Create a function that checks for all game win conditions, an impossible game, and an ongoing game
def win_check(total_O, total_X, total_empty_cells, win_check_list):
    win_condition = 0

    # Check game grid rows for multiple win conditions
    for i in range(0, 6, 3):
        if win_check_list[i] != ' ' and win_check_list[i] == win_check_list[i + 1] and win_check_list[i + 1] == \
                win_check_list[i + 2]:
            win_condition += 1

    # Check game grid columns for multiple win conditions
    for i in range(0, 3):
        if win_check_list[i] != ' ' and win_check_list[i] == win_check_list[i + 3] and win_check_list[i + 3] == \
                win_check_list[i + 6]:
            win_condition += 1

    # Check the first diagonal for multiple win conditions
    if win_check_list[0] != ' ' and win_check_list[0] == win_check_list[4] and win_check_list[4] == win_check_list[8]:
        win_condition += 1

    # Check the second diagonal for multiple win conditions
    if win_check_list[2] != ' ' and win_check_list[2] == win_check_list[4] and win_check_list[4] == win_check_list[6]:
        win_condition += 1

    # Check if the impossible game conditions are true
    if win_condition > 1:  # There can only be one win condition
        print("Impossible")

    elif (total_O - total_X) > 1:
        print("Impossible")

    # Check if a valid win exists and print the winner
    elif win_condition == 1:
        for i in range(0, 6, 3):
            if win_check_list[i] != '_' and win_check_list[i] == win_check_list[i + 1] and win_check_list[i + 1] == \
                    win_check_list[i + 2]:
                print(win_check_list[i], "wins")
                return 1

        for i in range(0, 3):
            if win_check_list[i] != '_' and win_check_list[i] == win_check_list[i + 3] and win_check_list[i + 3] == \
                    win_check_list[i + 6]:
                print(win_check_list[i], "wins")
                return 1

        # Check the first diagonal for a win condition and print the winner
        if win_check_list[0] != '_' and win_check_list[0] == win_check_list[4] and win_check_list[4] == \
                win_check_list[8]:
            print(win_check_list[0], "wins")
            return 1

        # Check the second diagonal for a win condition and print the winner
        if win_check_list[2] != '_' and win_check_list[2] == win_check_list[4] and win_check_list[4] == \
                win_check_list[6]:
            print(win_check_list[2], "wins")
            return 1

    # If none of the win conditions are true and there are no longer any empty or blank cells then "Draw"
    elif total_empty_cells == 0:
        print("Draw")
        return 1

    # If non of the win conditions are true and there are remaining empty or blank cells then "Game not finished"
    elif total_empty_cells != 0:
        return 0


# Create a function that checks if the input coordinates are valid or not
def check_if_valid(check_list):
    correct_range = ['1', '2', '3', ' ']  # List valid range of values for coordinates

    not_valid_count = 0
    out_of_range_count = 0

    for _ in check_list:
        if not _.isnumeric():
            if _ != ' ':
                not_valid_count += 1
        if _.isnumeric() and _ not in correct_range:
            out_of_range_count += 1

    if not_valid_count > 0:
        print('You should enter numbers!')
        return 0
    if out_of_range_count > 0 or check_list[1] != ' ':
        print('Coordinates should be from 1 to 3!')
        return 0
    if not_valid_count == 0 and out_of_range_count == 0:
        return 1


# Create a function that checks if a game grid cell is occupied or not and then if not replaces the cell with the
# current player
def game_cell_occupied_check(grid_coordinates, check_list, player):
    if grid_coordinates[0] == '1' and grid_coordinates[2] == '1':
        if check_list[0] != ' ':
            print('This cell is occupied! Choose another one!')
            return 1
        else:
            check_list[0] = player
            return 0

    if grid_coordinates[0] == '1' and grid_coordinates[2] == '2':
        if check_list[1] != ' ':
            print('This cell is occupied! Choose another one!')
            return 1
        else:
            check_list[1] = player
            return 0

    if grid_coordinates[0] == '1' and grid_coordinates[2] == '3':
        if check_list[2] != ' ':
            print('This cell is occupied! Choose another one!')
            return 1
        else:
            check_list[2] = player
            return 0

    if grid_coordinates[0] == '2' and grid_coordinates[2] == '1':
        if check_list[3] != ' ':
            print('This cell is occupied! Choose another one!')
            return 1
        else:
            check_list[3] = player
            return 0

    if grid_coordinates[0] == '2' and grid_coordinates[2] == '2':
        if check_list[4] != ' ':
            print('This cell is occupied! Choose another one!')
            return 1
        else:
            check_list[4] = player
            return 0

    if grid_coordinates[0] == '2' and grid_coordinates[2] == '3':
        if check_list[5] != ' ':
            print('This cell is occupied! Choose another one!')
            return 1
        else:
            check_list[5] = player
            return 0

    if grid_coordinates[0] == '3' and grid_coordinates[2] == '1':
        if check_list[6] != ' ':
            print('This cell is occupied! Choose another one!')
            return 1
        else:
            check_list[6] = player
            return 0

    if grid_coordinates[0] == '3' and grid_coordinates[2] == '2':
        if check_list[7] != ' ':
            print('This cell is occupied! Choose another one!')
            return 1
        else:
            check_list[7] = player
            return 0

    if grid_coordinates[0] == '3' and grid_coordinates[2] == '3':
        if check_list[8] != ' ':
            print('This cell is occupied! Choose another one!')
            return 1
        else:
            check_list[8] = player
            return 0


# Create a function that alternates the player between X and O based on the current (valid) turn.
def player_alternator_based_on_turn(turn):
    if turn % 2 != 0:
        return 'X'
    if turn % 2 == 0:
        return 'O'


# Initialize the game with these starting values.
game_board_list = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']  # Creates a new initial list from the input string
print_board(game_board_list)  # Prints the initial game board
current_O_count = 0
current_X_count = 0
current_empty_count = 9
turn_number = 0

while win_check(current_O_count, current_X_count, current_empty_count, game_board_list) != 1:

    turn_number += 1  # increment the turn number each time a valid turn starts.
    player = player_alternator_based_on_turn(turn_number)  # Alternate the player each turn

    grid_location_list = enter_grid_coordinates()  # Ask the user to enter the game cell coordinates

    # Check to see if the initial coordinates entered are valid for the game
    while check_if_valid(grid_location_list) != 1:
        grid_location_list = enter_grid_coordinates()

    # If the initial coordinates entered are valid, then check to see if the game cell matching
    # the coordinates is occupied or not
    while game_cell_occupied_check(grid_location_list, game_board_list, player) == 1:
        # If the game cell is occupied then ask the user to enter in a new set of game cell coordinates
        grid_location_list = enter_grid_coordinates()

        # Check these new coordinates for validity again
        while check_if_valid(grid_location_list) != 1:
            grid_location_list = enter_grid_coordinates()

    current_empty_count = empty_count(game_board_list)  # Check the board conditions each turn for all empty cells
    current_X_count = X_count(game_board_list)  # Check the conditions of the board each turn for all X cells
    current_O_count = O_count(game_board_list)  # Check the conditions of the board each turn for all O cells

    print_board(game_board_list)
