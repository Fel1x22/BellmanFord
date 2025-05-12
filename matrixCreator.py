import random

nodes = int(input("Number of nodes: "))
matrix = []

for i in range(nodes):
    row = []
    for j in range(nodes):

        if i == j:
            row.append(0)
        else:
            chance = random.randint(1, 100)
            if chance < 30:
                try:
                    if matrix[j][i] != 1000:
                        row.append(1000)
                    else:
                        row.append(random.randint(1, 30))
                except:
                    row.append(random.randint(1, 30))
            else:
                row.append(1000)
    matrix.append(row)

print(matrix)