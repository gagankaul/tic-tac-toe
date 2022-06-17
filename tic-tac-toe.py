#Welcome to the Tic Tac Toe Game

def draw_board(current_list):
  """Draw the columns in a row"""  
  print("\n\t\t   Tic-Tac-Toe")
  print("\t\t------------------")
  print(f"\t\t|| {current_list[0]} || {current_list[1]} || {current_list[2]} ||")
  print("\t\t------------------")
  print(f"\t\t|| {current_list[3]} || {current_list[4]} || {current_list[5]} ||")
  print("\t\t------------------")
  print(f"\t\t|| {current_list[6]} || {current_list[7]} || {current_list[8]} ||")
  print("\t\t------------------")


def get_player_input(player_char, pos_list):
  """Get player's move and check if it is valid"""
  running = True
  while running:
    position = int(input(f"\n{player_char}: Where would you like to place the piece (1-9): ")) - 1
    if pos_list[position] != '_':
      print("This spot is already taken. Please try again")
    else:
      pos_list[position] = player_char
      running = False


def is_winner(pos_list, player_char):
  """Check if a player has won by checking game positions"""
  if pos_list[0] == player_char and pos_list[1] == player_char and pos_list[2] == player_char:
    return True
  elif pos_list[3] == player_char and pos_list[4] == player_char and pos_list[5] == player_char:
    return True
  elif pos_list[6] == player_char and pos_list[7] == player_char and pos_list[8] == player_char:
    return True
  elif pos_list[0] == player_char and pos_list[3] == player_char and pos_list[6] == player_char:
    return True
  elif pos_list[1] == player_char and pos_list[4] == player_char and pos_list[7] == player_char:
    return True
  elif pos_list[2] == player_char and pos_list[5] == player_char and pos_list[8] == player_char:
    return True
  elif pos_list[0] == player_char and pos_list[4] == player_char and pos_list[8] == player_char:
    return True
  elif pos_list[2] == player_char and pos_list[4] == player_char and pos_list[6] == player_char:
    return True
  else:
    return False

#Create a list of players
players = ["X", "O"]

#Create a list of positions to be displayed as the positions grid
n_list = ["1","2","3","4","5","6","7","8","9"]

#Create an empty list of positions that will be displayed as current game grid
c_list = ["_"]*9

#Display positions grid
draw_board(n_list)

#Display game grid
draw_board(c_list)

#Main program loop to play the game
no_winner = True
while no_winner:
  for player in players:
    get_player_input(player, c_list)
    draw_board(n_list)
    draw_board(c_list)
    if is_winner(c_list, player):
      print(f"Congratulations! {player} has won this game.")
      no_winner = False
      break
    elif "_" not in c_list:
      print("It's a tie")