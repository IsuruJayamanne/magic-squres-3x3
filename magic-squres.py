#!/bin/python3

import math
import os
import random
import re
import sys
# from itertools import product
# import itertools
from itertools import permutations

#
# Complete the 'formingMagicSquare' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY s as parameter.
#

def getCost(S, G):
    difference_matrix = [[abs(S[i][j] - G[i][j]) for j in range(3)] for i in range(3)]
    total_difference = sum(sum(row) for row in difference_matrix)

    return total_difference
    pass

# def is_magic_square(matrix):
#     # Check if a 3x3 matrix is a magic square.
#     s = sum(matrix[0])

#     # Check rows and columns
#     for i in range(3):
#         if sum(matrix[i]) != s or sum(matrix[j][i] for j in range(3)) != s:
#             return False

#     # Check diagonals
#     if sum(matrix[i][i] for i in range(3)) != s or sum(matrix[i][2-i] for i in range(3)) != s:
#         return False

#     return True

def generate_magic_squares(s):
    min_cost = 100 # greater than max possible
    
    # Generates all possible 3x3 magic squares with distinct integers from 1 to 9
    from itertools import permutations

    # Generate all permutations of numbers 1 through 9
    for p in permutations(range(1, 10)):
        # Check if this permutation can form a magic square
        if (p[0] + p[1] + p[2] == p[3] + p[4] + p[5] == p[6] + p[7] + p[8] ==  # Rows
            p[0] + p[3] + p[6] == p[1] + p[4] + p[7] == p[2] + p[5] + p[8] ==  # Columns
            p[0] + p[4] + p[8] == p[2] + p[4] + p[6]):                         # Diagonals
            
            cost = getCost(s, [p[0:3], p[3:6], p[6:9]])
            if cost == 0:
                return 0
            if min_cost > cost:
                min_cost = cost

    return min_cost
                
def formingMagicSquare(s):
    # Write your code here
    cost = generate_magic_squares(s)
    print(cost)
    

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    # s = []

    # for _ in range(3):
    #     s.append(list(map(int, input().rstrip().split())))

    # result = formingMagicSquare(s)

    # fptr.write(str(result) + '\n')

    # fptr.close()
    s = [[4, 9, 2], [3, 5, 7], [8, 1, 5]]
    formingMagicSquare(s)

