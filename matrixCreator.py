import random

def create_matrix(nodes):
    mode ="complete"
    max_weight = 100
    min_weight = -10

    edges = []

    if mode == "complete":
        for i in range(nodes):
            for j in range(nodes):
                if i == j:
                    continue
                dist = random.randint(min_weight, max_weight)
                edges.append([i, j, dist])
    return edges