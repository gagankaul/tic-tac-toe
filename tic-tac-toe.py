#Welcome to the Tic Tac Toe Game


def draw_board(input_list):
  """Create a 3x3 grid; either a number board or a tic tac toe game game board"""  
  print("\n\t   Tic-Tac-Toe")
  print("\t------------------")
  print(f"\t|| {input_list[0]} || {input_list[1]} || {input_list[2]} ||")
  print("\t------------------")
  print(f"\t|| {input_list[3]} || {input_list[4]} || {input_list[5]} ||")
  print("\t------------------")
  print(f"\t|| {input_list[6]} || {input_list[7]} || {input_list[8]} ||")
  print("\t------------------")


def get_player_input(player_char, pos_list):
  """Get player's move until it is valid on the board with no piece currently there."""
  running = True
  while running:
    player_move = int(input(f"\n{player_char}: Where would you like to place the piece (1-9): "))
    if player_move > 0 and player_move < 10:
      position = player_move - 1
      if pos_list[position] != '_':
        print("This spot is already taken. Please try again")
      else:
        pos_list[position] = player_char
        running = False
    else:
      print("That is not a spot on the board. Please try again.")


def is_winner(pC, cL):
  """Return a Bool if the given player is a winner"""
  return ((cL[0] == pC and cL[1] == pC and cL[2] == pC) or #victory in first row
          (cL[3] == pC and cL[4] == pC and cL[5] == pC) or #victory in second row
          (cL[6] == pC and cL[7] == pC and cL[8] == pC) or #victory in third row
          (cL[0] == pC and cL[3] == pC and cL[6] == pC) or #victory in first column
          (cL[1] == pC and cL[4] == pC and cL[7] == pC) or #victory in second column
          (cL[2] == pC and cL[5] == pC and cL[8] == pC) or #victory in third column
          (cL[0] == pC and cL[4] == pC and cL[8] == pC) or #victory in digonal 1
          (cL[2] == pC and cL[4] == pC and cL[6] == pC))   #victory in diagonal 2

#The main program loop

#Define variables
players = ["X", "O"]
num_list = ["1","2","3","4","5","6","7","8","9"]
char_list = ["_"]*9

#Draw the initial state of the game board
draw_board(num_list)
draw_board(char_list)

#Program loop to play the game
state = True
while state:
  for player in players:
    get_player_input(player, char_list)
    #Redraw game boards
    draw_board(num_list)
    draw_board(char_list)
    if is_winner(player, char_list):
      print(f"\nCongratulations! {player} has won this game.")
      state = False
      break
    elif "_" not in char_list:
      print("\nThis game is a tie")
      state = False
      break