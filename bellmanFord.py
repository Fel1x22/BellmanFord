from matrixCreator import create_matrix
import sys
import math
import time

def print_matrix(edges, size):
    matrix = [[0 for _ in range(size)] for _ in range(size)]
    for edge in edges:
        matrix[edge[0]][edge[1]] = edge[2]
    
    letters = "abcdefghijklmnopqrstuvwxyz"
    printed = [letters[i] for i in range(size)]
    for letter in printed:
        print(letter + " "* (4), end="")
    print("")
    for index, row in enumerate(matrix):
        print(printed[index], end=" ")
        for cell in row:
            print(str(cell) + " "* (5 - (1 if cell <= 0  else int(math.log10(cell)))), end="")
        print("")

def relax(edge, D):
    if D[edge[0]] + edge[2] < D[edge[1]]:
        D[edge[1]] = D[edge[0]] + edge[2]

def bellmanFord(distanceMatrix):
    D = [1000] * 5
    D[0] = 0
    negative_loop = False
    for i in range(0, len(D)+1):
        for j in distanceMatrix:
            if j[2] != 1000 and D[j[0]] + j[2] < D[j[1]]:
                """relax(j, D)"""
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
    bellmanFord(edges)
    after = time.time()

    print(f"TIME TAKEN: {after-before}s")