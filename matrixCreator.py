import random

def create_matrix(nodes):
    edges = []
    for i in range(nodes):
        for j in range(i+1, nodes):
            chance = random.randint(1, 100)
            if chance < 50:
                edges.append([i, j, 1000])
                edges.append([j, i, 1000])
            else:
                dist = random.randint(1, 100)
                edges.append([i, j, dist])
                edges.append([j, i, dist])
    return edges