import random  # random input for the computer board for the game to be played  

print("Welcome to Battleship")

quit = strcmp(input('Quit?','s'),'quit');
if quit:
    disp ('end game')
    % terminate the game somehow
end


LENGTH_OF_SHIPS = [2,3,3,4,5]  
PLAYER_BOARD = [[" "] * 9 for i in range(9)] # dimensions of player board
COMPUTER_BOARD = [[" "] * 9 for i in range(9)] # dimensions of computer board
PLAYER_GUESS_BOARD = [[" "] * 9 for i in range(9)] # dimesnsions of player board
COMPUTER_GUESS_BOARD = [[" "] * 9 for i in range(9)]
LETTERS_TO_NUMBERS = {'A':0, 'B':1, 'C':2, 'D':3, 'E':4, 'F':5, 'G':6, 'H':7, 'I':8}

def print_board(board):
    print("  A B C D E F G H I") # horizontal listing 
    print("  *-*-*-*-*-*-*-*-*") # clean up can see space between the grid more clearly
    row_number = 1
    for row in board:
        print("%d|%s" % (row_number, "|".join(row)))
        row_number += 1

#check if all ships are hit
def count_hit_ships(board):
    count = 0
    for row in board:
        for column in row:
            if column == "X":
                count += 1
    return count

#place Ships

#check if ship fits in board if not will ask for new input by user
def check_ship_fit(SHIP_LENGTH, row, column, orientation):
    if orientation == "H": #H = 
        if column + SHIP_LENGTH > 9:
            return False
        else:
            return True
    else:
        if row + SHIP_LENGTH > 9:
            return False
        else:
            return True
def place_ships(board):
    #loop through length of ships
    for ship_length in LENGTH_OF_SHIPS:
        #loop until ship fits and doesn't overlap
        while True:
            if board == COMPUTER_BOARD:
                orientation, row, column = random.choice(["H", "V"]), random.randint(0,8), random.randint(0,8)
                if check_ship_fit(ship_length, row, column, orientation):
                    #check if ship overlaps
                    if ship_overlaps(board, row, column, orientation, ship_length) == False:
                        #place ship
                        if orientation == "H":
                            for i in range(column, column + ship_length):
                                board[row][i] = "X"
                        else:
                            for i in range(row, row + ship_length):
                                board[i][column] = "X"
                        break
            else:
                place_ship = True
                print('Place the ship with a length of ' + str(ship_length))
                row, column, orientation = user_input(place_ship)
                if check_ship_fit(ship_length, row, column, orientation):
                    #check if ship overlaps
                        if ship_overlaps(board, row, column, orientation, ship_length) == False:
                            #place ship
                            if orientation == "H":
                                for i in range(column, column + ship_length):
                                    board[row][i] = "X"
                            else:
                                for i in range(row, row + ship_length):
                                    board[i][column] = "X"
                            print_board(PLAYER_BOARD)
                            break 

#check e for overlap
def ship_overlaps(board, row, column, orientation, ship_length):
    if orientation == "H":
        for i in range(column, column + ship_length):
            if board[row][i] == "X":
                return True
    else:
        for i in range(row, row + ship_length):
            if board[i][column] == "X":
                return True
    return False


def user_input(place_ship):
    if place_ship == True:
        while True:
            try: 
                orientation = input("Enter orientation (H or V): ").upper() # any letter input will be capitalized for the code to read
                if orientation == "H" or orientation == "V":
                    break
            except TypeError:
                print('Enter a valid orientation H or V')
        while True:
            try: 
                row = input("Enter the row 1-9 of the ship: ")
                if row in '123456789':
                    row = int(row) - 1
                    break
            except ValueError:
                print('Enter a valid letter between 1-9')
        while True:
            try: 
                column = input("Enter the column of the ship: ").upper()
                if column in 'ABCDEFGHI':
                    column = LETTERS_TO_NUMBERS[column]
                    break
            except KeyError:
                print('Enter a valid letter between A-I')
        return row, column, orientation 
    else:
        while True:
            try: 
                row = input("Enter the row 1-9 of the ship: ")
                if row in '123456789':
                    row = int(row) - 1
                    break
            except ValueError:
                print('Enter a valid letter between 1-9')
        while True:
            try: 
                column = input("Enter the column of the ship: ").upper()
                if column in 'ABCDEFGHI':
                    column = LETTERS_TO_NUMBERS[column]
                    break
            except KeyError:
                print('Enter a valid letter between A-I')
        return row, column        


#user and computer turn
def turn(board):
    if board == PLAYER_GUESS_BOARD:
        row, column = user_input(PLAYER_GUESS_BOARD)
        if board[row][column] == "-":
            turn(board)
        elif board[row][column] == "X":
            turn(board)
        elif COMPUTER_BOARD[row][column] == "X":
            board[row][column] = "X"
        else:
            board[row][column] = "-"
    else:
        row, column = random.randint(0,7), random.randint(0,7)
        if board[row][column] == "-":
            turn(board)
        elif board[row][column] == "X":
            turn(board)
        elif PLAYER_BOARD[row][column] == "X":
            board[row][column] = "X"
        else:
            board[row][column] = "-"

place_ships(COMPUTER_BOARD)
print_board(COMPUTER_BOARD)
print_board(PLAYER_BOARD)
place_ships(PLAYER_BOARD)
        
while True:
    #player turn
    while True:
        print('Guess a battleship location')
        print_board(PLAYER_GUESS_BOARD)
        turn(PLAYER_GUESS_BOARD)
        break
    if count_hit_ships(PLAYER_GUESS_BOARD) == 17:
        print("You win!, good job")
        print("run code again to play another round")
        break   
    #computer turn
    while True:
        turn(COMPUTER_GUESS_BOARD)
        break           
    print_board(COMPUTER_GUESS_BOARD)   
    if count_hit_ships(COMPUTER_GUESS_BOARD) == 17:
        print("Sorry, the computer won.")
        print("try again")
        break
