from random import randint
n=5
matrix=[[randint(0,100) for i in range(n)] for j in range(n)]
print(matrix)
max_element = max(max(row) for row in matrix)
print(max_element)