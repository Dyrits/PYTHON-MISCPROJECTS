Grid = [[0, 3, 2, 0, 0, 0, 5, 0, 0],[4, 0, 0, 2, 0, 0, 0, 8, 0],[0, 0, 0, 0, 0, 0, 4, 7, 0],[5, 2, 0, 0, 7, 0, 0, 0, 4],[0, 0, 0, 1, 0, 6, 0, 0, 0],[7, 0, 0, 0, 5, 0, 0, 3, 9],[0, 9, 7, 0, 0 ,0, 0, 0, 0],[0, 6, 0, 0, 0, 3, 0, 0, 5],[0, 0, 5, 0, 0, 0, 7, 9, 0]]
GridCopy = [R[:] for R in Grid]
IR = lambda N : N // 9
IC = lambda N : N % 9
NValue = lambda G, N : G[IR(N)][IC(N)]
def SubGrid(G, N):
	ISR = IR(N) // 3 * 3
	ISC = IC(N) // 3 * 3
	SubGrid = []
	SubGrid += (G[ISR+R][ISC:ISC+3] for R in range(0, 3))
	return SubGrid
Row = lambda G, N : G[IR(N)][0:9]
Column = lambda G, N : [R[IC(N)] for R in G]
print(*Grid, sep="\n")
Next = True
Previous = False
N = 0
while N < 81:
    if NValue(GridCopy, N) != 0 and Next:
        print("Pre-established entry. Skipping to the next entry...")
        N += 1
    elif NValue(GridCopy, N) == 0 and Next:
        for NSolved in range(1, 10):
            if NSolved not in SubGrid(Grid, N) and NSolved not in Row(Grid, N) and NSolved not in Column(Grid, N):
                Grid[IR(N)][IC(N)] = NSolved
                print("Valid value found! Updating the grid...")
                print("Writing:", NSolved)
                print(*Grid, sep="\n")
                N += 1
                break
            else:
                print("The value", NSolved, "is invalid here.")
                if NSolved == 9:
                    print("Cannot place anything here. Going to previous entry...")
                    Next = False
                    Previous = True
                    N -= 1
                    break
    elif NValue(GridCopy, N) != 0 and Previous:
        print("Pre-established entry. Going to previous entry...")
        N -= 1
    elif NValue(GridCopy, N) == 0 and Previous:
        
        if Grid[IR(N)][IC(N)] == 9:
            Grid[IR(N)][IC(N)] = 0
            print("Maximum value already reached. Resetting and goint to previous entry...")
            N -= 1
        else:
            for NSolved in range(NValue(Grid, N)+1, 10):
                if NSolved not in SubGrid(Grid, N) and NSolved not in Row(Grid, N) and NSolved not in Column(Grid, N):
                    Grid[IR(N)][IC(N)] = NSolved
                    print("New valid value. Updating grid...")
                    print("Writing:", NSolved)
                    print(*Grid, sep="\n")
                    Next = True
                    Previous = False
                    N += 1
                    break
                else:
                    print("The new value", NSolved, "is invalid here.")
                    if NSolved == 9:
                        print("Cannot place anything new here. Resetting and going to previous entry...")
                        Grid[IR(N)][IC(N)] = 0
                        N -= 1
                        break
print("The sudoku is solved!")
print("Solution:")
print(*Grid, sep="\n")