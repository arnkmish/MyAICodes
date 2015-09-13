""" TIC TAC TOE PLAYING SIMPLE REFLEX AGENT DESIGNED BY ARNAB KUMAR MISHRA (ARNKMISH)
EVERYTHING INSIDE THE FUNCTION NAMED get_move() IS WRITTEN BY ARNAB KUMAR MISHRA, OTHER THAN THE PART OF THE ONLY ELSE PORTION INSIDE THE FUNCTION.
ALSO THE LOGIC FOR TAKING USER INPUT FOR SELECTING X OR O IS ALSO WRITTEN BY ARNAB KUMAR MISHRA. """
import random
def print_board():
    for i in range(0,3):
        for j in range(0,3):
            print map[2-i][j],
            if j != 2:
                print "|",
        print ""


def check_done():
    for i in range(0,3):
        if map[i][0] == map[i][1] == map[i][2] != " " \
        or map[0][i] == map[1][i] == map[2][i] != " ":
            print turn, "won!!!"
            return True
        
    if map[0][0] == map[1][1] == map[2][2] != " " \
    or map[0][2] == map[1][1] == map[2][0] != " ":
        print turn, "won!!!"
        return True

    if " " not in map[0] and " " not in map[1] and " " not in map[2]:
        print "Draw"
        return True
        

    return False
