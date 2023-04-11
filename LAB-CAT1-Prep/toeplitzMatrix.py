N=5
M=4

def isToeplitz( matrix):
	for i in range(1,N):
		for j in range(1,M):
			# check if each index is equal to its
			# diagonally upper index if not return false
			if (matrix[i][j] != matrix[i - 1][j - 1]):
				return False;
		
	return True;

# Driver code
mat = [ [ 6, 7, 8, 9 ],
	  [ 4, 6, 7, 8 ],
	  [ 1, 4, 6, 7 ],
      [ 0, 1, 4, 6 ],
      [ 2, 0, 1, 4 ] ]

# Function call
if (isToeplitz(mat)):
	print("Matrix is a Toeplitz ")
else:
	print("Matrix is not a Toeplitz ")

