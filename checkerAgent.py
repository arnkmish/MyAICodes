'''
HW3 submitted by Arnab Kumar Mishra. Implementation of minimax with Alpha Beta pruning
Pseudocode reference https://en.wikipedia.org/wiki/Alpha%E2%80%93beta_pruning
The algorithm looks ahead various levels based on time remaining and moves remaining.
'''
import gamePlay
from copy import deepcopy
from getAllPossibleMoves import getAllPossibleMoves


def evaluation(board, color):
    # Evaluation function 1
    # Count how many more pieces I have than the opponent
    
    opponentColor = gamePlay.getOpponentColor(color)
    
    value = 0
    # Loop through all board positions
    for piece in range(1, 33):
        xy = gamePlay.serialToGrid(piece)
        x = xy[0]
        y = xy[1]
                
        if board[x][y].upper() == color.upper():
            # DEFENSE : Side pieces are better defensed
            if y == 0 or y == 7:
                value = value + 0.02
            # ATTACK : Middle pieces attack more grids
            if piece in [6,7,8,9,10,11,14,15,16,17,18,19,22,23,24,25,26,27] :
                value = value + 0.06
            # Check if my piece is a king; assign a higher value
            if board[x][y] == color.upper():
                value = value + 3
            # Check if my piece is a Man; assign a normal value
            elif board[x][y] == color.lower():
                value = value + 2
            # DEFENSE : If I have diagonal pieces then they are defensed
            if x+1 <= 7:
                if y+1 <=7 and board[x+1][y+1].lower() == color.lower():
                    value = value + 0.1
                if y-1 >=0 and board[x+1][y-1].lower() == color.lower():
                    value = value + 0.1
            if x-1 >= 0:
                if y+1 <=7 and board[x-1][y+1].lower() == color.lower():
                    value = value + 0.1
                if y-1 >=0 and board[x-1][y-1].lower() == color.lower():
                    value = value + 0.1

        elif board[x][y].upper() == opponentColor.upper():
            # DEFENSE : Side pieces are better defensed
            if y == 0 or y == 7:
                value = value - 0.02
            # ATTACK : Middle pieces attack more grids
            if piece in [6,7,8,9,10,11,14,15,16,17,18,19,22,23,24,25,26,27] :
                value = value - 0.06
            # Check if my opponent's piece is a King; subtract a higher value
            if board[x][y] == opponentColor.upper():
                value = value - 3
            # Check if my opponent's piece is a Man; subtract a normal value
            elif board[x][y] == opponentColor.lower():
                value = value - 2
            # DEFENSE : If opponent has diagonal pieces then that's bad for me.
            if x+1 <= 7:
                if y+1 <=7 and board[x+1][y+1].lower() == opponentColor.lower():
                    value = value - 0.1
                if y-1 >=0 and board[x+1][y-1].lower() == opponentColor.lower():
                    value = value - 0.1
            if x-1 >= 0:
                if y+1 <=7 and board[x-1][y+1].lower() == opponentColor.lower():
                    value = value - 0.1
                if y-1 >=0 and board[x-1][y-1].lower() == opponentColor.lower():
                    value = value - 0.1
            
    return value
# A next move function that uses only board and color for Part 1 of HW3
def nextMove(board, color, time, movesRemaining):
    moves = getAllPossibleMoves(board, color)
    #Trying to find the move where I have best score
    print time
    ourColor = color
    best = None
    #flag = False
    # The Worst possible value for alpha
    alpha = -float('inf')
    # The Worst possible value for beta
    beta = float('inf')
    # When there's only one possible move that can be made, then no point in thinking
    if len(moves) == 1:
        return moves[0]
    else:
        for move in moves:
            newBoard = deepcopy(board)
            gamePlay.doMove(newBoard,move)
            if time > 50:
                if movesRemaining > 140:
                    depth = 5
                elif movesRemaining <=140 and movesRemaining > 80:
                    depth = 7
                else:
                    depth = 5
            elif time <= 50 and time > 30:
                depth = 5
            elif time <= 30 and time > 5:
                depth = 3
            else:
                depth = 1
            moveVal = alphaBetaOnMiniMax(newBoard, depth, alpha, beta, False, gamePlay.getOpponentColor(color), ourColor)
            if best == None or moveVal > best:
                bestMove = move
                best = moveVal
        return bestMove
    

def alphaBetaOnMiniMax(newBoard, depth, alpha, beta, turnMaxPlayer, color, ourColor):
    moves = getAllPossibleMoves(newBoard, color)
    # Base Case for recurssion
    if depth == 0 or len(moves) == 0:
        return evaluation(newBoard, ourColor)
    # If Max Player's turn then Maximize the alpha value
    if turnMaxPlayer == True:
        for move in moves:
            newBoard1 = deepcopy(newBoard)
            gamePlay.doMove(newBoard1, move)
            alpha = max(alpha, alphaBetaOnMiniMax(newBoard1, depth - 1, alpha, beta, False, gamePlay.getOpponentColor(color), ourColor))
            if alpha >= beta:
                break
        return alpha
    # If Min Player's turn then minimize beta value
    elif turnMaxPlayer == False:
        for move in moves:
            newBoard1 = deepcopy(newBoard)
            gamePlay.doMove(newBoard1, move)
            beta = min(beta, alphaBetaOnMiniMax(newBoard1, depth - 1, alpha, beta, True, gamePlay.getOpponentColor(color), ourColor))
            if alpha >= beta:
                break
        return beta