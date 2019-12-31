# X=1, O=0

def printBox():  # The function to print the grid with X O.
    for x in range(0, 9, 3):
        print(sxo[x], "|", sxo[x+1], "|", sxo[x+2])
        if (x != 6):
            print("-", "-", "-", "-", "-")


def printBox2():  # The function to print the grid with numbers.
    for x in range(0, 9, 3):
        print(s[x], "|", s[x+1], "|", s[x+2])
        if (x != 6):
            print("-", "-", "-", "-", "-")

def put(L, XO):  # A function to put 0 == O or 1 == X in the grid.
    a = 0  # a is to check if location is available or not.
    while a == 0:
        if s[L] != 0:
            if s[L] != 1:
                s[L] = XO
                if XO == 1:
                    sxo[L] = 'X'
                else:
                    sxo[L] = 'O'
                a = 1
            else:
                print("Entered location not available, try another location!")
                L = int(input())
        else:
            print("Entered location not available, try another location!")
            L = int(input())

    if(((s[0] == s[4]== s[8] == 0) | (s[0]==s[4]==s[8] == 1)) | ((s[2]==s[4]==s[6] == 0) | (s[2]==s[4]==s[6] == 1))):  # Diagonal check for win.
        print(sxo[L], 'has won!')
        return 1

    for x in range(0, 9, 3):  # row check for win.
        if((s[x] == s[x + 1] == s[x + 2] == 0) | (s[x] == s[x + 1] == s[x + 2] == 1)):
            print(sxo[L], 'has won!')
            print("\n")
            return 1

    for x in range(0, 3):  # Column check for win.
        if ((s[x] == s[x + 3] == s[x + 6] == 0) | (s[x] == s[x + 3] == s[x + 6] == 1)):
            print(sxo[L], 'has won!')
            print("\n")
            return 1
    return 0

play = 0  # Variable to continue play.

while play == 0:
    s = [0, 1, 2, 3, 4, 5, 6, 7, 8]  # Initial grid values, s contains the grid to play Tic Tac Toe
    t = 1  # t is the turn variable
    j = 0  # j is the variable to check if someone has won.
    sxo = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']

    print("Welcome to Tic Tac Toe")
    print("Remember the grid locations!\n")
    printBox2()  # Initial grid view.

    s = [9, 9, 9, 9, 9, 9, 9, 9, 9]  # New values to the grid to play.
    k = 0  # variable to check if draw has occurred, by adding the total number of turns less than 9.

    print("First X goes")

    while j == 0:

        if t == 1 and j == 0:
            L = int(input("Enter the location you want to write X, from 0 to 8"))
            j = put(L, t)
            # print("This is j ", j)
            t = 0
            printBox()
            k = k + 1
            if k > 8 and j == 0:
                print("Draw is inevitable!")
                break

        if t == 0 and j == 0:
            L = int(input("Enter the location you want to write O, from 0 to 8"))
            j = put(L, t)
            # print("This is j ", j)
            t = 1
            printBox()
            k = k + 1
            if k > 8 and j == 0:
                print("Draw is inevitable!")
                break

    play = int(input('To play again press number 0, else enter other integer!'))
    if play != 0:
        print('Thank you so much for playing Vzuu! :\')' )

pass