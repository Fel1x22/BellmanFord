#Aiming to use this to test out teh Bellman Ford Algorithm

distanceMatrix = [[0, 1000, 7, 1000, 1, 3], [5, 0, 1000, 1000, 2, 1000], [1000, 1000, 0, 1000, 1000, 1000],
 [1000, 2, 1000, 0, 1000, 1000], [1000, 1000, 1000, 1000, 0, 6], [1000, 1000, 1000, 1000, 1000, 0], ]

D = [1000, 1000, 1000, 0, 1000, 1000]

def relax(u, v):
    if D[u] + distanceMatrix[u][v] < D[v]:
        D[v] = D[u] + distanceMatrix[u][v]


for i in range(0, len(D)):
    for j in range(0, len(distanceMatrix)):
        for k in range(0, len(distanceMatrix[j])):
            if j != k and distanceMatrix[j][k] != 1000:
                relax(j, k)

print(D)