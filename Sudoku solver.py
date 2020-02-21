
Grid = [
    [0, 3, 2, 0, 0, 0, 5, 0, 0],
    [4, 0, 0, 2, 0, 0, 0, 8, 0],
    [0, 0, 0, 0, 0, 0, 4, 7, 0],
    [5, 2, 0, 0, 7, 0, 0, 0, 4],
    [0, 0, 0, 1, 0, 6, 0, 0, 0],
    [7, 0, 0, 0, 5, 0, 0, 3, 9],
    [0, 9, 7, 0, 0 ,0, 0, 0, 0],
    [0, 6, 0, 0, 0, 3, 0, 0, 5],
    [0, 0, 5, 0, 0, 0, 7, 9, 0]
    ]

#We create a copy of the list to keep the original values.
import copy
GridCopy = copy.deepcopy(Grid)

#The grid includes 81 entries from 0 to 80. It is separated from Grid[0]|0] to Grid[8][8]. We need to be able to identify the indexes.
def LocatorR(N):
    LocatorR = N//9
    #Locator (Row) 
    return LocatorR

def LocatorC(N):
    LocatorC = N%9
    #Locator (Column)
    return LocatorC

#We set the indexes for a given value. For example, if N=15, it would return 1 and 6 which is the position of the 16th entrie in the grid.


def NValue(G, N):
    LR = LocatorR(N)
    LC = LocatorC(N)
    #We set the two locators so we can use them as index in the grid.
    NValue = G[LR][LC]
    return NValue
    #The functiun pick and return the value of the entry N.


#We create a function to isolate one of the 9 subgrid (3X3) concerned by the entry N.
def SubGrid(G, N):
    LR = LocatorR(N)//3*3
    LC = LocatorC(N)//3*3
    #We set LR and LC as the indexes for the starting row and starting column of the subgrid.
    #The maximum value for LR and LC are 8. Using this operation, we obtain value of 0, 3 or 6.
    #We add the 3 values from LR and LC to the list SubGrid (and repeat it for the 2 next rows): 
    SubGrid = []
    for R in range(0, 3):
        SubGrid += G[LR+R][LC:LC+3]
    return SubGrid

#We create a function to isolate the row concerned by the entry N as a list.
def Row(G, N):
    LR = LocatorR(N)
    Row = G[LR][0:9]
    return Row

#We create a function to isolate the column concerned by the entry N as a list.
def Column(G, N):
    LC = LocatorC(N)
    Column = [R[LC] for R in G]
    return Column


print(*Grid, sep="\n")

Next = True
Back = False
N = 0

while N < 81:
##The grid includes 81 entries from 0 to 80. As long as N is under 81, the loop will be running.

    if NValue(GridCopy, N) != 0 and Next:
    #We are checking if the value of the entry N in the copy of the Grid is 0. We use the copy because it will keep the original values and not be modified.
    #We also verify if Next is True, allowing us to know if we'll continue to go forwards or backwards in the Grid.
        N += 1
        print("Pre-established entry. Going to next entry...")
        #If N is not 0, the value is a pre-established one, and we skip it. 
    elif NValue(GridCopy, N) == 0 and Next:
        for NSolved in range(1, 10):
        #The value of N, once solved, can only be between 1 and 9. We check every number until we find one fitting the following condition:
            if NSolved not in SubGrid(Grid, N) and NSolved not in Row(Grid, N) and NSolved not in Column(Grid, N):
            #We check if the value of N already exist in the subgrid, row and column. If not:
                Grid[LocatorR(N)][LocatorC(N)] = NSolved
                print("Next to next. Updating grid...")
                print("Writing:", NSolved)
                print(*Grid, sep="\n")
                #We attribute the value of NSolved where N is located.
                N += 1
                #We itterate, and exit the loop.
                break
            else:
                print("The value", NSolved, "is invalid here.")
                if NSolved == 9:
                    print("Cannot place anything here. Going to previous entry...")
                    #If we reach the end of the allowed range without any valid value, we need to go back to the previous entry.
                    Next = False
                    Back = True
                    N -= 1
                    #We go back an entry and exit the loop.
                    break
#If we are not going backwards, we have different but quite similar conditions.
    elif NValue(GridCopy, N) != 0 and Back:
        N -= 1
        print("Pre-established entry. Going to previous entry...")
        #If N is not 0, the value is a pre-established one, and we skip it, going back to another more entry.
    elif NValue(GridCopy, N) == 0 and Back:
        if Grid[LocatorR(N)][LocatorC(N)] == 9:
            Grid[LocatorR(N)][LocatorC(N)] = 0
            print("Maximum value already reached. Resetting and goint to previous entry...")
            #If the value of N is not a pre-established one but already reached 9, we set it back to 0, and go back to another more entry.
            N -= 1
        else:
            for NSolved in range(NValue(Grid, N)+1, 10):
            #The value of N, once solved, can only be between 1 and 9. Since we already went backwards, we are testing a new value incrementing the previous value up to 9.
                if NSolved not in SubGrid(Grid, N) and NSolved not in Row(Grid, N) and NSolved not in Column(Grid, N):
                    Grid[LocatorR(N)][LocatorC(N)] = NSolved
                    print("Back to next. Updating grid...")
                    print("Writing:", NSolved)
                    print(*Grid, sep="\n")
                    Next = True
                    Back = False
                    #Once we find a new value NSolved to set, we are going back forward and exit the loop.
                    N += 1
                    break
                else:
                    print("The value", NSolved, "is invalid here.")
                    if NSolved == 9:
                        print("Cannot place anything new here. Resetting and going to previous entry...")
                        Grid[LocatorR(N)][LocatorC(N)] = 0
                        N -= 1
                        break
print("The sudoku is solved!")
print("Solution:")
print(*Grid, sep="\n")
