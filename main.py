#Making Tic Tac Toe with Python

#What will I need?
   #board
   #display game
   #function for win
   #function for tie
   #function for loss
      #check rows
      #check colums
   #switch player 
   #handle turn 

   # ------ Global Variables ------

   # Will hold our game board data
board = ["-", "-", "-",
         "-", "-", "-",
         "-", "-", "-"]

# Lets us know if the game is over yet
game_still_going = True

# Tells us who the winner is
winner = None

# Tells us who the current player is (X goes first)
current_player = "X"


# ------------- Functions ---------------

# Play a game of tic tac toe
def play_game():

  # Show the initial game board
  display_board()

  # Loop until the game stops (winner or tie)
  while game_still_going:

    # Handle a turn
    handle_turn(current_player)

    # Check if the game is over
    check_if_game_over()

    # Flip to the other player
    flip_player()
  
  # Since the game is over, print the winner or tie
  if winner == "X" or winner == "O":
    print(winner + " won.")
  elif winner == None:
    print("Tie.")


# Display the game board to the screen
def display_board():
  print("\n")
  print(board[0] + " | " + board[1] + " | " + board[2] + "     1 | 2 | 3")
  print(board[3] + " | " + board[4] + " | " + board[5] + "     4 | 5 | 6")
  print(board[6] + " | " + board[7] + " | " + board[8] + "     7 | 8 | 9")
  print("\n")


# Handle a turn for an arbitrary player
def handle_turn(player):

  # Get position from player
  print(player + "'s turn.")
  position = input("Choose a position from 1-9: ")

  # Whatever the user inputs, make sure it is a valid input, and the spot is open
  valid = False
  while not valid:

    # Make sure the input is valid
    while position not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
      position = input("Choose a position from 1-9: ")
 
    # Get correct index in our board list
    position = int(position) - 1

    # Then also make sure the spot is available on the board
    if board[position] == "-":
      valid = True
    else:
      print("You can't go there. Go again.")

  # Put the game piece on the board
  board[position] = player

# Now I need to display board
display_board()

# Check if the game is over
def check_if_game_over():
  check_for_winner()
  check_for_tie()

# Check to see if somebody has won
def check_for_winner():
  # Set global variables
  global winner
  # Check if there was a winner anywhere
  row_winner = check_rows()
  column_winner = check_columns()
  diagonal_winner = check_diagonals()
  # Get the winner
  if row_winner:
    winner = row_winner
  elif column_winner:
    winner = column_winner
  elif diagonal_winner:
    winner = diagonal_winner
  else:
    winner = None

# Check rows for win
def check_rows():
  # Set up global variables
  global game_still_going
  # Checking if the rows all have the same variable (and not empty) 
  row_1 = board[0] == board[1] == board[2] != "-"
  row_2 = board[3] == board[4] == board[5] != "-"
  row_3 = board[6] == board[7] == board[8] != "-"
  # if any row does have a match, flag that there is a win
  if row_1 or row_2 or row_3:
    game_still_going = False
# Return the winner: X or O
  if row_1:
    return board[0]
  elif row_2:
    return board[3]
  elif row_3:
    return board[6]
  # Or return None if there is no winner
  else:
    return None

# Check columns for a win
def check_columns():
  def check_columns():
  # Set up global variables
    global game_still_going
  # Checking if the columns all have the same variable (and not empty) 
  column_1 = board[0] == board[3] == board[6] != "-"
  column_2 = board[1] == board[4] == board[7] != "-"
  column_3 = board[2] == board[5] == board[8] != "-"
  # if any row does have a match, flag that there is a win
  if column_1 or column_2 or column_3:
    game_still_going = False
 # Return the winner: X or O
  if column_1:
    return board[0]
  elif column_2:
    return board[1]
  elif column_3:
    return board[2]
  # Or return None for no winner
  else:
    return None

# Check diagonals for win
def check_diagonals():
  # Set up global variables
  global game_still_going
  # Checking if the rows all have the same variable (and not empty) 
  diagonal_1 = board[0] == board[4] == board[8] != "-"
  diagonal_2 = board[6] == board[4] == board[2] != "-"
  # if any row does have a match, flag that there is a win
  if diagonal_1 or diagonal_2:
    game_still_going = False
# Return the winner: X or O
  if diagonal_1:
    return board[0]
  elif diagonal_2:
    return board[2]
# Or return if no winner
  else:
    return None

# Check if there is a tie
def check_for_tie():
  # Set global variables
  global game_still_going
  # If board is full
  if "-" not in board:
    game_still_going = False
    return True
  # Else there is no tie
  else:
    return False

# Switch the current player from X to O, or O to X
def switch_player():
  # Global variables we need
  global current_player
  # If the current player was X, make it O
  if current_player == "X":
    current_player = "O"
  # Or if the current player was O, make it X
  elif current_player == "O":
    current_player = "X"

# ------------ Start Execution -------------
# Play a game of tic tac toe
play_game()