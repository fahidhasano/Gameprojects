
def sum(a,b,c):
    return a+b+c




def checkboard(xState,zState):
    one="X" if xState[0] else ("0" if zState[0] else 0 )
    two = "X" if xState[1] else ("0" if zState[1] else 1)
    three = "X" if xState[2] else ("0" if zState[2] else 2)
    four = "X" if xState[3] else ("0" if zState[3] else 3)
    five = "X" if xState[4] else ("0" if zState[4] else 4)
    six = "X" if xState[5] else ("0" if zState[5] else 5)
    seven = "X" if xState[6] else ("0" if zState[6] else 6)
    eight  = "X" if xState[7] else ("0" if zState[7] else 7)
    nine = "X" if xState[8] else ("0" if zState[8] else 8)

    print("Welcome to Tic Tac Toe hotties!!!")
    print(f"{one}||{two}||{three}")
    print(f"{four}||{five}||{six}")
    print(f"{seven}||{eight}||{nine}")


def checkwin(xState,zState):
    wins= [[0,1,2],[3,4,5],[6,7,8],[0,4,8],[2,4,6],[0,3,6],[1,4,7],[2,5,8]]
    for x in wins:
        if(sum(xState[x[0]],xState[x[1]],xState[x[2]])==3):
            print("X is the winner")
            return 1
        else:
            if (sum(zState[x[0]], zState[x[1]], zState[x[2]]) == 3):
                print("0 is the winner")
                return 0
    return -1







if __name__=="__main__":
    xState=[0,0,0,0,0,0,0,0,0]
    zState = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    flag=1
    while(True):
        checkboard(xState,zState)
        if(flag==1):
            print("X's turn")
            value= int(input("Enter a value"))
            xState[value]=1
        else:
            print("0 's turn")
            value=int(input("Enter"))
            zState[value]=1

        csk= checkwin(xState,zState)
        if(csk!=-1):
            print("match over")
            break
        flag = 1 - flag






