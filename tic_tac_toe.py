# TIC TAC TOE Tutorial by Code Coach
# https://www.youtube.com/watch?v=dK6gJw4-NCo

import random

board = ["-", "-", "-", 
         "-", "-", "-", 
         "-", "-", "-"]

currentPlayer = "X"
winner = None
gameRunning = True

# Printing the game board
def printBoard(board):
    print(board[0] + " | " + board[1] + " | " + board[2])
    print('---------')
    print(board[3] + " | " + board[4] + " | " + board[5])
    print('---------')
    print(board[6] + " | " + board[7] + " | " + board[8])

printBoard(board)

# Take player input
def player_input(board):
    inp = int(input("Enter a number 1-9: "))
    if inp >= 1 and inp <= 9 and board[inp-1] == '-':
        board[inp-1] = currentPlayer
    else:
        print("Ooops, player already in that spot!")

# Check for win or tie
def checkHorizontal(board):
    global winner
    if board[0] == board[1] == board[2] and board[0]!= "-":
        winner = board[0]
        return True
    elif board[3] == board[4] == board[5] != "-":
        winner = board[3]
        return True
    elif board[6] == board[7] == board[8] and board[6] != "-":
        winner = board[6]
        return True

def checkVertical(board):
    global winner
    if board[0] == board[3] == board[6] and board[0] != "-":
        winner = board[0]
        return True
    elif board[1] == board[4] == board[7] and board[1] != "-":
        winner = board[1]
        return True
    elif board[2] == board[5] == board[8] and board[2] != "-":
        winner = board[2]
        return True
    
def checkDiag(board):
    global winner
    if board[0] == board[4] == board[8] and board[0] != "-":
        winner = board[0]
        return True
    elif board[2] == board[4] == board[6] and board[2] != "-":
        winner = board[2]
        return True
    

def checkTie(board):
    global winner
    if "-" not in board:
        printBoard(board)
        print("It is a tie")
        global gameRunning 
        gameRunning = False

def checkWin():
    if checkDiag(board) or checkHorizontal(board) or checkVertical(board):
        printBoard(board)
        print(f"The winner is {winner}")
        global gameRunning 
        gameRunning = False
    else:
        pass

def switchPlayer():
    global currentPlayer
    if currentPlayer == "X":
        currentPlayer = "O"
    else:
        currentPlayer = "X"

    
# Switch the player
def computer(board):
    while currentPlayer == 'O':
        position = random.randint(0, 8)
        if board[position] == "-":
            board[position] ="O"
            switchPlayer()

# Check for win or tie again
while gameRunning:
    printBoard(board)
    player_input(board)
    checkWin()
    checkTie(board)
    switchPlayer()

    computer(board)
    checkWin()
    checkTie(board)

