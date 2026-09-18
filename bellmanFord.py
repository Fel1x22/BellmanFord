from matrixCreator import create_matrix
import sys
import math
import time
import numpy as np

def num_digits(number):
    if number == 0:
        return 0
    else:
        return int(math.log10(abs(number)))

def print_matrix(edges, size):
    matrix = np.zeros((size, size))
    for edge in edges:
        matrix[edge[0], edge[1]] = edge[2]

    indices = [str(i) for i in range(size)]
    for letter in indices:
        print(" "* (4) + letter + " "* (1), end="")
    print()
    print("  " + "-"*(1 + (size*6)))
    for index, row in enumerate(matrix):
        print(indices[index] + "|", end="")
        print(" ", end="")
        for cell in row:
            print(" " if cell >= 0 else "", end="")
            print(str(int(cell)) + " "* (4 - num_digits(int(cell))), end="")
        print()

def relax(edge, D):
    if D[edge[0]] + edge[2] < D[edge[1]]:
        D[edge[1]] = D[edge[0]] + edge[2]

def bellmanFord(distanceMatrix, size):
    D = [1000] * size
    D[0] = 0
    negative_loop = False
    for i in range(0, len(D)+1):
        for j in distanceMatrix:
            if j[2] != 1000 and D[j[0]] + j[2] < D[j[1]]:
                if i == len(D):
                    negative_loop = True
                    break
                D[j[1]] = D[j[0]] + j[2]
    if negative_loop:
        print("Negative loop found: no valid result returned.")
    else:
        print("Results:")
        print(D)


if __name__ == '__main__':
    if len(sys.argv) - 1 != 1:
        print("Error: Incorrect number of arguements entered. Please enter a valid integer for the matrix axis size.")
        exit()
    try:
        size = int(sys.argv[1])
    except:
        print("Error: Invalid axis size entered. Please enter a valid integer for the matrix axis size.")
        exit()
    
    edges = create_matrix(size)
    print_matrix(edges, size)
    before = time.time()
    bellmanFord(edges, size)
    after = time.time()

    print(f"TIME TAKEN: {after-before}s")