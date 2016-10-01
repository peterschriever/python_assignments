from sys import exit
from itertools import chain
import numpy as np

#matrix = np.arange(9).reshape(3, 3)
matrix = np.array([
    [1,2,3],
    [4,3,5],
    [3,6,7]
])
print(matrix)

posdiag = [list(np.diagonal(matrix, i)) for i in range(-2, 3)]
matrix = np.fliplr(matrix)
negdiag = [list(np.diagonal(matrix, i)) for i in range(-2, 3)]
print("posdiag", posdiag)
print("negdiag", negdiag)

rows = matrix.tolist()
print("rows", rows)
cols = matrix.transpose().tolist()
print("cols", cols)

def lstCheckEqual(lst):
    return lst.count(lst[0]) == len(lst)

nInARow = 3 # 3 in a row
c = (rows, cols, posdiag, negdiag)
for lst in chain(*c): # for every list in the chain
    # for i in range(len(lst)-n+1):
    #     print("i in len(lst)-n+1: ",i, len(lst)-n+1)
    if len(lst) == nInARow and lstCheckEqual(lst):
        print(nInARow, "in a row!\nTeam", lst[0], "won!")
