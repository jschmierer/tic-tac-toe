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
  if (player == 1):
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
def rowCheck(row):
  box1 = board[row][0]
  box2 = board[row][1]
  box3 = board[row][2]
  
  if (box1 == "" and box2 == "" and box3 == ""):
    return 0
  elif (box1 == box2 and box1 != ""):
    if (box1 == box3):
      if (box1 == "X"):
        print("You win!")
      else:
        print("Computer wins.")
      return 3
    else:
      if (box3 != ""):
        return 0
      return 2
  elif (box1 == box3 and box1 != ""):
    if (box2 != ""):
      return 0
    return 2
  elif (box2 == box3 and box2 != ""):
    if (box1 != ""):
      return 0
    return 2
  if (box1 != "" and box2 != ""):
    return 0
  elif (box1 != "" and box3 != ""):
    return 0
  elif (box2 != "" and box3 != ""):
    return 0
  return 1
  
def allRowCheck():
  m = 0
  for i in range(3):
    if (rowCheck(i) > m):
      m = rowCheck(i)
  return m
  
def colCheck(i):
  box1 = board[0][i]
  box2 = board[1][i]
  box3 = board[2][i]
  
  if (box1 == "" and box2 == "" and box3 == ""):
    return 0
  elif (box1 == box2 and box1 != ""):
    if (box1 == box3):
      if (box1 == "X"):
        print("You win!")
      else:
        print("Computer wins.")
      return 3
    else:
      if (box3 != ""):
        return 0
      return 2
  elif (box1 == box3 and box1 != ""):
    if (box2 != ""):
      return 0
    return 2
  elif (box2 == box3 and box2 != ""):
    if (box1 != ""):
      return 0
    return 2
  if (box1 != "" and box2 != ""):
    return 0
  elif (box1 != "" and box3 != ""):
    return 0
  elif (box2 != "" and box3 != ""):
    return 0
  return 1
    
def allColCheck():
  m = 0
  for i in range(3):
    if (colCheck(i) > m):
      m = colCheck(i)
  return m
  
def diagCheck(diag):
  if (diag == 0):
    box1 = board[0][0]
    box2 = board[1][1]
    box3 = board[2][2]
  else:
    box1 = board[0][2]
    box2 = board[1][1]
    box3 = board[2][0]
  if (box1 == "" and box2 == "" and box3 == ""):
    return 0
  elif (box1 == box2 and box1 != ""):
    if (box1 == box3):
      if (box1 == "X"):
        print("You win!")
      else:
        print("Computer wins.")
      return 3
    else:
      if (box3 != ""):
        return 0
      return 2
  elif (box1 == box3 and box1 != ""):
    if (box2 != ""):
      return 0
    return 2
  elif (box2 == box3 and box2 != ""):
    if (box1 != ""):
      return 0
    return 2
  if (box1 != "" and box2 != ""):
    return 0
  elif (box1 != "" and box3 != ""):
    return 0
  elif (box2 != "" and box3 != ""):
    return 0
  return 1

def allDiagCheck():
  m = 0
  for i in range(2):
    if (diagCheck(i) > m):
      m = diagCheck(i)
  return m

def winCheck():
  if (allRowCheck() == 3 or allColCheck() == 3 or allDiagCheck() == 3):
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
  
def openWin(row, a):
  arr = []
  if (a == "row"):
    for j in range(3):
      if (board[row][j] == ""):
        arr.append(str(j))
        if (j == 2):
          arr.append(board[row][j - 1])
        else:
          arr.append(board[row][j + 1])
  elif (a == "col"):
    for j in range(3):
      if (board[j][row] == ""):
        arr.append(str(j))
        if (j == 2):
          arr.append(board[j - 1][row])
        else:
          arr.append(board[j + 1][row])
  elif (a == "diag"):
    if (row == 0):
      for j in range(3):
        if (board[j][j] == ""):
          arr.append(str(j))
          arr.append(str(j))
          if (j == 2):
            arr.append(board[1][1])
          else:
            arr.append(board[j + 1][j + 1])
    else:
      for j in range(3):
        if (board[j][2 - j] == ""):
          arr.append(str(j))
          arr.append(str(2 - j))
          if (j == 1):
            arr.append(board[0][2])
          else:
            arr.append(board[1][1])
  return arr

