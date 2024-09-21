
def sum(a,b,c):
    return a+b+c
def printBoard(xState,zState):
    one="X" if xState[0] else ("O" if zState[0] else 0)
    two="X" if xState[1] else ("O" if zState[1] else 1)
    three="X" if xState[2] else ("O" if zState[2] else 2)
    four="X" if xState[3] else ("O" if zState[3] else 3)
    five="X" if xState[4] else ("O" if zState[4] else 4)
    six="X" if xState[5] else ("O" if zState[5] else 5)
    seven="X" if xState[6] else ("O" if zState[6] else 6)
    eight="X" if xState[7] else ("O" if zState[7] else 7)
    nine="X" if xState[8] else ("O" if zState[8] else 8)

    print(f" {one} | {two}  | {three}  ")
    print(f" --| -- | --  ")
    print(f" {four} | {five}  | {six}  ")
    print(f" --| -- | --  ")
    print(f" {seven} | {eight}  | {nine}  ")
def checkwin(xState,zState):
    wins= [[0,1,2],[3,4,5],[6,7,8],[0,4,8],[2,4,6],[0,3,6],[1,4,7],[2,5,8]]
    for win in wins:

        if (sum(xState [win[0]],xState [win[1]],xState[win[2]])==3):
            print("X winner!! Chicken Dinner !!!")

            return 1

        if (sum(zState [win[0]],zState [win[1]],zState[win[2]])==3):
            print("O winner!! Chicken Dinner !!!")

            return 0
    return -1


if __name__ == "__main__":
    xState=[0,0,0,0,0,0,0,0,0]
    zState=[0,0,0,0,0,0,0,0,0]
    turn=1 #1 for X and 0 for O
    print("Welcome to tic tac toe")
    while(True):
        printBoard(xState,zState)
        if (turn==1):
            print("X's chance")
            value= int(input("Please enter a value:"))
            xState[value]=1
        else:
            print("0's chance")
            value = int(input("Please enter a value:"))
            zState[value] = 1

        cwin=checkwin(xState,zState)
        if(cwin!=-1):
            print("match over")
            break
        turn= 1-turn







