# main.py
import random

# print the board
def printBoard():
  for i in range(3):
    for j in range(3):
      if (i <= 1):
        if (board[i][j] != ""):
          print("_" + board[i][j] + "_", end = "")
        else:
          print("___", end = "")
        if (j <= 1):
          print("|", end = "")
      else:
        if (board[i][j] != ""):
          print(" " + board[i][j] + " ", end = "")
        else:
          print("   ", end = "")
        if (j <= 1):
          print("|", end = "")
    print()

# add to board
def addToBoard(player, row, col):
  row = row - 1
  col = col - 1
  if (board[row][col] == ""):
    if (player == 1):
      board[row][col] = "X"
    else:
      board[row][col] = "O"
    return True
  else:
    return False

# win check
def rowCheck():
  for i in range(3):
    box1 = board[i][0]
    box2 = board[i][1]
    box3 = board[i][2]
    if (box1 == box2 and box1 == box3 and box1 != ""):
      if (box1 == "X"):
        print("Player 1 wins!")
      else:
        print("Player 2 wins!")
      return True
  return False
  
def colCheck():
  for i in range(3):
    box1 = board[0][i]
    box2 = board[1][i]
    box3 = board[2][i]
    if (box1 == box2 and box1 == box3 and box1 != ""):
      if (box1 == "X"):
        print("Player 1 wins!")
      else:
        print("Player 2 wins!")
      return True
  return False
  
def diagCheck():
  box1 = board[0][0]
  box2 = board[1][1]
  box3 = board[2][2]
  if (box1 == box2 and box1 == box3 and box1 != ""):
    if (box1 == "X"):
      print("Player 1 wins!")
    else:
      print("Player 2 wins!")
    return True
  box1 = board[0][2]
  box3 = board[2][0]
  if (box1 == box2 and box1 == box3 and box1 != ""):
    if (box1 == "X"):
      print("Player 1 wins!")
    else:
      print("Player 2 wins!")
    return True
  return False

def winCheck():
  if (rowCheck() or colCheck() or diagCheck()):
    return False
  tie = True
  for i in range(3):
    for j in range(3):
      if board[i][j] == "":
        tie = False
  if (tie):
    print("Tie! Game over.")
    return False
  return True
    
# player switcher
def playerSwitch():
  if (player == 1):
    return 2
  else:
    return 1

# make board for logic
board = []
for i in range(3):
  row = []
  row.append("")
  row.append("")
  row.append("")
  board.append(row)

# who goes first
player = 0
flip = random.randint(0, 1)

if flip == 0:
  print("Player 1 (X) will go first!")
  player = 1
else:
  print("Player 2 (O) will go first!")
  player = 2

turn = 1

# game
while winCheck():
  row = int(input("Player " + str(player) + ", pick a row to play: "))
  col = int(input("Pick a column: "))
  if ((row < 1 or row > 3) or (col < 1 or col > 3)):
    print("Please enter a valid box (rows 1-3, columns 1-3)")
  else:
    if (addToBoard(player, row, col)):
      printBoard()
      player = playerSwitch()
      turn += 1
    else:
      print("That box is taken!")