# Get the move to be played by the agent, based on the current board position.
def get_move(map, com, human):# The whole function other than the else part is written by Arnab.
    # If possible try to win
    # Attack Horizontally
    if map[0][0] == " " and map[0][1] == com and map[0][2] == com:
        map[0][0] = com
        return None
    elif map[0][0] == com and map[0][1] == " " and map[0][2] == com:
        map[0][1] = com
        return None
    elif map[0][0] == com and map[0][1] == com and map[0][2] == " ":
        map[0][2] = com
        return None
    elif map[1][0] == " " and map[1][1] == com and map[1][2] == com:
        map[1][0] = com
        return None
    elif map[1][0] == com and map[1][1] == " " and map[1][2] == com:
        map[1][1] = com
        return None
    elif map[1][0] == com and map[1][1] == com and map[1][2] == " ":
        map[1][2] = com
        return None
    elif map[2][0] == " " and map[2][1] == com and map[2][2] == com:
        map[2][0] = com
        return None
    elif map[2][0] == com and map[2][1] == " " and map[2][2] == com:
        map[2][1] = com
        return None
    elif map[2][0] == com and map[2][1] == com and map[2][2] == " ":
        map[2][2] = com
        return None
    # Attack Vertically
    elif map[0][0] == " " and map[1][0] == com and map[2][0] == com:
        map[0][0] = com
        return None
    elif map[0][0] == com and map[1][0] == " " and map[2][0] == com:
        map[1][0] = com
        return None
    elif map[0][0] == com and map[1][0] == com and map[2][0] == " ":
        map[2][0] = com
        return None
    elif map[0][1] == " " and map[1][1] == com and map[2][1] == com:
        map[0][1] = com
        return None
    elif map[0][1] == com and map[1][1] == " " and map[2][1] == com:
        map[1][1] = com
        return None
    elif map[0][1] == com and map[1][1] == com and map[2][1] == " ":
        map[2][1] = com
        return None
    elif map[0][2] == " " and map[1][2] == com and map[2][2] == com:
        map[0][2] = com
        return None
    elif map[0][2] == com and map[1][2] == " " and map[2][2] == com:
        map[1][2] = com
        return None
    elif map[0][2] == com and map[1][2] == com and map[2][2] == " ":
        map[2][2] = com
        return None
    # Attack Diagonally
    elif map[0][0] == " " and map[1][1] == com and map[2][2] == com:
        map[0][0] = com
        return None
    elif map[0][0] == com and map[1][1] == " " and map[2][2] == com:
        map[1][1] = com
        return None
    elif map[0][0] == com and map[1][1] == com and map[2][2] == " ":
        map[2][2] = com
        return None
    elif map[0][2] == " " and map[1][1] == com and map[2][0] == com:
        map[0][2] = com
        return None
    elif map[0][2] == com and map[1][1] == " " and map[2][0] == com:
        map[1][1] = com
        return None
    elif map[0][2] == com and map[1][1] == com and map[2][0] == " ":
        map[2][0] = com
        return None
    # Try to defend when needed
    # Defend Horizontally
    elif map[0][0] == " " and map[0][1] == human and map[0][2] == human:
        map[0][0] = com
        return None
    elif map[0][0] == human and map[0][1] == " " and map[0][2] == human:
        map[0][1] = com
        return None
    elif map[0][0] == human and map[0][1] == human and map[0][2] == " ":
        map[0][2] = com
        return None
    elif map[1][0] == " " and map[1][1] == human and map[1][2] == human:
        map[1][0] = com
        return None
    elif map[1][0] == human and map[1][1] == " " and map[1][2] == human:
        map[1][1] = com
        return None
    elif map[1][0] == human and map[1][1] == human and map[1][2] == " ":
        map[1][2] = com
        return None
    elif map[2][0] == " " and map[2][1] == human and map[2][2] == human:
        map[2][0] = com
        return None
    elif map[2][0] == human and map[2][1] == " " and map[2][2] == human:
        map[2][1] = com
        return None
    elif map[2][0] == human and map[2][1] == human and map[2][2] == " ":
        map[2][2] = com
        return None
    # Defend Vertically
    elif map[0][0] == " " and map[1][0] == human and map[2][0] == human:
        map[0][0] = com
        return None
    elif map[0][0] == human and map[1][0] == " " and map[2][0] == human:
        map[1][0] = com
        return None
    elif map[0][0] == human and map[1][0] == human and map[2][0] == " ":
        map[2][0] = com
        return None
    elif map[0][1] == " " and map[1][1] == human and map[2][1] == human:
        map[0][1] = com
        return None
    elif map[0][1] == human and map[1][1] == " " and map[2][1] == human:
        map[1][1] = com
        return None
    elif map[0][1] == human and map[1][1] == human and map[2][1] == " ":
        map[2][1] = com
        return None
    elif map[0][2] == " " and map[1][2] == human and map[2][2] == human:
        map[0][2] = com
        return None
    elif map[0][2] == human and map[1][2] == " " and map[2][2] == human:
        map[1][2] = com
        return None
    elif map[0][2] == human and map[1][2] == human and map[2][2] == " ":
        map[2][2] = com
        return None
    # Defend Diagonally
    elif map[0][0] == " " and map[1][1] == human and map[2][2] == human:
        map[0][0] = com
        return None
    elif map[0][0] == human and map[1][1] == " " and map[2][2] == human:
        map[1][1] = com
        return None
    elif map[0][0] == human and map[1][1] == human and map[2][2] == " ":
        map[2][2] = com
        return None
    elif map[0][2] == " " and map[1][1] == human and map[2][0] == human:
        map[0][2] = com
        return None
    elif map[0][2] == human and map[1][1] == " " and map[2][0] == human:
        map[1][1] = com
        return None
    elif map[0][2] == human and map[1][1] == human and map[2][0] == " ":
        map[2][0] = com
        return None
    # If the board is empty then mark the center to increase winning chances
    elif map[0][0] == " " and map[0][1] == " " and map[0][2] == " " and map[1][0] == " " and map[1][1] == " " and map[1][2] == " " and map[2][0] == " " and map[2][1] == " " and map[2][2] == " ":
        map[1][1] = com 
        return None
    # If after marking the center human opponent marks a non corner square then mark one of the farthest corner squares to seal the win
    elif map[0][0] == " " and map[0][1] == human and map[0][2] == " " and map[1][0] == " " and map[1][1] == com and map[1][2] == " " and map[2][0] == " " and map[2][1] == " " and map[2][2] == " ":
        map[2][2] = com 
        return None
    elif map[0][0] == " " and map[0][1] == " " and map[0][2] == " " and map[1][0] == " " and map[1][1] == com and map[1][2] == human and map[2][0] == " " and map[2][1] == " " and map[2][2] == " ":
        map[2][0] = com 
        return None
    elif map[0][0] == " " and map[0][1] == " " and map[0][2] == " " and map[1][0] == " " and map[1][1] == com and map[1][2] == " " and map[2][0] == " " and map[2][1] == human and map[2][2] == " ":
        map[0][0] = com 
        return None
    elif map[0][0] == " " and map[0][1] == " " and map[0][2] == " " and map[1][0] == human and map[1][1] == com and map[1][2] == " " and map[2][0] == " " and map[2][1] == " " and map[2][2] == " ":
        map[0][2] = com 
        return None
    # After bot marks center, and human marks a corner, mark the diagonally oppsite square w.r.t the human mark
    elif map[0][0] == " " and map[0][1] == " " and map[0][2] == " " and map[1][0] == " " and map[1][1] == com and map[1][2] == " " and map[2][0] == " " and map[2][1] == " " and map[2][2] == human:
        map[0][0] = com
        return None
    elif map[0][0] == " " and map[0][1] == " " and map[0][2] == " " and map[1][0] == " " and map[1][1] == com and map[1][2] == " " and map[2][0] == human and map[2][1] == " " and map[2][2] == " ":
        map[0][2] = com
        return None
    elif map[0][0] == human and map[0][1] == " " and map[0][2] == " " and map[1][0] == " " and map[1][1] == com and map[1][2] == " " and map[2][0] == " " and map[2][1] == " " and map[2][2] == " ":
        map[2][2] = com
        return None
    elif map[0][0] == " " and map[0][1] == " " and map[0][2] == human and map[1][0] == " " and map[1][1] == com and map[1][2] == " " and map[2][0] == " " and map[2][1] == " " and map[2][2] == " ":
        map[2][0] = com
        return None
    # Bot marks center, human marks corner, bot marks diagonally opposite corner and human marks non corner square, punish
    elif map[0][0] == com and map[0][1] == human and map[0][2] == " " and map[1][0] == " " and map[1][1] == com and map[1][2] == " " and map[2][0] == " " and map[2][1] == " " and map[2][2] == human:
        map[2][0] = com
        return None
    elif map[0][0] == com and map[0][1] == " " and map[0][2] == " " and map[1][0] == human and map[1][1] == com and map[1][2] == " " and map[2][0] == " " and map[2][1] == " " and map[2][2] == human:
        map[0][2] = com
        return None
    elif map[0][0] == " " and map[0][1] == " " and map[0][2] == com and map[1][0] == " " and map[1][1] == com and map[1][2] == human and map[2][0] == human and map[2][1] == " " and map[2][2] == " ":
        map[0][0] = com
        return None
    elif map[0][0] == " " and map[0][1] == human and map[0][2] == com and map[1][0] == " " and map[1][1] == com and map[1][2] == " " and map[2][0] == human and map[2][1] == " " and map[2][2] == " ":
        map[2][2] = com
        return None
    elif map[0][0] == human and map[0][1] == " " and map[0][2] == " " and map[1][0] == " " and map[1][1] == com and map[1][2] == " " and map[2][0] == " " and map[2][1] == human and map[2][2] == com:
        map[0][2] = com
        return None
    elif map[0][0] == human and map[0][1] == " " and map[0][2] == " " and map[1][0] == " " and map[1][1] == com and map[1][2] == human and map[2][0] == " " and map[2][1] == " " and map[2][2] == com:
        map[2][0] = com
        return None
    elif map[0][0] == " " and map[0][1] == " " and map[0][2] == human and map[1][0] == " " and map[1][1] == com and map[1][2] == " " and map[2][0] == com and map[2][1] == human and map[2][2] == " ":
        map[0][0] = com
        return None
    elif map[0][0] == " " and map[0][1] == " " and map[0][2] == human and map[1][0] == human and map[1][1] == com and map[1][2] == " " and map[2][0] == com and map[2][1] == " " and map[2][2] == " ":
        map[2][2] = com
        return None
    # If human marks the center, then mark a corner square
    elif map[0][0] == " " and map[0][1] == " " and map[0][2] == " " and map[1][0] == " " and map[1][1] == human and map[1][2] == " " and map[2][0] == " " and map[2][1] == " " and map[2][2] == " ":
        map[2][0] = com
        return None
    # If human marks center, bot marks corner square, human marks diagonally opposite square mark the corner square on the same row as the earlier mark by the bot
    elif map[0][0] == " " and map[0][1] == " " and map[0][2] == human and map[1][0] == " " and map[1][1] == human and map[1][2] == " " and map[2][0] == com and map[2][1] == " " and map[2][2] == " ": 
        map[2][2] =com
        return None
    # If human marks corner square, mark the center and proceed
    elif map[0][0] == " " and map[0][1] == " " and map[0][2] == " " and map[1][0] == " " and map[1][1] == " " and map[1][2] == " " and map[2][0] == human and map[2][1] == " " and map[2][2] == " ":
        map[1][1] =com
        return None
    elif map[0][0] == " " and map[0][1] == " " and map[0][2] == " " and map[1][0] == " " and map[1][1] == " " and map[1][2] == " " and map[2][0] == " " and map[2][1] == " " and map[2][2] == human:
        map[1][1] = com
        return None
    elif map[0][0] == " " and map[0][1] == " " and map[0][2] == human and map[1][0] == " " and map[1][1] == " " and map[1][2] == " " and map[2][0] == " " and map[2][1] == " " and map[2][2] == " ":
        map[1][1] = com
        return None
    elif map[0][0] == human and map[0][1] == " " and map[0][2] == " " and map[1][0] == " " and map[1][1] == " " and map[1][2] == " " and map[2][0] == " " and map[2][1] == " " and map[2][2] == " ":
        map[1][1] = com
        return None
    elif map[0][0] == " " and map[0][1] == " " and map[0][2] == " " and map[1][0] == human and map[1][1] == " " and map[1][2] == " " and map[2][0] == " " and map[2][1] == " " and map[2][2] == " ":
        map[1][1] = com
        return None
    elif map[0][0] == " " and map[0][1] == " " and map[0][2] == " " and map[1][0] == " " and map[1][1] == " " and map[1][2] == " " and map[2][0] == " " and map[2][1] == human and map[2][2] == " ":
        map[1][1] = com
        return None
    elif map[0][0] == " " and map[0][1] == " " and map[0][2] == " " and map[1][0] == " " and map[1][1] == " " and map[1][2] == human and map[2][0] == " " and map[2][1] == " " and map[2][2] == " ":
        map[1][1] = com
        return None
    elif map[0][0] == " " and map[0][1] == human and map[0][2] == " " and map[1][0] == " " and map[1][1] == " " and map[1][2] == " " and map[2][0] == " " and map[2][1] == " " and map[2][2] == " ":
        map[1][1] = com
        return None
    elif map[0][0] == " " and map[0][1] == " " and map[0][2] == human and map[1][0] == " " and map[1][1] == com and map[1][2] == " " and map[2][0] == human and map[2][1] == " " and map[2][2] == " ":
        map[0][1] = com
        return None
    elif map[0][0] == human and map[0][1] == " " and map[0][2] == " " and map[1][0] == " " and map[1][1] == com and map[1][2] == " " and map[2][0] == " " and map[2][1] == " " and map[2][2] == human:
        map[0][1] = com
        return None
    elif map[0][0] == " " and map[0][1] == human and map[0][2] == " " and map[1][0] == " " and map[1][1] == com and map[1][2] == " " and map[2][0] == human and map[2][1] == " " and map[2][2] == " ":
        map[0][0] = com
        return None
    elif map[0][0] == " " and map[0][1] == " " and map[0][2] == " " and map[1][0] == " " and map[1][1] == com and map[1][2] == human and map[2][0] == human and map[2][1] == " " and map[2][2] == " ":
        map[2][2] = com
        return None
    elif map[0][0] == " " and map[0][1] == " " and map[0][2] == " " and map[1][0] == human and map[1][1] == com and map[1][2] == " " and map[2][0] == " " and map[2][1] == " " and map[2][2] == human:
        map[2][0] = com
        return None
    elif map[0][0] == " " and map[0][1] == human and map[0][2] == " " and map[1][0] == " " and map[1][1] == com and map[1][2] == " " and map[2][0] == " " and map[2][1] == " " and map[2][2] == human:
        map[0][2] = com
        return None
    elif map[0][0] == " " and map[0][1] == " " and map[0][2] == human and map[1][0] == " " and map[1][1] == com and map[1][2] == " " and map[2][0] == " " and map[2][1] == human and map[2][2] == " ":
        map[2][2] = com
        return None
    elif map[0][0] == " " and map[0][1] == " " and map[0][2] == human and map[1][0] == human and map[1][1] == com and map[1][2] == " " and map[2][0] == " " and map[2][1] == " " and map[2][2] == " ":
        map[0][0] = com
        return None
    elif map[0][0] == human and map[0][1] == " " and map[0][2] == " " and map[1][0] == " " and map[1][1] == com and map[1][2] == " " and map[2][0] == " " and map[2][1] == human and map[2][2] == " ":
        map[2][0] = com
        return None
    elif map[0][0] == human and map[0][1] == " " and map[0][2] == " " and map[1][0] == " " and map[1][1] == com and map[1][2] == human and map[2][0] == " " and map[2][1] == " " and map[2][2] == " ":
        map[0][2] = com
        return None
    elif map[0][0] == " " and map[0][1] == " " and map[0][2] == " " and map[1][0] == human and map[1][1] == com and map[1][2] == " " and map[2][0] == " " and map[2][1] == human and map[2][2] == " ":
        map[2][0] = com
        return None
    elif map[0][0] == " " and map[0][1] == " " and map[0][2] == " " and map[1][0] == " " and map[1][1] == com and map[1][2] == human and map[2][0] == " " and map[2][1] == human and map[2][2] == " ":
        map[2][2] = com
        return None
    elif map[0][0] == " " and map[0][1] == human and map[0][2] == " " and map[1][0] == " " and map[1][1] == com and map[1][2] == human and map[2][0] == " " and map[2][1] == " " and map[2][2] == " ":
        map[0][2] = com
        return None
    elif map[0][0] == " " and map[0][1] == human and map[0][2] == " " and map[1][0] == human and map[1][1] == com and map[1][2] == " " and map[2][0] == " " and map[2][1] == " " and map[2][2] == " ":
        map[0][0] = com
        return None
    # If none of the rules mentioned above are matching then pick a random empty location for marking
    else:
        again = True
        while(again == True):
            pos = random.choice([1, 2, 3, 4, 5, 6, 7 ,8 , 9])
            if pos <=9 and pos >=1:
                    Y = pos/3
                    X = pos%3
                    if X != 0:
                        X -=1
                    else:
                        X = 2
                        Y -=1
                    
                    if map[Y][X] == " ":
                        map[Y][X] = com
                        #moved = True
                        break
                    else:
                        again = True
    return None 

