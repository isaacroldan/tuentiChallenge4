########################################## 
#   
#  #TuentiChallenge4 (2014).
#  Challenge 15: Take a corner
#  https://contest.tuenti.net/Challenges?id=15
#  Isaac Roldan (@saky)
#  
##########################################

#AGAIN: Don't reinvent the wheel, othello Class found here:
#http://dhconnelly.com/paip-python/docs/paip/othello.html

import othello


import copy
import pdb
import sys

EMPTY, BLACK, WHITE, OUTER = '.', 'X', 'O', '?'
SQUARE_WEIGHTS = [
    0,   0,   0,   0,   0,   0,   0,   0,   0,   0,
    0, 12000, -20,  -20,   -5,   -5,  -20, -20, 12000,   0,
    0, -20, -40,  -5,  -5,  -5,  -5, -40, -20,   0,
    0,  -20,  -5,  -15,  -3,   -3,  -15,  -5,  -20,   0,
    0,   5,  -5,   -3,   -3,   -3,   -3,  -5,   -5,   0,
    0,   5,  -5,   -3,   -3,   -3,   -3,  -5,   -5,   0,
    0,  -20,  -5,  -15,   -3,   -3,  -15,  -5,  -20,   0,
    0, -20, -40,  -5,  -5,  -5,  -5, -40, -20,   0,
    0, 12000, -20,  -20,   -5,   -5,  -20, -20, 12000,   0,
    0,   0,   0,   0,   0,   0,   0,   0,   0,   0,
]
MAX_VALUE = sum(map(abs, SQUARE_WEIGHTS))
MIN_VALUE = -MAX_VALUE
positions = []

def evaluate(player,board):
    #Evaluate the board, if the player has reached the corner, 2000 points! :D
    for p in positions:
        if board[p] == player:
            return 2000
    return 0

cases = int(raw_input(""))
for p in range(cases):
    play = raw_input("").split(" ")
    player = play[0]
    moves = int(play[2])
    matrix = []
    for l in range(8):
        line = raw_input("")
        matrix.append(line)

    board = othello.initial_board()
    for line in range(1,9):
        for col in range(1,9):
            move = int(str(line)+str(col))
            board[move]=matrix[line-1][col-1]

    player2 = ""
    if player == "White":
        player2 = "O"
    else:
        player2 = "X"

    #Don't test for a position if the user already has a disc there
    positions = [11,18,81,88]
    if board[11] == player2:
        positions.remove(11)
    if board[18] == player2:
        positions.remove(18)
    if board[81] == player2:
        positions.remove(81)
    if board[88] == player2:
        positions.remove(88)

    #Alphabeta Algorithm :)
    value, pos =  othello.alphabeta(player2,board,MIN_VALUE,MAX_VALUE,moves*2,evaluate)
    pos2 = pos
    if value<=0 or not pos:
        print "Impossible"

    else:
        pos2 = str(pos2)[::-1]
        first = str(pos2)[0]
        s = ""
        if first == "1":
            s = "a"
        if first == "2":
            s = "b"
        if first == "3":
            s = "c"
        if first == "4":
            s = "d"
        if first == "5":
            s = "e"
        if first == "6":
            s = "f"
        if first == "7":
            s = "g"
        if first == "8":
            s = "h"
            
        print s + str(pos2)[1]




