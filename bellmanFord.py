from matrixCreator import create_matrix
import sys
import math
import time
import numpy as np
import argparse

def num_digits(number):
    if number == 0:
        return 1
    else:
        return int(math.log10(abs(number))) + 1

def print_matrix(edges, size):
    matrix = np.zeros((size, size))
    for edge in edges:
        matrix[edge[0], edge[1]] = edge[2]

    indices = [str(i) for i in range(size)]
    print(" " * num_digits(size), end="")
    for num in indices:
        print(" "* (4) + num + " " *  (2-num_digits(int(num))), end="")
    print()
    print("  " + "-"*(1 + (size*6)))
    for index, row in enumerate(matrix):
        spaces = " " * (num_digits(size) - num_digits(index) + 1)
        print(indices[index] + spaces + "|", end="")
        print(" ", end="")
        for cell in row:
            print(" " if cell >= 0 else "", end="")
            print(str(int(cell)) + " "* (5 - num_digits(int(cell))), end="")
        print()

def relax(edge, D):
    if D[edge[0]] + edge[2] < D[edge[1]]:
        D[edge[1]] = D[edge[0]] + edge[2]

def bellmanFord(distanceMatrix, size):
    before = time.time()
    D = [1000] * size
    D[0] = 0
    negative_loop = False
    for i in range(0, len(D)+1):
        for edge in distanceMatrix:
            if D[edge[0]] + edge[2] < D[edge[1]]:
                if i == len(D):
                    negative_loop = True
                    break
                D[edge[1]] = D[edge[0]] + edge[2]
    after = time.time()
    if negative_loop:
        return "Negative loop found: no valid result returned.", after-before
    else:
        return D, after-before


if __name__ == '__main__':

    parser = argparse.ArgumentParser()
    parser.add_argument("size", type=int, help="Size of matrix")
    parser.add_argument("-v", "--verbose", help="Print time taken to compute distances", action="store_true")
    args = parser.parse_args()

    size = args.size
    verbose = args.verbose
    
    edges = create_matrix(size)
    print_matrix(edges, size)
    result, time_taken = bellmanFord(edges, size)
    print("Results:")
    print(result)
    if verbose:
        units = ["s", "ms", "μs", "ns"]
        unit_index = 0
        while time_taken < 1:
            time_taken *= 1000
            unit_index += 1
        
        print(f"TIME TAKEN: {round(time_taken, 2)}{units[unit_index]}")