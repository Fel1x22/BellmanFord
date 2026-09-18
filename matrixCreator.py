import random


def create_matrix(nodes):
    matrix = [[0 for _ in range(nodes)] for _ in range(nodes)]

    for i in range(nodes):
        for j in range(nodes):
            if j > i:
                chance = random.randint(1, 100)
                if chance < 50:
                    matrix[i][j], matrix[j][i] = 1000, 1000
                else:
                    dist = random.randint(1, 100)
                    matrix[i][j], matrix[j][i] = dist, dist
    return matrix