# Ask the human player if he wants to go first.
repeat = True
while repeat == True:
    human = raw_input("Please enter X to play as X or O to play as O: ")
    human = human.upper()
    if (human == 'X'):
        com = 'O'
        repeat = False
    elif (human == 'O'):
        com = 'X'
        repeat = False 
    else:
        print("You didn't enter X or O.")
        repeat = True

turn = "X"
map = [[" "," "," "],
       [" "," "," "],
       [" "," "," "]]
done = False


# Switching between turns
while done != True:
    if(turn == human):
        print_board()
    
        print turn, "'s turn"
        print

        moved = False
        while moved != True:
            print "Please select position by typing in a number between 1 and 9, see below for which number that is which position..."
            print "7|8|9"
            print "4|5|6"
            print "1|2|3"
            print

            try:
                pos = int(raw_input("Select: "))
                if pos <=9 and pos >=1:
                    Y = pos/3
                    X = pos%3
                    if X != 0:
                        X -=1
                    else:
                        X = 2
                        Y -=1
                    
                    if map[Y][X] == " ":
                        map[Y][X] = turn
                        moved = True
                        done = check_done()

                        if done == False:
                            if turn == "X":
                                turn = "O"
                            else:
                                turn = "X"
                
            
            except:
                print "You need to add a numeric value"
    else:
        get_move(map, com, human)
        done = check_done()
        if done == False:
            if turn == "X":
                turn = "O"
            else:
                turn = "X"
if(done == True):
    print_board()
