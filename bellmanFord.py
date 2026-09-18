from matrixCreator import create_matrix
import sys
import math
import time

def print_matrix(matrix):
    length = 5
    letters = "abcdefghijklmnopqrstuvwxyz"
    printed = [letters[i] for i in range(0, len(matrix[0]))]
    for letter in printed:
        print(letter + " "*(4), end="")
    print("")
    for index, row in enumerate(matrix):
        print(printed[index], end=" ")
        for cell in row:
            print(str(cell) + " "* (5 - (1 if cell == 0  else int(math.log10(cell)))), end="")
        print("")

def relax(u, v, distanceMatrix, D):
    if D[u] + distanceMatrix[u][v] < D[v]:
        D[v] = D[u] + distanceMatrix[u][v]

def bellmanFord(distanceMatrix):
    D = [1000] * len(distanceMatrix)
    D[0] = 0

    for i in range(0, len(D)):
        for j in range(0, len(distanceMatrix)):
            for k in range(0, len(distanceMatrix[j])):
                if j != k and distanceMatrix[j][k] != 1000:
                    relax(j, k, distanceMatrix, D)
    print_matrix(distanceMatrix)
    print(D)

matrix = create_matrix(int(sys.argv[1]))
before = time.time()
bellmanFord(matrix)
after = time.time()

print(f"TIME TAKEN: {after-before}s")