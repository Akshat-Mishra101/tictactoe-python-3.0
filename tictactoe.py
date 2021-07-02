dbboard = {'1':' ','2':' ','3':' ','4':' ','5':' ','6':' ','7':' ','8':' ','9':' '} #dictionary to store the values
boardkeys={'1':' ','2':' ','3':' ','4':' ','5':' ','6':' ','7':' ','8':' ','9':' '} #template dictionary to reset the original one
demo={'1':'1','2':' 2','3':' 3','4':'4','5':' 5','6':' 6','7':'7','8':' 8','9':' 9'}  #demo dictionary to display to the user for reference


def inputtaker(): #the given function takes the input and ensures that the value is valid
    while(True):
        inpu = input("Enter The Value Here:\n>>>")
        if inpu.isdigit() and int(inpu)<4 and int(inpu)>0:
            return inpu
        else:
            print("Please Enter A Valid Choice\n")

    
def ask_name(String1):
    while True:
        name = input(String1+"\n>>>")
        if name.isalpha():
            return name
        else:
            print("Please use only letters, try again")
            
def inputtaker2(player):
    value=""
    while(True):
        try:
            inpu = int(input(player+"'s Turn "+"Enter Your Move\n>>>"))
            if(inpu>0 and inpu<10):
                value=inpu
                break
            else:
                print("\nEnter A Value Between 1 and 9\n")
                continue
        except:
            print("\nPlease Enter A Valid Choice\n")  
            continue
    return value


def printtheboard(board):  #the given function prints the board onto the screen, along with the demo board
    print(board['1'] + ' |' + board['2'] + ' |' + board['3']+"                                "+demo['1'] + ' |' + demo['2'] + '|' + demo['3'])
    print('--+--+--'+"                               "+'--+--+--')
    print(board['4'] + ' |' + board['5'] + ' |' + board['6']+"                                "+demo['4'] + ' |' + demo['5'] + '|' + demo['6'])
    print('--+--+--'+"                               "+'--+--+--')
    print(board['7'] + ' |' + board['8'] + ' |' + board['9']+"                                "+demo['7'] + ' |' + demo['8'] + '|' + demo['9'])


def game(player1,player2):
    turn = 'X'
    count = 0
    currentplayer=player1
    while(count!=9):
        printtheboard(dbboard)
        cd=0;
        move = str(inputtaker2(currentplayer))
        if dbboard[move] == ' ':
            dbboard[move] = turn
            count +=1
            cd=0
        else:
            cd=1
            print("The Given Place Is Already Filled")
            continue
        if count >= 5:
            if dbboard['7'] == dbboard['8'] == dbboard['9'] != ' ': 
                printtheboard(dbboard)
                print("\nGame Over \n")                
                print(currentplayer+" Wins! The Round")
                return currentplayer
                break
            elif dbboard['4'] == dbboard['5'] == dbboard['6'] != ' ': 
                printtheboard(dbboard)
                print("\nGame Over.\n")                
                print(currentplayer+" Wins!")
                return currentplayer
                break
            elif dbboard['1'] == dbboard['2'] == dbboard['3'] != ' ': 
                printtheboard(dbboard)
                print("\nGame Over.\n")                
                print(currentplayer+" Wins! The Round")
                return currentplayer
                break
            elif dbboard['1'] == dbboard['4'] == dbboard['7'] != ' ': 
                printtheboard(dbboard)
                print("\nGame Over.\n")                
                print(currentplayer+" Wins! The Round")
                return currentplayer
                break
            elif dbboard['2'] == dbboard['5'] == dbboard['8'] != ' ': 
                printtheboard(dbboard)
                print("\nGame Over.\n")                
                print(currentplayer+" Wins! The Round")
                return currentplayer
                break
            elif dbboard['3'] == dbboard['6'] == dbboard['9'] != ' ': 
                printtheboard(dbboard)
                print("\nGame Over.\n")                
                print(currentplayer+" Wins! The Round")
                return currentplayer
                break 
            elif dbboard['7'] == dbboard['5'] == dbboard['3'] != ' ': 
                printtheboard(dbboard)
                print("\nGame Over.\n")                
                print(currentplayer+" Wins! The Round")
                return currentplayer
                break
            elif dbboard['1'] == dbboard['5'] == dbboard['9'] != ' ': 
                printtheboard(dbboard)
                print("\nGame Over.\n")                
                print(currentplayer+" Wins! The Round")
                return currentplayer
                break 

        if count == 9:
            print("\nGame Over.\n")                
            print("It's a Tie!!")
            return  "TIE"

        if turn =='X' and cd == 0:
            currentplayer=player2
            turn = 'O'
        else:
            currentplayer=player1
            turn = 'X'        
while(True):
    dbboard.update(boardkeys)
    print("__Welcome To The Tic-Tac-Toe Game__\n")
    print("Enter 1 For a single round match")
    print("Enter 2 for a 3 round match")
    print("Enter 3 to Exit")
    input1 = inputtaker()
    if input1=='3':
        print("Exiting the Game")
        break
    elif input1=='1':
        player1=ask_name("Enter First Player's Name")
        player2=ask_name("Enter Second Player's Name")
        winner=game(player1,player2)
        dbboard.update(boardkeys)
    elif input1=='2':
        player1=ask_name("Enter First Player's Name")
        a=b=0
        player2=ask_name("Enter Second Player's Name")
        getwinner1 = game(player1,player2)
        if getwinner1 == player1:
            a=a+1
        else:
            b=b+1
        dbboard.update(boardkeys)
        print("Round 2")
        getwinner2 = game(player1,player2)
        if getwinner2 == player1:
            a=a+1
        else:
            b=b+1
        dbboard.update(boardkeys)
        print("Round 3")
        dbboard.update(boardkeys)
        getwinner3= game(player1,player2)
        if getwinner3 == player1:
            a=a+1
        else:
            b=b+1
        
        if a>b:
            print(player1+" Wins The Match!")
        else:
            print(player2+" Wins The Match!")
