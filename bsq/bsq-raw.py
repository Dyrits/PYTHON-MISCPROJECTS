import numpy as np 
grid = [
  ["0", "1", "1", "0", "1", "0", "1"], 
  ["1", "1", "1", "1", "1", "1", "1"], 
  ["1", "1", "1", "0", "1", "1", "0"], 
  ["1", "1", "1", "1", "1", "1", "1"], 
  ["1", "1", "1", "0", "1", "1", "1"],
  ["1", "1", "1", "0", "1", "1", "1"]
  ]
grid = np.array(grid)
print(grid)
row = 0
column = 0
row_max = 0
column_max = 0
square_max = 0
index_row = 0
index_column = 0
square_expansion = 0
while  row < len(grid) and row < (len(grid) - square_max):
	while column < len(grid[row]):
		index_row = row + 1
		index_column = column + 1
		square_expansion= 0
		while '0' not in grid[row:index_row, column:index_column] and index_column - 1 < len(grid[row]):
			square_expansion +=1
			if square_expansion > square_max:
				square_max = square_expansion
				row_max = row
				column_max = column
			index_column +=1
			index_row +=1
		column +=1
	row += 1
	column = 0
grid[row_max:row_max+square_max, column_max:column_max+square_max] = "X"
print("Result:)")
print(grid)
