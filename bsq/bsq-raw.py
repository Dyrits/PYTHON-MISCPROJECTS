import numpy as np 
grid = [
  ["0", "1", "1", "0", "1", "0", "1"], 
  ["1", "1", "1", "1", "1", "1", "1"], 
  ["1", "1", "1", "0", "1", "1","0"], 
  ["1", "1", "1", "1", "1", "1", "1"], 
  ["1", "1", "1", "0", "1", "1", "1"],
  ["1", "1", "1", "0", "1", "1", "1"]
  ]
grid = np.array(grid)
print(grid)
valeur_test_c = 0
valeur_test_r = 0
valeur_max_r = 0
valeur_max_c = 0
square_max = 0
index_r = 0
index_c = 0
square_expand = 0
while  valeur_test_r < len(grid) and valeur_test_r < (len(grid) - square_max):
	while valeur_test_c < len(grid[valeur_test_r]):
		index_r = valeur_test_r + 1
		index_c = valeur_test_c + 1
		square_expand= 0
		while '0' not in grid[valeur_test_r:index_r, valeur_test_c:index_c] and index_c - 1 < len(grid[valeur_test_r]):
			square_expand +=1
			if square_expand > square_max:
				square_max = square_expand
				valeur_max_r = valeur_test_r
				valeur_max_c = valeur_test_c
			index_c +=1
			index_r +=1
		valeur_test_c +=1
	valeur_test_r += 1
	valeur_test_c = 0
grid[valeur_max_r:valeur_max_r+square_max, valeur_max_c:valeur_max_c+square_max] = "X"
print("Result:)")
print(grid)
	