def forkFinder():
  found = False
  if player == 1:
    letter = "X"
  else:
    letter = "O"
  for i in range(3):
    for j in range(3):
      if board[i][j] == "":
        board[i][j] = letter
        diag = -1
        if (i == 0 and j == 0) or (i == 1 and j == 1) or (i == 2 and j == 2):
          diag = 0
        elif (i == 0 and j == 2) or (i == 2 and j == 0):
          diag = 1
        if (diag != -1):
          if (rowCheck(i) == 2 and colCheck(j) == 2) or (rowCheck(i) == 2 and diagCheck(diag)) or (colCheck(j) and diagCheck(diag)):
            if letter == "O":
              board[i][j] = ""
              return (i, j)
            else:
              board[i][j] = ""
              found = True
              pos = (i, j)
          else:
            board[i][j] = ""
        else:
          if rowCheck(i) == 2 and colCheck(j) == 2:
            if letter == "O":
              board[i][j] = ""
              return (i, j)
            else:
              board[i][j] = ""
              found = True
              pos = (i, j)
          else:
            board[i][j] = ""
  if not found:
    return None
  else:
    return pos

def randCorner():
  arr = []
  possibles = [(0, 0), (0, 2), (2, 0), (2, 2)]
  random.shuffle(possibles)
  for row, col in possibles:
    if board[row][col] == "":
      arr.append(row)
      arr.append(col)
      return arr
  arr.append(-1)
  return arr
    

def randEdge():
  arr = []
  possibles = [(0, 1), (1, 0), (0, 1), (2, 1)]
  random.shuffle(possibles)
  for row, col in possibles:
    if board[row][col] == "":
      arr.append(row)
      arr.append(col)
      return arr
    
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

# random start
player = 0
flip = random.randint(0, 1)

if flip == 0:
  print("You (X) will go first!")
  player = 1
else:
  print("Computer (O) will go first!")
  player = 2

turn = 1

# game
while winCheck():
  if (player == 1):
    row = int(input("Pick a row to play: "))
    col = int(input("Pick a column: "))
    if ((row < 1 or row > 3) or (col < 1 or col > 3)):
      print("Please enter a valid box (rows 1-3, columns 1-3)")
    else:
      if (addToBoard(1, row, col)):
        printBoard()
        player = playerSwitch()
        turn += 1
      else:
        print("That box is taken!")
        
  else:
    close = False
    if turn == 1:
        arr = randCorner()
        row = arr[0]
        col = arr[1]
    else:
      #check if can immediately win
      for i in range(3):
        if (rowCheck(i) == 2):
          close = True
          arr = openWin(i, "row")
          if (arr[1] == "O"):
            row = i
            col = int(arr[0])
            break
          else:
            row = i
            col = int(arr[0])
      for i in range(3):
        if (colCheck(i) == 2):
          close = True
          arr = openWin(i, "col")
          if (arr[1] == "O"):
            row = int(arr[0])
            col = i
            break
          else:
            row = int(arr[0])
            col = i
      for i in range(2):
        if (diagCheck(i) == 2):
          close = True
          arr = openWin(i, "diag")
          if (arr[2] == "O"):
            row = int(arr[0])
            col = int(arr[1])
            break
          else:
            row = int(arr[0])
            col = int(arr[1])
      
      if (not close):
        pos = forkFinder()
        if (pos):
          close = True
          row = pos[0]
          col = pos[1]
          
        if (board[1][1] == ""):
          row = 1
          col = 1
        else:
          arr = randCorner()
          if (arr[0] != -1):
            row = arr[0]
            col = arr[1]
          else:
            arr = randEdge()
            row = arr[0]
            col = arr[1]
    addToBoard(2, row, col)
    print("Computers turn:")
    printBoard()
    player = playerSwitch()
    turn += 1