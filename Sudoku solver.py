
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
GridCopy = [R[:] for R in Grid]

#The grid includes 81 entries from 0 to 80. It is separated from Grid[0]|0] to Grid[8][8]. We need to be able to identify the indexes.
#For example, if N=15, it would return 1 and 6 which are the positions of the 16th entry in the grid.
#We isolate the indexes for a given entry N:
IR = lambda N : N // 9
#Index (Row).
IC = lambda N : N % 9
#Index (Column).

#We also need to be able to identify the value of the entry, according to its position in the grid:
NValue = lambda G, N : G[IR(N)][IC(N)]

#We create a function to isolate one of the 9 subgrid (3X3) concerned by the entry N:
def SubGrid(G, N):
    #We set ISR and ISC as the indexes for the starting row and starting column of the subgrid:
    ISR = IR(N) // 3 * 3
    ISC = IC(N) // 3 * 3
    #The maximum value for IR and IC are 8. Using this operation, we obtain value of 0, 3 or 6.
    #We add the 3 values from IR and IC to the list SubGrid (and repeat it for the 2 next rows): 
    SubGrid = []
    for R in range(0, 3):
        SubGrid += G[ISR+R][ISC:ISC+3]
    return SubGrid

#We create a function to isolate the row concerned by the entry N as a list:
Row = lambda G, N : G[IR(N)][0:9]

#We create a function to isolate the column concerned by the entry N as a list:
Column = lambda G, N : [R[IC(N)] for R in G]


#We display the initial grid:
print(*Grid, sep="\n")

#We set different variables for the loop:
Next = True
Previous = False
#Next and Previous are used to determined if we are going through the grid forward or backward.
N = 0
#N is the entry targeted in the grid. We start with the first one: 0.


while N < 81:
##The grid includes 81 entries from 0 to 80. As long as N is under 81, the loop will be running.

#Forwards conditions :

    if NValue(GridCopy, N) != 0 and Next:
    #We are checking if the value of the entry in the copy of the grid is 0. We use the copy because it will keep the original values and not be modified.
        print("Pre-established entry. Skipping to the next entry...")
        N += 1
        #If N is not 0, the value is a pre-established one, and we skip it. 

    elif NValue(GridCopy, N) == 0 and Next:
    #If the value of the entry is 0, we will proceed.

        for NSolved in range(1, 10):
        #The value of the entry, once solved, can only be between 1 and 9. 
            
            #We check every number until we find one fitting the following condition:
            if NSolved not in SubGrid(Grid, N) and NSolved not in Row(Grid, N) and NSolved not in Column(Grid, N):
            #We check if the value of the entry is not already in the subgrid, row and column. 
                #If not, we can proceed by updating the value:
                Grid[IR(N)][IC(N)] = NSolved
                print("Valid value found! Updating the grid...")
                print("Writing:", NSolved)
                print(*Grid, sep="\n")
                #We itterate, and exit the loop:
                N += 1
                break

            #If the value of the entry already exists in the subgrid, row or column:
            else:
                print("The value", NSolved, "is invalid here.")
                if NSolved == 9:
                #We reach the end of the allowed range without any valid value.
                    #We need to go back to the previous entry:
                    print("Cannot place anything here. Going to previous entry...")
                    #We update the variables to go backward, and exit the loop:
                    Next = False
                    Previous = True
                    N -= 1
                    break

#Backwards conditions :

    elif NValue(GridCopy, N) != 0 and Previous:
        print("Pre-established entry. Going to previous entry...")
        N -= 1
        #If the value of the entry is not 0, the value is a pre-established one, and we skip it, going backwards once more.
    
    #If the value of the entry is 0:
    elif NValue(GridCopy, N) == 0 and Previous:
        
        if Grid[IR(N)][IC(N)] == 9:
            Grid[IR(N)][IC(N)] = 0
            print("Maximum value already reached. Resetting and goint to previous entry...")
            #If the value of N is not a pre-established one but already reached 9, we set it back to 0 because we can't go higher. Then, we go backwards once more:
            N -= 1
        
        else:
            for NSolved in range(NValue(Grid, N)+1, 10):
            #The value of N, once solved, can only be between 1 and 9. Since we already went backwards, we are testing a new value incrementing (one by one) the previous value up to 9.
               
                if NSolved not in SubGrid(Grid, N) and NSolved not in Row(Grid, N) and NSolved not in Column(Grid, N):
                #We check if the value of the entry is not already in the subgrid, row and column. 
                    #If not, we can proceed by updating the value:
                    Grid[IR(N)][IC(N)] = NSolved
                    print("New valid value. Updating grid...")
                    print("Writing:", NSolved)
                    print(*Grid, sep="\n")
                    #We update the variables to go forward, and exit the loop:
                    Next = True
                    Previous = False
                    N += 1
                    break

                #If the new value of the entry already exists in the subgrid, row or column:
                else:
                    print("The new value", NSolved, "is invalid here.")
                    if NSolved == 9:
                    #We reach the end of the allowed range without any new valid value.
                        #We need to reset the value to 0 and go back the previous entry, then exit the loop:
                        print("Cannot place anything new here. Resetting and going to previous entry...")
                        Grid[IR(N)][IC(N)] = 0
                        N -= 1
                        break


print("The sudoku is solved!")
print("Solution:")
print(*Grid, sep="\n")
